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

def showImg(imgArray):
    image = Image.fromarray(imgArray)
    image.show()

def prefixSum(histogram):
    sum = np.zeros(255, np.uint32)
    sum[0] = histogram[0]
    for i in range(1, 255):
        sum[i] = sum[i-1] + histogram[i]
    return sum

def createLUT(histogram):
    # 누적합 구하기
    sum = prefixSum(histogram)
    nb_pix = sum[-1]
    lut = np.zeros(255, np.uint32)
    for i in range(255):
        # 정규화된 누적 합 = (누적합 / 픽셀 수) * 최대 명도 & 반올림을 위한 +0.5 = LUT
        lut[i] = (sum[i] / nb_pix)*255 + 0.5 

    return lut

def createEQ(imgArray):
    image_EQ = imgArray.copy()
    basic_histogram = createHistogram(image_EQ)
    lut = createLUT(basic_histogram)

    for row in range(image_EQ.shape[0]):
        for col in range(image_EQ.shape[1]):
            curBright = image_EQ[row, col]
            image_EQ[row, col] = lut[curBright]

    return image_EQ

def createBasicContrastStretching(imgArray):
    image_Stretching = imgArray.copy()
    low = np.min(image_Stretching)
    high = np.max(image_Stretching)
    mult = 255 / (high - low)
    for row in range(image_Stretching.shape[0]):
        for col in range(image_Stretching.shape[1]):
            image_Stretching[row, col] = (image_Stretching[row, col] - low) * mult
    
    return image_Stretching

def createEndsIn(imgArray):
    image_EndsIn = imgArray.copy()
    low = 40
    high = 190
    mult = 255 / (high - low)
    for row in range(image_EndsIn.shape[0]):
        for col in range(image_EndsIn.shape[1]):
            x = image_EndsIn[row, col]
            if x<low:
                image_EndsIn[row, col] = 0
            elif x>high:
                image_EndsIn[row, col] = 255
            else:  
                image_EndsIn[row, col] = (image_EndsIn[row, col] - low) * mult
    return image_EndsIn



if __name__ == '__main__':
    # load image
    file = "./HW2_Histogram/lena_bmp_512x512_new.bmp"
    img = Image.open(file)
    #img.show()

    # image to numpy array
    img_np = np.array(img)

    # --------------- 1. Histogram ---------------
    basic_histogram = createHistogram(img_np)

    # --------------- 2. Histogram Equalization ---------------
    img_EQ = createEQ(img_np)
    EQ_histogram = createHistogram(img_EQ)

    # --------------- 3. Basic Contrast Stretching ---------------
    img_ContrastStretching = createBasicContrastStretching(img_np)
    contrast_histogram = createHistogram(img_ContrastStretching)

    # --------------- 4. Ends-in Contrast Stretching ---------------
    img_EndsIn = createEndsIn(img_np)
    endsIn_histogram = createHistogram(img_EndsIn)
    # showImg(img_np)
    # showImg(img_EQ)
    # showImg(img_ContrastStretching)
    # showImg(img_EndsIn)
    printGraph(basic_histogram)
    printGraph(EQ_histogram)
    printGraph(contrast_histogram)
    printGraph(endsIn_histogram)
