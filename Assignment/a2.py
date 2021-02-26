#Brain Imaging Methods | Assignment - II | Basic Image processing
#Author: Shriraj  Sawant
#Roll No: 19350006
#PhD Scholar @BRaINLab IITGN

#Import Statements
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

img = plt.imread("Brain_og.jpg") #Read image
plt.imshow(img, cmap='Greys_r') #start plotting image
plt.title("Original Brain Image with shape {}x{}".format(img.shape[0], img.shape[1])) #add title and image dimensions
plt.show() #display image on screen

plt.hist(img.ravel(),256,[0,256]) #plot histogram
plt.title("Histogram for the Original Brain Image")
plt.xlabel('Intensity [0-256]')
plt.ylabel('No. of Pixels')
plt.show() #display histogram


