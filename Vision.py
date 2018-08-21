#victor 
#17/03/2018 
#Created @ 2018-03-17 09:29 

import numpy as np
from keras.preprocessing import image
from keras.applications import resnet50

# Pillow=4.0.0
PATH = "swimming.jpg"

model = resnet50.ResNet50()

model = resnet50.ResNet50()  # Load Keras' ResNet50 model ImageNet database

img = image.load_img(PATH, target_size=(224, 224))  # Eesiz 224x224 pixels (required by this model)

x = image.img_to_array(img)  # Convert the image to a numpy array

img = image.load_img("%s" % PATH, target_size=(224, 224))  # Resize it to 224x224 pixels (required)

x = image.img_to_array(img)  # to numpy array

x = np.expand_dims(x, axis=0)  # Add a forth dimension since Keras expects a list of images

x = resnet50.preprocess_input(x)  # Input

predictions = model.predict(x)  # predict

predicted_classes = resnet50.decode_predictions(predictions, top=9)  # Look up the result. Index top9

print("This is an image of:")

for imagenet_id, name, likelihood in predicted_classes[0]:
    print(" - {}: {:2f} likelihood".format(name, likelihood))
