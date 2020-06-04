# Open an image with matplotlib

import numpy as np 
import matplotlib.pyplot as plt 

from PIL import Image

img = Image.open('C:/Users/Admin/Desktop/pic.jpg')
img

# rotate the image
img.rotate(-90)

# Check the type of image
type(img)

# turn the image into an array
img_array = np.asarray(img)

# Get the Height, Width & Channels
img_array.shape

plt.imshow(img_array)

# RGB Colors
img_test = img_array.copy()

# only red color
plt.imshow(img_test[:, :, 0])

# Scale red channel to gray
plt.imshow(img_test[:, :, 0], cmap= 'gray')

# only green color
plt.imshow(img_test[:, :, 1])

# Scale green channel to gray
plt.imshow(img_test[:, :, 1], cmap= 'gray')

# only blue color
plt.imshow(img_test[:, :, 2])

# Scale blue channel to gray
plt.imshow(img_test[:, :, 2], cmap= 'gray')

# Remove Red Color
img_test[:, :, 0] = 0

plt.imshow(img_test)

# Remove Green Color
img_test[:, :, 1] = 0

plt.imshow(img_test)

# Remove Blue Color
img_test[:, :, 2] = 0

plt.imshow(img_test)