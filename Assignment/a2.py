"""
Brain Imaging Methods | Assignment - II | Basic Image processing and Gaussian Smoothening

@Author: Shriraj  Sawant
@Roll_No: 19350006
@PhD_Scholar 
@BRaINLab_IITGN

"""

#Import Statements
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

img = plt.imread("Brain_og.jpg") #Read image
print("Shape of the image is: ")
print(img.shape) #show image dimensions
plt.imshow(img, cmap='Greys_r') #start plotting image
plt.title("Original Brain Image with shape {}x{}".format(img.shape[0], img.shape[1])) #add title and image dimensions
plt.show() #display image on screen

plt.hist(img.ravel(),256,[0,256]) #plot histogram
plt.title("Histogram for the Original Brain Image")
plt.xlabel('Intensity [0-256] | Bins = 256')
plt.ylabel('No. of Pixels')
plt.show() #display histogram

plt.hist(img.ravel(),10,[0,256]) #plot histogram
plt.title("Histogram for the Original Brain Image")
plt.xlabel('Intensity [0-256] | Bins = 10')
plt.ylabel('No. of Pixels')
plt.show() #display histogram

#Gaussian Smoothening
sigmas=[5, 10, 20, 30, 40, 50] #levels of gaussian smoothening

for sigma in sigmas:
  smooth_img = ndimage.gaussian_filter(img, sigma) #applied gaussian smoothening with corresponding sigma
  
  plt.imshow(smooth_img, cmap='Greys_r') #start plotting image
  plt.title("Smoothened Brain Image with shape {}x{} & sigma = {}".format(smooth_img.shape[0], smooth_img.shape[1], sigma)) #add title and image dimensions
  plt.show() #display image on screen

  plt.hist(smooth_img.ravel(),256,[0,256]) #plot histogram
  plt.title("Histogram for the Smoothened Brain Image")
  plt.xlabel('Intensity [0-256] | Bins = 256 | Sigma = {}'.format(sigma))
  plt.ylabel('No. of Pixels')
  plt.show() #display histogram

  plt.hist(smooth_img.ravel(),10,[0,256]) #plot histogram
  plt.title("Histogram for the Smoothened Brain Image")
  plt.xlabel('Intensity [0-256] | Bins = 10 | Sigma = {}'.format(sigma))
  plt.ylabel('No. of Pixels')
  plt.show() #display histogram
  
print("Program ran successfully!")




