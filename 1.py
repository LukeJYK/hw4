'''
1.空域低通滤波器：分别用高斯滤波器和中值滤波器去平滑测试图像test1和2，模板大小分别是3x3 ， 5x5 ，7x7； 分析各自优缺点；
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

dir = ['C:\\Users\\lenovo\\Desktop\\4\\test1.pgm','C:\\Users\\lenovo\\Desktop\\4\\test2.tif']
for i in dir:
    img = cv2.imread(i,0)
    img_array1 = np.array(img)
    img1 = cv2.GaussianBlur(img, (3, 3), 0)
    img2= cv2.GaussianBlur(img, (5, 5), 0)
    img3 = cv2.GaussianBlur(img, (7, 7), 0)
    plt.subplot(221), plt.imshow(img, 'gray')
    plt.subplot(222), plt.imshow(img1, 'gray')
    plt.subplot(223), plt.imshow(img2, 'gray')
    plt.subplot(224), plt.imshow(img3, 'gray')
    plt.show()
#均值滤波
for i in dir:
    img = cv2.imread(i,0)
    img_array1 = np.array(img)
    def median_b(n):
        for i in range(0, 257-n):
            for j in range(0, 257-n):
                arr1 = img_array1[i:i+n,j:j+n]
                a = np.median(arr1)
                b=int((n-1)/2)
                img_array1[i+b, j+b] =a
        img1 = Image.fromarray(img_array1)
        return img1
    #img3 = median_b(7)
    plt.subplot(221), plt.imshow(img, 'gray')
    plt.subplot(222), plt.imshow(median_b(3), 'gray')
    plt.subplot(223), plt.imshow(median_b(5), 'gray')
    plt.subplot(224), plt.imshow(median_b(7), 'gray')
    plt.show()
