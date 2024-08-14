import cv2 as cv
import numpy as np
#Reading Images -> Resizing Images -> Image Operation -> GUI representation
def add_images():
    image_1 = cv.imread("image_1.jpg", cv.IMREAD_COLOR)
    image_2 = cv.imread("image_2.jpg", cv.IMREAD_COLOR)
    if image_1.shape != image_2.shape:
        print("Images are not the same size, resizing...")
        image_2 = cv.resize(image_2, (image_1.shape[1], image_1.shape[0]))    
    
    result_add_images = cv.add(image_1, image_2)
    
    return result_add_images


def sub_images():
    image_1 = cv.imread("image_1.jpg", cv.IMREAD_COLOR)
    image_2 = cv.imread("image_2.jpg", cv.IMREAD_COLOR)
    
    if image_1.shape != image_2.shape:
        print("Images are not the same size, resizing...")
        image_2 = cv.resize(image_2, (image_1.shape[1], image_1.shape[0]))
        
    
    result_subtract_images = cv.subtract(image_1, image_2)
    return result_subtract_images


def mul_images():
    image_1 = cv.imread("image_1.jpg", cv.IMREAD_COLOR)
    image_2 = cv.imread("image_2.jpg", cv.IMREAD_COLOR)
    
    if image_1.shape != image_2.shape:
        print("Images are not the same size, resizing...")
        image_2 = cv.resize(image_2, (image_1.shape[1], image_1.shape[0]))
        
    
    result_multiplied_images = cv.multiply(image_1, image_2)
    return result_multiplied_images

def div_images():
    image_1 = cv.imread("image_1.jpg", cv.IMREAD_COLOR)
    image_2 = cv.imread("image_2.jpg", cv.IMREAD_COLOR)
    
    if image_1.shape != image_2.shape:
        print("Images are not the same size, resizing...")
        image_2 = cv.resize(image_2, (image_1.shape[1], image_1.shape[0]))
        
    result_divided_images = cv.divide(image_1, image_2)
    return result_divided_images




cv.imshow("Result of Arithmetic Addition",mul_images())
cv.waitKey(0)
cv.destroyAllWindows()
