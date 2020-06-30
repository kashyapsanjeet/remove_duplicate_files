import hashlib
from scipy.misc import imread,imresize,imshow
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import time
import numpy as np
import os
import csv

path_to_image_directory = 'C:/Users/kashy/Desktop/duplicate/images'  #add path

file_list = os.listdir(path_to_image_directory)
print(len(file_list))

duplicates = []
hash_keys = dict()


for index, filename in enumerate(os.listdir(path_to_image_directory)):
    filen = path_to_image_directory+ '/' + filename
    if os.path.isfile(filen):
        with open(filen , 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
            #print(filehash)
        if filehash not in hash_keys:
            hash_keys[filehash] = index
        else:
            duplicates.append((index,hash_keys[filehash],filehash))

#print(duplicates)


with open('fie_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Filename", "FileHash"])
    for index in duplicates:
		path = path_to_image_directory + file_list[index[0]]
        writer = csv.writer(file)
        writer.writerow([file_list[index[0]], index[2]])
        os.remove(path)
        

