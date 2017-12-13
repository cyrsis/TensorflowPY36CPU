from skimage import morphology
from skimage import io 

img = io.imread('image.png')
eroded_img  = morphology.erosion(img)

io.imshow(eroded_img)
io.show()
