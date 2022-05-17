"""
Madison Howard
April 12, 2022
Assignment 17
My partner is Megan Cuevas :^)
"""

import cv2
import sys
import os
import numpy as np
from math import sin,cos,pi

###################################################################
"""
(Problem 1)
In the function rot_approach1, implement ‘Approach 1’ for image rotation as described in the accompanying PDF.
This function already has code which prepares an object res for holding the resulting image.
It creates an object with the same dimensions as the original image but with all pixels preset to black.
"""
def rot_approach1(img, cx, cy, angle):
    # The most naive image rotation scheme possible.
    # Return an image representing the input image 'img'
    # rotated by 'angle' about the point (cx, cy) and truncated
    # to fit within an image of the same dimensions.
    # Get the 'shape' of the image. It will be returned as
    # height (in pixels), width (in pixels), # of channels (e.g., 3 for RGB or BGR)
    (h,w,c) = img.shape
    # Use 0 for the color, but converted to the pixel [0,0] channel 0 type.
    entry = type(img[0,0,0])(0)
    # Create an image of the same dimensions, filled with 0's in all
    # channels of all pixels:
    res = np.full((h,w,c), entry)

    # Put your code here, to compute the resulting image, 'res'.
    ## find center, multiply by matrix, copy the og color and replace new pixel with old color.
    ## if new pixel is not on "board" then ignore.
    ## center of board is 0,0 
    #center = ((h+1)/2, (w+1)/2, c)
    angle = -angle #makes it go counter-clockwise
    rot_matrix = np.array([[cos(angle), -sin(angle)],[sin(angle), cos(angle)]])
    #to find the centers....
    for i in range(h):
        for j in range(w):
        # This is the center pixel of row, i, and column, j, relative to the point of rotation
            #M = [i,j]
            center_pixel_y = i - cy + 0.5
            center_pixel_x = j - cx + 0.5
            M_center = np.array([center_pixel_x, center_pixel_y])
            #Multiply the og points by a matrix for rotation to get new point location.
            rotated_point = rot_matrix @ M_center
            res_i = int(cy+rotated_point[1])
            res_j = int(cx +rotated_point[0])
            #make sure this is the pixel thats actually the new img
            if res_i >= 0 and res_i < h and res_j>=0 and res_j<w:
                res[res_i,res_j] = img[i,j]
            #still need to assign the colors...
            # res.append(rotated_point, c) #this doesn't work
            #print(rotated_matrix)
    # Then return the result
    return res


###############################################################
def main():
    ifilename = 'patterns.jpeg'
    img = cv2.imread(ifilename)
    if img is None:
        sys.exit("Could not read the image.")
    basename,ext = os.path.splitext(ifilename)
    (h,w,c) = img.shape
    angle = float(input("Enter an angle of rotation (counter-clockwise, in radians): "))
    img_rotated = rot_approach1(img, w/2, h/2, angle)
    # The following code would save the resulting image to file:
    #filename = basename+"-app1"+ext
    #cv2.imwrite(filename, img_rotated)
    cv2.imshow("Display window", img_rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
