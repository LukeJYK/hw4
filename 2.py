import math
import cv2
import numpy as np
from PIL import Image
def guassi(ksize,array):
    sigma = 1.5
    pi = 3.1415926
    center = ksize / 2
    for i in range(0,ksize):
        x2 = pow(i - center, 2)
        for j in range(0,ksize):
            y2 = pow(j - center, 2)
            g = math.exp(-(x2 + y2) / (2 * sigma * sigma))
            g /= 2 * pi * sigma
            array[i,j] = g
    return array
img = cv2.imread('C:\\Users\\lenovo\\Desktop\\4\\test1.pgm',0)
img_array1 = np.array(img)
array11=guassi(4,img_array1)
img2 = Image.fromarray(array11)
img2.show()