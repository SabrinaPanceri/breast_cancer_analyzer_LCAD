from PIL import Image
import cv2
from numpy import asarray
# load the image
image = Image.open('IMG_3202.JPG')
# image = cv2.imread('IMG_3202.JPG')
# from keras.preprocessing import image

<<<<<<< HEAD
X_test=image.load_img('roi.png'); #loading image and then convert it into grayscale and with it's target size 
X_test=image.img_to_array(X_test); #convert image into array
=======
# X_test=image.load_img('canvas.png'); #loading image and then convert it into grayscale and with it's target size 
# X_test=image.img_to_array(X_test); #convert image into array
>>>>>>> 675287f720702db7bdd57fda5533ca130bcf6acb
# convert image to numpy array
data = asarray(image)
# print(type(data))
# summarize shape
# print(data.shape)

# create Pillow image
# image2 = Image.fromarray(data)
# print(type(image2))

# summarize image details
# print(image2.mode)
# print(image2.size)
print (data) 
# print(X_test)

with open('data' + '.txt', 'a+') as myfile:
    myfile.write(str(X_test))
