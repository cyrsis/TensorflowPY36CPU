from sklearn import datasets, metrics
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from skimage import io, color, feature, transform

mnist = datasets.fetch_mldata('MNIST Original')

img_tuple = list(zip(mnist.data, mnist.target))

images = mnist.data

data_size = len(images)

#Preprocessing images
images = images.reshape(len(images), -1)
labels = mnist.target

#Initialize Logistic Regression
LR_classifier = LogisticRegression(C=50., penalty='l2', multi_class='multinomial', solver='sag', tol=0.01)
#Training the data on only 75% of the dataset. Rest of the 25% will be used in testing the Logistic Regression
#LR_classifier.fit(images[:int((data_size / 4) * 3)], labels[:int((data_size / 4) * 3)])
LR_classifier.fit(images, labels)

#Load a custom image 
digit_img = io.imread('digit.png')
#Convert image to grayscale
digit_img = color.rgb2gray(digit_img)

#Resize the image to 28x28
digit_img = transform.resize(digit_img, (28, 28), mode="wrap")

#Run edge detection on the image 
digit_edge = feature.canny(digit_img, sigma=5) 

io.imshow(digit_edge)
io.show()

digit_edge = digit_edge.flatten()

#Testing the data
predictions = LR_classifier.predict(digit_img.flatten())

print(predictions)
