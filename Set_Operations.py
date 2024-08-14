import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def union_images():
    image_1 = cv.imread("image_1.jpg", cv.IMREAD_COLOR)
    image_2 = cv.imread("image_2.jpg", cv.IMREAD_COLOR)
    if image_1.shape != image_2.shape:
        print("Images are not the same size, resizing...")
        image_2 = cv.resize(image_2, (image_1.shape[1], image_1.shape[0]))    
    
    result_add_images = cv.bitwise_or(image_1, image_2)
    
    return result_add_images

def intersection_images():
    image_1 = cv.imread("image_1.jpg", cv.IMREAD_COLOR)
    image_2 = cv.imread("image_2.jpg", cv.IMREAD_COLOR)
    
    if image_1.shape != image_2.shape:
        print("Images are not the same size, resizing...")
        image_2 = cv.resize(image_2, (image_1.shape[1], image_1.shape[0]))
        
    result_subtract_images = cv.bitwise_and(image_1, image_2)
    return result_subtract_images

def negation_images():
    image_1 = cv.imread("image_1.jpg", cv.IMREAD_COLOR)
    image_2 = cv.imread("image_2.jpg", cv.IMREAD_COLOR)
    
    if image_1.shape != image_2.shape:
        print("Images are not the same size, resizing...")
        image_2 = cv.resize(image_2, (image_1.shape[1], image_1.shape[0]))
        
    result_multiplied_images = cv.bitwise_not(image_1, image_2)
    return result_multiplied_images

def inverter_images():
    image_1 = cv.imread("image_1.jpg", cv.IMREAD_COLOR)
    image_2 = cv.imread("image_2.jpg", cv.IMREAD_COLOR)
    
    if image_1.shape != image_2.shape:
        print("Images are not the same size, resizing...")
        image_2 = cv.resize(image_2, (image_1.shape[1], image_1.shape[0]))
        
    result_divided_images = cv.bitwise_xor(image_1, image_2)
    return result_divided_images

result = negation_images()

result_rgb = cv.cvtColor(result, cv.COLOR_BGR2RGB)

plt.imshow(result_rgb)
plt.axis('off')
plt.show()