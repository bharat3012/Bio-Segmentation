import pydicom as dicom
import os
import cv2
import PIL # optional
# make it True if you want in PNG format
PNG = False
# Specify the .dcm folder path
folder_path = "/media/bharat/My Passport/Hitesh/BTproject/process/Image"
# Specify the output jpg/png folder path
jpg_folder_path = "/media/bharat/My Passport/Hitesh/BTproject/process/CTimage"
images_path = os.listdir(folder_path)
for n, image in enumerate(sorted(images_path)):
    print(os.path.join(folder_path, image))
    ds = dicom.dcmread(os.path.join(folder_path, image), force=True)
    ds.file_meta.TransferSyntaxUID = dicom.uid.ImplicitVRLittleEndian
    pixel_array_numpy = ds.pixel_array
    print(pixel_array_numpy.shape)
    if PNG == False:
        image = image.replace('.dcm', '_training.jpg')
    else:
        image = image.replace('.dcm', '.png')
    pixel_array_numpy2 = cv2.flip(pixel_array_numpy, 0)
    #print(os.path.join(jpg_folder_path, image))
    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy2)
    if n % 50 == 0:
        print('{} image converted'.format(n))