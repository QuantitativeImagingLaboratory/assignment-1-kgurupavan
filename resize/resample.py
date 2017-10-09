import numpy as np
import math as m
class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here

        row = image.shape[0]
        col = image.shape[1]
        fx = float(fx)
        fy = float(fy)
        x_new = int(fx*row)
        y_new = int(fy*col)
        output_image = np.zeros(shape=(x_new,y_new))
        x_ratio = x_new/(row-1)
        y_ratio = y_new/(col-1)
        for i in range(0, (x_new - 1)):
            for k in range(0, (y_new - 1)):
                output_image[i+1,k+1] = image[1 + round(i / x_ratio), 1 + round(k / y_ratio)]

        image=output_image

        return image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        row = image.shape[0]
        col = image.shape[1]
        fx = float(fx)
        fy = float(fy)
        x_new = int(fx * row)
        y_new = int(fy * col)
        output_image = np.zeros(shape=(x_new, y_new))
        x_ratio = x_new / (row - 1)
        y_ratio = y_new / (col - 1)
        #x_ratio=int(x_ratio)
        #y_ratio=int(y_ratio)
        for i in range(0, (x_new - 1)):
            for k in range(0, (y_new - 1)):
                if((1+int((i/x_ratio)))<int(row) and (1+int((k/y_ratio)))<int(col)):
                    width = -(((i / x_ratio) - m.floor(i / x_ratio)) - 1)
                    height = -(((k / y_ratio) - m.floor(k / y_ratio)) - 1)
                    I11 = image[1 + m.floor(i / x_ratio), 1 + m.floor(k / y_ratio)]
                    I12 = image[1 + m.floor(i / x_ratio), 1 + m.floor(k / y_ratio)]
                    I21 = image[1 + m.floor(i / x_ratio), 1 + m.floor(k / y_ratio)]
                    I22 = image[1 + m.floor(i / x_ratio), 1 + m.floor(k / y_ratio)]
                    output_image[i + 1, k + 1] = (1 - width) * (1 - height)* I22 + (width) * (1 - height) * I21 + (1 - width) * (
                     height) * I12 + (width) * (height) * I11
        image=output_image

        return image

