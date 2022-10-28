import os
import json
import glob
from .reader import Data_Reader
from .params import dbfile

def _write_json(dict_to_save, savefolder):
    json_object = json.dumps(dict_to_save, indent=4)
    with open(savefolder, "w") as f:
        f.write(json_object)
    
def read_json(filepath):
    with open(filepath) as f:
        db_data = json.load(f)
    return db_data

def upload_file_to_db(filename):
    db_size = 0
    db_data = {}
    if os.path.exists(dbfile):
        db_data = read_json(dbfile)
        db_size = len(db_data)
    card_data_reader = Data_Reader()
    card_data_reader.upload_file(filename)
    temp_data = card_data_reader.output
    db_data[db_size+1] = temp_data
    _write_json(db_data, dbfile)

def upload_folder_to_db(folder):
    imgfiles = glob.glob(os.path.join(folder, '*.jpg'))
    db_size = 0
    db_data = {}
    if os.path.exists(dbfile):
        db_data = read_json(dbfile)
        db_size = len(db_data)
    card_data_reader = Data_Reader()
    for imgfile in imgfiles:
        db_size += 1
        card_data_reader.upload_file(imgfile)
        temp_data = card_data_reader.output
        db_data[db_size] = temp_data
    _write_json(db_data, dbfile)

if __name__ == '__main__':
    folder = '../images/'
    imgfiles = glob.glob(os.path.join(folder, '*.jpg'))
    print("Number of files : ", len(imgfiles))
    upload_folder_to_db(folder)
    upload_file_to_db(imgfiles[0])
