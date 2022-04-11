import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def createHistogram(imgArray):
    bright = np.zeros(256, np.uint16)
    for row in range(imgArray.shape[0]):
        for col in range(imgArray.shape[1]):
            curPix = imgArray[row, col]
            bright[curPix] = bright[curPix] + 1
            
    return bright

def printGraph(histogram):
    x = np.arange(256)
    plt.bar(x, histogram, width=1.0)
    plt.show()

def prefixSum(histogram):
    sum = np.zeros(255, np.uint32)
    sum[0] = histogram[0]
    for i in range(1, 255):
        sum[i] = sum[i-1] + histogram[i]
    return sum

def normalizeSum(histogram):
    # 누적합 구하기
    sum = prefixSum(histogram)
    nb_pix = sum[-1]
    norm_sum = np.zeros(255, np.uint32)
    for i in range(255):
        # 정규화된 누적 합 = (누적합 / 픽셀 수) * 최대 명도 & 반올림을 위한 +0.5
        norm_sum[i] = (sum[i] / nb_pix)*255 + 0.5 

    return norm_sum

def histogramEQ(imgArray):
    norm_sum = normalizeSum(basic_histogram)
    img_EQ = np.array(img)

    for row in range(img_EQ.shape[0]):
        for col in range(img_EQ.shape[1]):
            curBright = img_EQ[row, col]
            img_EQ[row, col] = norm_sum[curBright]
    return img_EQ

if __name__ == '__main__':
    # load image
    file = "./HW2_Histogram/lena_bmp_512x512_new.bmp"
    img = Image.open(file)
    #img.show()

    # image to numpy array
    img_np = np.array(img)

    # --------------- 1. Histogram ---------------
    basic_histogram = createHistogram(img_np)
    printGraph(basic_histogram)

    # --------------- 2. Histogram Equalization ---------------
    img_EQ = 
    EQ_histogram = createHistogram(img_EQ)
    printGraph(EQ_histogram)
    # --------------- 3. Basic Contrast Stretching ---------------