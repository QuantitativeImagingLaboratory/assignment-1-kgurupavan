import numpy as np

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256
        row = image.shape[0]
        col = image.shape[1]
        for i in range(0,row):
            for j in range(0,col):
                hist[(image[i,j])] = hist[(image[i,j])] + 1

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""
        exp1=0
        exp2=0
        total_count1=0
        total_count2=0
        t= round((len(hist)-1)/2)

        diff=len(hist)-1
        while True:

                for i in range(0, t):
                    total_count1 = total_count1 + hist[i]
                for i in range(0, t):
                    exp1 = exp1 + (i * (hist[i] / total_count1))
                for i in range(t, len(hist)):
                    total_count2 = total_count2 + hist[i]

                for i in range(t, len(hist)):
                    exp2 = exp2 + (i * (hist[i] / total_count2))

                new_t = (((exp1 + exp2) / 2))
                diff= new_t - t
                t=int(new_t)
                if diff > 1:
                    break



        threshold = new_t

        return threshold

    def binarize(self, image,threshold):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()
        for i in range(0,bin_img.shape[0]):
            for j in range(0,bin_img.shape[1]):
                if bin_img[i,j] > threshold:
                     bin_img[i,j]=0
                else:
                     bin_img[i,j]=255

        return bin_img


