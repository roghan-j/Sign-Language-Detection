import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

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

counter= 0

folder= 'data/thankyou'

cap = cv2.VideoCapture(0)

# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():

        # Read feed
        ret, frame = cap.read()

        # Make detections
        image, results = mediapipe_detection(frame, holistic)
        print(results)
        
        # Draw landmarks
        draw_styled_landmarks(image, results)

        # Show to screen
        cv2.imshow('OpenCV Feed', image)

        key= cv2.waitKey(1)
        
        if key == ord("s"):
            counter += 1
            cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', image)
            print(counter)

        # Break gracefully
        if cv2.waitKey(10) & key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

draw_landmarks(frame, results)

# plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

# while True:
#     success, img= cap.read()
#     hands, img= detector.findHands(img)

#     if hands:
#         hand= hands[0]
#         x,y,w,h= hand['bbox']

        # if y-offset > 0 and x-offset>0:
        #     imgWhite= np.ones((imgSize, imgSize, 3), np.uint8)*255
        #     imgCrop= img[y-offset : y+h+offset, x-offset : x+w+offset]

        #     imgCropShape= imgCrop.shape

        #     aspectRatio= h/w

            # if aspectRatio > 1:
            #     k= imgSize/h
            #     wCal= math.ceil(k*w)
            #     imgResize= cv2.resize(imgCrop, (wCal, imgSize))
            #     imgResizeShape= imgResize.shape
            #     wGap= math.ceil((imgSize-wCal)/2)
            #     imgWhite[:, wGap:wCal+wGap]= imgResize

            # else:
            #     k= imgSize/w
            #     hCal= math.ceil(k*h)
            #     imgResize= cv2.resize(imgCrop, (imgSize, hCal))
            #     imgResizeShape= imgResize.shape
            #     hGap= math.ceil((imgSize-hCal)/2)
            #     imgWhite[hGap:hCal+hGap, :]= imgResize

            # cv2.imshow("ImageCrop", imgCrop)
            # cv2.imshow("ImageWhite", imgWhite)


    # cv2.imshow("Image", img)
    # key= cv2.waitKey(1)

    # if key == ord("s"):
    #     counter += 1
    #     cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', img)
    #     print(counter)