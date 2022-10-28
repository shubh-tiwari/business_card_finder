import os
import glob
from business_card_finder import upload_file_to_db, upload_folder_to_db

folder = 'images/'
imgfiles = glob.glob(os.path.join(folder, '*.jpg'))
print("Number of files : ", len(imgfiles))
upload_folder_to_db(folder)
upload_file_to_db(imgfiles[0])