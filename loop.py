import imutils
import cv2
from imutils.paths import list_images
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure as ex
import imageio
import sys


for imagePath in list_images("/Users/rohanbanerjee/Documents/SukShi19/dhe"):
    img = cv2.imread(imagePath)
    print(imagePath)
    # img = cv2.resize(image, (25, 25))

    # img = cv2.imread('6.jpg')
    if(len(img.shape)==2):      #gray
        outImg = ex.equalize_hist(img[:,:])*255 
    elif(len(img.shape)==3):    #RGB
        outImg = np.zeros((img.shape[0],img.shape[1],3))
        for channel in range(img.shape[2]):
            outImg[:, :, channel] = ex.equalize_hist(img[:, :, channel])*255

    outImg[outImg>255] = 255
    outImg[outImg<0] = 0
    
    cv2.imwrite(imagePath, outImg)




