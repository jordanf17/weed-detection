import cv2
import numpy as np

#read image
src = cv2.imread('C:/Users/Jordan Furtado/Documents/7_sem/ImageProcessing-CollegeWork-main/proj/lawn.jpg', cv2.IMREAD_UNCHANGED)
print(src.shape)

# extract red channel
red_channel = src[:,:,2]
green_channel = src[:,:,1]

# create empty image with same shape as that of src image
red_img = np.zeros(src.shape)

def soil(red_img):
    # Obtain dimension of an image array
    row,col = red_img.shape[0:2]
    
    # loops through pixel array 
    for i in range(row):
        for j in range(col):
            if(green_channel[i,j]>red_channel[i,j]):
                red_img[i,j]=green_channel[i,j]
            else:
                red_img[i,j]=0
               

soil(red_img)
#assign the red channel of src to empty image

#save image
cv2.imwrite('C:/Users/Jordan Furtado/Documents/7_sem/ImageProcessing-CollegeWork-main/proj/cv2-soil-channel.png',red_img) 