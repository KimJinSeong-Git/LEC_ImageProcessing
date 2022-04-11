import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# load image
file = "./HW2_Histogram/lena_bmp_512x512_new.bmp"
img = Image.open(file)
img.show()

# image to numpy array
img_np = np.array(img)

# count bright
bright = np.zeros(255, np.uint16)
for row in range(img_np.shape[0]):
    for col in range(img_np.shape[1]):
        curPix = img_np[row, col]
        bright[curPix] = bright[curPix] + 1

# print graph
x = np.arange(255)
#plt.bar(x, bright, width=1.0)
#plt.show()

# Histogram Equalization
# - 누적합
sum = np.zeros(255, np.uint32)
sum[0] = bright[0]
for i in range(1, 255):
    sum[i] = sum[i-1] + bright[i]

# - 정규화된 누적합
nb_pix = sum[-1]
norm_sum = np.zeros(255, np.uint32)
for i in range(255):
    norm_sum[i] = (sum[i] / nb_pix)*255 + 0.5 # 정규화된 누적 합 = (누적합 / 픽셀 수) * 최대 명도 & 반올림을 위한 +0.5

img_Eq = np.array(img)
for row in range(img_Eq.shape[0]):
    for col in range(img_Eq.shape[1]):
        curBright = img_Eq[row, col]
        img_Eq[row, col] = norm_sum[curBright]

im = Image.fromarray(img_Eq)
im.show()
#plt.bar(x, bright, width=1.0)
#plt.show()
