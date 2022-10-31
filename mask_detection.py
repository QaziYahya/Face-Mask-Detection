
from tensorflow.keras.models import load_model
from keras.applications.mobilenet import preprocess_input
import tensorflow as tf
import cv2
import numpy as np
import random as rnd
import os

# get the path of the model
model_path = os.path.join(os.path.dirname(__file__), 'mobilenet.h5')

# load the model
model = load_model(model_path)
# start the webcam feed
cap = cv2.VideoCapture(0)
# used to hold a single frame
frame = None

while True:
    # get the frame
	ret, frame = cap.read()
	
    # if there was no problem getting a frame then continue
	if not ret:
		continue

    # extract the squared area from the frame	
	cropped = frame[50:500, 450:850]
    # process the input
	cropped = preprocess_input(cropped)
    # resize the image 
	cropped = cv2.resize(cropped, (224,224))
    # make the input dimensions appropriate for the model
	cropped = np.expand_dims(cropped, axis=0)
	
    # get the model prediction
	p = np.argmax(model.predict(cropped)[0]) 
	
	pred = ""
	
    # if p = 0 then the model predicted that the mask is off
	if p == 0:
		pred = "Mask off"
    # if p = 1 then the model predicted that the mask is on
	else:
		pred = "Mask on"
	
    # put the square on the frame
	cv2.rectangle(frame, (450, 50), (850, 500), (0,255,0), 2)
	# put the prediction text on the frame
	cv2.putText(img = frame, text = pred, org = (450, 520), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(255,255,255))
	# show the frame
	cv2.imshow("Rock-Paper-Scissors", frame)

    # get the pressed key	
	k = cv2.waitKey(50)

    # if pressed key == 'q' then quit
	if k == ord('q'):
		break	