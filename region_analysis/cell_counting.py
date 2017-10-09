import numpy as np
import cv2 as cv2
class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""
        row = image.shape[0]
        col = image.shape[1]
        print(row,col)
        R= np.zeros(shape=(row,col))
        k=1
        list=[]
        for i in range(1,row):
            for j in range(1,col):
                if image[i, j] == 0 and image[i, j-1] == 255 and image[i-1, j] == 255:
                    R[i, j] = k
                    k = k + 1;
                if image[i, j] == 0 and image[i, j-1] == 255 and image[i-1, j] == 0:
                    R[i, j] = R[i - 1, j]
                if image[i, j] == 0 and image[i, j-1] == 0 and image[i-1, j] == 255:
                    R[i, j] = R[i, j - 1]
                if image[i, j] == 0 and image[i, j-1] == 0 and image[i-1, j] == 0:
                    R[i, j] = R[i - 1, j]
                    if R[i, j - 1] != R[i-1, j]:
                        R[i,j-1]=R[i-1,j]


        regions = dict()

        for i in range(0, R.shape[0]):
            for j in range(0, R.shape[1]):
                if R[i,j] in regions.keys():
                    regions[R[i,j]].append([i,j])
                else:
                    regions[R[i,j]]=[[i,j]]

        return regions


    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        stats=dict()
        for key,value in region.items():
            x_centroid=0
            y_centroid=0

            for i in range(0,len(value)):
                x_centroid=x_centroid+value[i][0]
                y_centroid=y_centroid+value[i][1]
            x_centroid=round(x_centroid/len(value))
            y_centroid=round(y_centroid/len(value))
            mark=round(len(value)/2)
            centroid=[x_centroid,y_centroid]
            if(len(value)>=15):
                stats[key] =[value[mark],centroid,len(value)]
        print(len(stats))
       # for key,value in stats.items():
        #    print("Region:",key,"Area:",value[2],"Centroid:",value[1])

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return stats

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        for key,value in stats.items():
            msg=str(value[1][0])+","+str(value[1][1])
            pixel=(value[1][0],value[1][1])
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image,"*",pixel, font, 0.2, (121,0,0))

        return image

