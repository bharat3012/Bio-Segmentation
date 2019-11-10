import numpy as np
import pydicom as dicom
import os
import shutil
import png
import SimpleITK as sitk
from shutil import copy2

N = 82
W = 512
H = 512
path1 = '/media/bharat/My Passport/Hitesh/BTproject/process/Pancreas-CT'
path2 = '/media/bharat/My Passport/Hitesh/BTproject/process/Pancreas'
def save_image(img_arr, path):
    itk_img = sitk.GetImageFromArray(img_arr, isVector=False)
    sitk.WriteImage(itk_img, path)

if not os.path.exists(path2):
    os.makedirs(path2)

for n in range(N):
    volumeID = '{:0>4}'.format(n + 1) #(1 to 82)
    print ('Processing File ' + volumeID)
    filename1 = 'PANCREAS_' + volumeID #(1 to 82 folders)
    directory1 = os.path.join(path1, filename1)

    filename2 = volumeID
    print(directory1)
    k_walk = os.walk(directory1) # Directory 1 to 82 

    for path_, _, file_ in k_walk:

        L = len(file_) #No. of files in folders
        if L > 0:

            data = np.zeros((W, H, L), dtype = np.int16) # Initialize
            for f in sorted(file_): # Sort them
                file1 = os.path.abspath(os.path.join(path_, f)) # Abslute
                
                image = dicom.read_file(file1)
                sliceID = image.data_element("InstanceNumber").value - 1
                print(file1, sliceID)
                newpath = os.path.join(path2 + "/Image_" + volumeID)
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                
                if sliceID<=9:
)
                    copy2(file1, newpath +"/"+ "00" + str(sliceID)+ ".dcm")
                elif 99>=sliceID>=10:

                    copy2(file1, newpath +"/"+ "0" + str(sliceID)+ ".dcm")
                else:

                    copy2(file1, newpath +"/"+ str(sliceID)+ ".dcm")
