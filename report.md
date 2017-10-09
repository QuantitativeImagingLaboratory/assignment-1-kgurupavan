1) Interpolation:
* Interpolation is a process where we calculate unknown values using the known data. Using the interpolation process, we can increase/decrease the number of pixels in an image.

a)Nearest Neighbor interpolation:
* Initially, the no of rows and columns of the source image are captured. Based on the given scaling factors(fx,fy), scaling ratio is calculated as follows:
  X_scale= (fx * row)/ (row -1)
  Y_scale= (fy * col)/ (col-1)
* Now, a new image is initialized with zero pixels of resulting rows and columns.
* By recursively looping through new image, the new pixel values are calculated and rounding off the scaled index values based on x_scale and y_scale values. 

 Observation:
* Using nearest neighbor interpolation algorithm, the resulting image pixels contains noise but the calculation of pixels is fast compared to bilinear interpolation.


b)Bilinear Interpolation:
* Initially, the no of rows and columns of the source image are captured. Based on the given scaling factors(fx,fy), scaling ratio is calculated as follows:
  X_scale= (fx * row)/ (row -1)
  Y_scale= (fy * col)/ (col-1)
* Now, a new image is initialized with zero pixels of resulting rows and columns.
* By recursively looping through new image, the new pixel values are calculated based on averaging the four nearest neighbors calculated to the new point selected.






2) Region Counting:

a) Initially, each pixel count is calculated and stored in the hist[] list.
To find the optimal threshold, initialize the threshold value by half of the count of pixels in the image.
* Initialize the t=k/2
* Calculate the expected value of x i.e E(X) for all x < t – exp1
* Calculate the expected value of x i.e E(X) for all x > t – exp2
* Calculate the average of exp1 & exp2 and mark it as new threshold.
* Calculate the difference of previous threshold and new threshold.
* Repeat the loop assigning the calculated threshold value to t until the difference is less than 1.

b) After calculating the threshold value, copy the image into a binary image.
* Now based on the threshold value, assign 0 or 255. If the pixel intensity is greater than threshold value, assign 255 otherwise assign with 0.
* Binary image is created.

c) Blob coloring:
* The no of regions in an image are calculated based on the binary coloring.
* Consider three cells, current, top and left.
* If only current pixel, assign a region.
* If only current and top pixel, assign a region for both.
* If only current and left pixel, assign a region for both.
* If current, top and left pixel, assign a region. Also check, if top!=left, assign same value.
* Based on this, regions are identified in an image.

d) Stats and region counting
* The pixels, and region number are stored in region data structure.
* Now from the regions data, we can calculate the pixel count and store it under attribute named area. 
* Centroids can be calculated from the respective pixels of region.


