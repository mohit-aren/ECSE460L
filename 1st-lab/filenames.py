# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 00:49:03 2020

@author: mohit123
"""

import os

from shutil import copyfile
import scipy.misc
import matplotlib

folder_path = "PE_masks"
src_path = "OneDrive_1_1-3-2022/(1) GT Mask-Gian/(1) GT Mask-Gian"
dest_path = "PE_GT"
#folder_path1 = "C:/Mohit/2020/Oct20/COVID/COVID/COVID50/(1) JPG"
# Specify the output jpg/png folder path

images_path = os.listdir(folder_path)
index = 0


jpg_files = []
dest_files = []

for n, image in enumerate(images_path):
    print(image)
    if(image.find('png') == -1):
        continue
    src = os.path.join(src_path, image)
    dest = os.path.join(dest_path, image)
    jpg_files.append(image)
    copyfile(src, dest)

print(len(jpg_files))