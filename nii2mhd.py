import numpy as np

from glob import glob
import os
import os.path
import SimpleITK as sitk
import pandas as pd

from skimage import transform, img_as_bool
final_path = "/media/bharat/My Passport/Hitesh/BTproject/process2/Attention-Gated-Networks/dataio/images/"
file_list=glob(final_path+"*.nii")
#print("Don:",file_list)
new_path= "/media/bharat/My Passport/Hitesh/BTproject/process2/Attention-Gated-Networks/dataio/new_images/"

for img_list in sorted(file_list):
    #img_list = file_list[i]

    itk_img = sitk.ReadImage(img_list)
    img_array = sitk.GetArrayFromImage(itk_img)
    print(img_list[-8:-4])

    path = new_path + img_list[-8:-4]+ "_training.mhd"

    itk_nimg= sitk.GetImageFromArray(img_array, isVector=False)
    print(path)

    sitk.WriteImage(itk_nimg, path)