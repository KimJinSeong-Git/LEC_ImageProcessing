import os
import numpy as np
from PIL import Image

# load image
file = "F:/github/LEC_ImageProcessing/HW2_Histogram/lena_bmp_512x512_new.bmp"
img = Image.open(file)
#img.show()

# image to numpy array
img_np = np.array(img)

# count bright
bright = np.zeros(255, np.uint16)
count = 0
for row in range(img_np.shape[0]):
    for col in range(img_np.shape[1]):
        curPix = img_np[row, col]
        bright[curPix] = bright[curPix] + 1
        count = count + 1

print(bright.sum())
print(img_np.size)
