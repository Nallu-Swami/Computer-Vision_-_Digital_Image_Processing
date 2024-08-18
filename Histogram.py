#Histogram Equalization -> needed to get better contrast in images
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not loaded. Check the file path.")
else:
    equalized_image = cv2.equalizeHist(image)
    plt.figure(figsize=(10, 5))

    # Original Image
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    # Equalized Image
    plt.subplot(1, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Image')
    plt.axis('off')

    # Show the plots
    plt.show()
