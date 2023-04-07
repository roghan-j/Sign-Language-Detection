import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time

import pyttsx3
from gtts import gTTS
from matplotlib import pyplot as plt

import mediapipe as mp

mp_holistic = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results

def draw_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS) # Draw pose connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Draw right hand connections

def draw_styled_landmarks(image, results):

    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                             ) 
    # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                             ) 
    # Draw right hand connections  
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                             )

cap= cv2.VideoCapture(0)
classifier= Classifier("model/model-1/keras_model.h5", "model/model-1/labels.txt")
# classifier= Classifier("model/model-2/keras_model.h5", "model/model-2/labels.txt")
# classifier= Classifier("model/model-3/keras_model.h5", "model/model-3/labels.txt")
# classifier= Classifier("model/model-4/keras_model.h5", "model/model-4/labels.txt")
# classifier= Classifier("model/model-5/keras_model.h5", "model/model-5/labels.txt")

labels= ["fishing", "I", "love", "favourite", "hobby", "my", "you", "feel", "family", "bad", "sorry"]
# labels= ["I love you", "heart", "my", "home", "I", "live", "inside", "beautiful"]
# labels= ["clean", "home", "help", "thank you", "arrive", "learn", "start"]
# labels= ["love", "go", "with", "you", "good", "day", "I", "think", "happen"]
# labels= ["hello", "need", "talk", "about", "health", "feel", "sick", "cold", "my", "have"]

# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    t2s= pyttsx3.init()
    sentence= []

    while cap.isOpened():

        # Read feed
        ret, frame = cap.read()

        # Make detections
        image, results = mediapipe_detection(frame, holistic)
        
        # Show to screen
        cv2.imshow('OpenCV Feed', image)

        key= cv2.waitKey(1)

        prediction, index= classifier.getPrediction(image, draw=False)
        
        # print(prediction, index)
        print(labels[index])

        key= cv2.waitKey(1)
        
        if key == ord("c"):
            sentence= []
            
        if key == ord("s"):
            print("Storing...")
            filename= "./voice/voice-"+str(time.time())+".mp3"
            gTTS(text=" ".join(sentence), lang="en", slow=True).save(filename)
            
        if key == ord("v"):
            print("Appending word...")
            sentence.append(labels[index])
            print(sentence)
            # t2s.say(labels[index])
            # t2s.runAndWait()

        if cv2.waitKey(10) & key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

draw_landmarks(frame, results)
