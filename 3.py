import cv2
"""
利用高通滤波器滤波测试图像test3,4：
包括unsharp masking, Sobel edge detector, and Laplace edge detection；Canny algorithm.分析各自优缺点；
"""
from PIL import Image
from PIL import ImageFilter
import cv2
import numpy as np
import argparse
img=Image.open('C:\\Users\\lenovo\\Desktop\\4\\test4 copy.bmp')
img_array = np.array(img)
"""
反锐化掩模

overimg = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
overimg.show()
"""
x = cv2.Sobel(img_array, cv2.CV_16S,1, 0)
y = cv2.Sobel(img_array, cv2.CV_16S, 0, 1)
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
cv2.imshow("Result", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
sobel算子

'''



"""
拉普拉斯变化
# if don't use a floating point data type when computing
# the gradient magnitude image, you will miss edges
lap = cv2.Laplacian(img_array, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

# display two images in a figure
cv2.imshow("Edge detection by Laplacaian", np.hstack([lap, img_array]))

cv2.imwrite("1_edge_by_laplacian.jpg", np.hstack([img_array, lap]))

if (cv2.waitKey(0) == 27):
    cv2.destroyAllWindows()
"""

# 30 and 150 is the threshold, larger than 150 is considered as edge,
# less than 30 is considered as not edge


'''
canny = cv2.Canny(img_array, 30, 150)

canny = np.uint8(np.absolute(canny))
# display two images in a figure
cv2.imshow("Edge detection by Canny", np.hstack([img_array, canny]))
cv2.imwrite("1_edge_by_canny.jpg", np.hstack([img_array, canny]))
if (cv2.waitKey(0) == 27):
    cv2.destroyAllWindows()
'''
