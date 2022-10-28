import os
import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from rapidfuzz import fuzz
from nltk.corpus import stopwords

from doctr.io import DocumentFile
from doctr.models import ocr_predictor

class Data_Reader:
    def __init__(self):
        self.word_list = []
        self.output = {}
        self.imgfile = None
        self.image = np.empty(shape=(0,0,0))
        self.image_shape = self.image.shape
        self.ocr_data = pd.DataFrame([], 
                    columns=self._result_column)
    
    @property
    def _result_column(self):
        columns = ['word', 'ymin', 'xmin', 'ymax', 'xmax', 'score']
        return columns
    
    def _update_info(self, img):
        self.image = img
        self.image_shape = img.shape
    
    def _update_result(self, result):
        #ocr_data = pd.DataFrame([])
        h, w, _ = self.image.shape
        boxes = result[1][0]
        words = result[2][0]
        boxes[:, [0, 2]] *= w
        boxes[:, [1, 3]] *= h
        boxes = boxes.astype(np.int32).tolist()
        for i, box in enumerate(boxes):
            temp_df = pd.DataFrame([], columns=self._result_column)
            xmin, ymin, xmax, ymax, _ = box
            temp_df.loc[i, 'word'] = words[i][0].lower()
            temp_df.loc[i, 'ymin'] = ymin
            temp_df.loc[i, 'xmin'] = xmin
            temp_df.loc[i, 'ymax'] = ymax
            temp_df.loc[i, 'xmax'] = xmax
            temp_df.loc[i, 'score'] = round(words[i][1], 4)
            self.ocr_data = pd.concat(
                    [self.ocr_data, temp_df], axis=0, copy=False)

    def visulize_image(self):
        if self.image.size > 0:
            plt.imshow(self.image)
            plt.show()
        else:
            print("Error : Image not selected")
            
    def infer(self, imgfile):
        model = ocr_predictor(pretrained=True)
        doc = DocumentFile.from_images(imgfile)
        self._update_info(doc[0])
        result = model(doc)
        self._update_result(result)
        return result
    
    def _update_db(self, imgfile):
        output = {}
        output['imgfile'] = imgfile
        output['word_list'] = self.word_list
        return output

    def upload_file(self, imgfile):
        if not os.path.exists(imgfile):
            print("File not found")
            return
        words = self.infer(imgfile)[2][0]
        if len(words) > 0:
            self.word_list = [word[0] for word in words]
        self.output = self._update_db(imgfile)
    
    def visualize_result(self):
        font = cv2.FONT_HERSHEY_SIMPLEX
        output_image = self.image.copy()
        index_list = u.ocr_data.index.to_list()
        for index in index_list:
            word = self.ocr_data.loc[index, 'word']
            ymin = self.ocr_data.loc[index, 'ymin']
            xmin = self.ocr_data.loc[index, 'xmin']
            ymax = self.ocr_data.loc[index, 'ymax']
            xmax = self.ocr_data.loc[index, 'xmax']
            #score = self.ocr_data.loc[index, 'score']
            #out_text = word + " : " + str(score*100)
            out_text = word
            output_image = cv2.rectangle(
                output_image, (xmin, ymin), (xmax, ymax), 
                color=(0, 0, 255), thickness=2
            )
            output_image = cv2.putText(
                output_image,  out_text, (xmin, ymin), font, 1,
                (0, 0, 255), 2, cv2.LINE_AA)
        plt.imshow(output_image)
        plt.show()

    def match(self, name, thresh=0.6):
        max_score = -1
        matched_word = None
        word_list = self.ocr_data['word'].to_list()
        word_list = [word for word in word_list if not word in \
                            set(stopwords.words('english'))]
        for word in word_list:
            score = fuzz.ratio(name.lower(), word) / 100
            if score > max_score:
                max_score = score
                matched_word = word
        if max_score < thresh:
            return None, None
        return matched_word, max_score

if __name__ == '__main__':
    folder = 'images/'
    imgfiles = glob.glob(os.path.join(folder, '*.jpg'))
    u = Data_Reader()
    u.upload_file(imgfiles[0])
    # print(u.word_list)
    # print(u.ocr_data)
    # u.visualize_result()
    # u.visulize_image()
    print(u.match('anf'))