import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# load image
file = "./HW2_Histogram/lena_bmp_512x512_new.bmp"
img = Image.open(file)
#img.show()

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
plt.bar(x, bright, width=1.0)
plt.show()

# Histogram Equalization
# - 누적합
sum = np.zeros(255, np.uint32)
sum[0] = bright[0]
for pixBright in range(1, 255):
    sum[pixBright] = sum[pixBright-1] + bright[pixBright]

print(sum)