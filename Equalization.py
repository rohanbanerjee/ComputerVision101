import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('WeedCont.tif', 0)
equalizedImg = cv2.equalizeHist(img)

plt.title('equalized')
plt.imshow(equalizedImg)
plt.xticks([])
plt.yticks([])
plt.show()
