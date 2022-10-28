import cv2
import matplotlib.pyplot as plt
from rapidfuzz import fuzz
from nltk.corpus import stopwords
from .uploader import read_json
from .params import dbfile

class Finder:
    def __init__(self):
        self.db_data = read_json(dbfile)

    def find_business_card(self, name, thresh=0.8, plot=False):
        db_score = -1
        #print("Data : ", self.db_data)
        for key, val in self.db_data.items():
            img_score = -1
            imgfile = val['imgfile']
            word_list = val['word_list']
            word_list = [word.lower() for word in word_list if not word in \
                            set(stopwords.words('english'))]
            name = name.lower()
            for word in word_list:
                score = fuzz.ratio(name, word) / 100
                if score > img_score:
                    img_score = score
                    img_word = word
            
            if img_score > db_score:
                db_score = img_score
                matched_image = imgfile
                matched_word = img_word
        
        if db_score < thresh:
            print("Not found any match to DB")
            return None, None, None
        
        if plot == True:
            plt.imshow(cv2.imread(matched_image))
            plt.show()
        
        return imgfile, db_score, matched_word

if __name__ == "__main__":
    finder = Finder()
    imgfile, score, _ = finder.find_business_card('Chris', plot=True)