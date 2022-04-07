import os
import numpy as np
from PIL import Image

# load image
file = "F:/github/LEC_ImageProcessing/HW2_Histogram/lena_bmp_512x512_new.bmp"
img = Image.open(file)
#img.show()

# image to numpy array
img_np = np.array(img)
print(img_np.shape)