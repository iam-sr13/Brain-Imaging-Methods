#Brain Imaging Methods | Assignment - II | Basic Image processing
#Author: Shriraj  Sawant
#Roll No: 19350006
#PhD Scholar @BRaINLab IITGN

#Import Statements
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

img = plt.imread("Brain_og.jpg") #Read image
plt.imshow(img) #start plotting image
plt.title("Original Brain Image with shape {}x{}".format(img.shape)) #add title and image dimensions
plt.show() #display image on screen


