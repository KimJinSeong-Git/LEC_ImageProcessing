import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def createHistogram(imgArray):
    bright = np.zeros(255, np.uint16)
    for row in range(img_np.shape[0]):
        for col in range(img_np.shape[1]):
            curPix = img_np[row, col]
            bright[curPix] = bright[curPix] + 1
            
    return bright


# load image
file = "./HW2_Histogram/lena_bmp_512x512_new.bmp"
img = Image.open(file)
img.show()

# image to numpy array
img_np = np.array(img)

# --------------- 1. count bright ---------------
basic_histogram = createHistogram(img_np)

# print graph
x = np.arange(255)
plt.bar(x, basic_histogram, width=1.0)
plt.show()

# --------------- 2. Histogram Equalization ---------------
# - 누적합
sum = np.zeros(255, np.uint32)
sum[0] = basic_histogram[0]
for i in range(1, 255):
    sum[i] = sum[i-1] + basic_histogram[i]

# - 정규화된 누적합
nb_pix = sum[-1]
norm_sum = np.zeros(255, np.uint32)
for i in range(255):
    norm_sum[i] = (sum[i] / nb_pix)*255 + 0.5 # 정규화된 누적 합 = (누적합 / 픽셀 수) * 최대 명도 & 반올림을 위한 +0.5

# - 평활화 결과
img_Eq = np.array(img)
for row in range(img_Eq.shape[0]):
    for col in range(img_Eq.shape[1]):
        curBright = img_Eq[row, col]
        img_Eq[row, col] = norm_sum[curBright]

im = Image.fromarray(img_Eq)
im.show()
#plt.bar(x, bright, width=1.0)
#plt.show()

# --------------- 3. Basic Contrast Stretching ---------------




















