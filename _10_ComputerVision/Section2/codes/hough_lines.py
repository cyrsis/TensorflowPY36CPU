import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import (hough_line, probabilistic_hough_line)
from skimage.feature import canny
from skimage import io 
from skimage.color import rgb2gray
from skimage import draw,data
#Read an image
image = data.camera()

#Apply your favorite edge detection algorithm. We use 'canny' for this example.
edges = canny(image, 2, 1, 25)
#Once you have the edges, run the hough transform over the image
lines = hough_line(image)

probabilistic_lines = probabilistic_hough_line(edges, threshold=10, line_length=5, line_gap=3)
