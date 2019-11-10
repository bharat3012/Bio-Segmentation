import pydicom
import os
import shutil

from shutil import copyfile
fullpath = '/media/bharat/My Passport/Hitesh/BTproject/process/Pancreas/'
folders = os.listdir(fullpath)
dst = '/media/bharat/My Passport/Hitesh/BTproject/process/Image/'
for folder1 in sorted(folders):
    folderpath = fullpath +  folder1
    files = os.listdir(folderpath)
    for img in sorted(files):
        copyfile(folderpath+ "/" + img, dst +img)
        print(img)
        os.rename(dst + img, dst + folder1[-2:] + "_" + img[-7:] )