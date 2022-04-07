import os
import numpy as np
from PIL import Image

file = "F:/github/LEC_ImageProcessing/HW2_Histogram/lena_bmp_512x512_new.bmp"
imageData = np.zeros((512, 512, 3), dtype=np.uint8)
imageData[0:256, 0:256] = [255, 0, 0]
img = Image.fromarray(imageData, "RGB")
img.save(file)
img.show()