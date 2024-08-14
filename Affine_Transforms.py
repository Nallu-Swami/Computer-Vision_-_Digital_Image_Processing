import cv2 as cv
import numpy as np

def image_translation():
    image_1 = cv.imread("image_1.jpg", cv.IMREAD_COLOR)
    

    rows, cols, _ = image_1.shape
    
    shear_factor = 0.3
    M_shear = np.float32([[1, shear_factor, 0],
                          [0, 1, 0]])
    shear_image = cv.warpAffine(image_1, M_shear, (cols, rows))

    angle = 45
    M_rotate = cv.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    rotated_image = cv.warpAffine(image_1, M_rotate, (cols, rows))
    
    scale_factor_x = 1.2
    scale_factor_y = 1.2
    M_scale = np.float32([[scale_factor_x, 0, 0],
                          [0, scale_factor_y, 0]])
    scaled_image = cv.warpAffine(image_1, M_scale, (cols, rows))
    
    return shear_image, rotated_image, scaled_image

shear_image, rotated_image, scaled_image = image_translation()

cv.imshow("Sheared Image", shear_image)
cv.imshow("Rotated Image", rotated_image)
cv.imshow("Scaled Image", scaled_image)
cv.waitKey(0)
cv.destroyAllWindows()
