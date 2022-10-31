from tensorflow.keras.models import load_model
from keras.applications.mobilenet import preprocess_input
import tensorflow as tf
import cv2
import numpy as np
import random as rnd

model = load_model("mobilenet.h5")
cap = cv2.VideoCapture(0)
frame = None

#tf.random.set_seed(1234)

while True:
	ret, frame = cap.read()
	
	if not ret:
		continue
		
	cropped = frame[50:500, 450:850]
	cropped = preprocess_input(cropped)
	cropped = cv2.resize(cropped, (224,224))
	cropped = np.expand_dims(cropped, axis=0)
	
	p = np.argmax(model.predict(cropped)[0]) 
	
	pred = ""
	
	if p == 0:
		pred = "Mask off"
	else:
		pred = "Mask on"
	
	cv2.rectangle(frame, (450, 50), (850, 500), (0,255,0), 2)
	
	cv2.putText(img = frame, text = pred, org = (450, 520), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(255,255,255))
	
	cv2.imshow("Rock-Paper-Scissors", frame)
		
	k = cv2.waitKey(50)

	if k == ord('q'):
		break	
