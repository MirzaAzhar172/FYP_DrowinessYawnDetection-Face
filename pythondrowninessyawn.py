from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread, Lock
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import pyttsx3
import os
import paho.mqtt.client as mqtt

# Initialize MQTT client
broker_address = "127.0.0.1"  # Replace with your MQTT broker IP
port = 1883  # Default MQTT port
client = mqtt.Client(client_id="PythonClient", protocol=mqtt.MQTTv5)
client.connect(broker_address, port)

# Initialize a lock
engine_lock = Lock()

def alarm(msg):
    global alarm_status
    global alarm_status2

    while alarm_status:
        print('Calling - alarm 1')
        with engine_lock:
            engine.say(msg)
            engine.runAndWait()
        print('WARNING!! 1 - executed')  # Debug message
        client.publish("alarm_topic", msg)

    if alarm_status2:
        print('Calling alarm 2')
        with engine_lock:
            engine.say(msg)
            engine.runAndWait()
        print('WARNING!! 2 executed')  # Debug message
        client.publish("alarm_topic", msg)

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def final_ear(shape):
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]

    leftEAR = eye_aspect_ratio(leftEye)
    rightEAR = eye_aspect_ratio(rightEye)

    ear = (leftEAR + rightEAR) / 2.0
    return (ear, leftEye, rightEye)

def lip_distance(shape):
    top_lip = shape[50:53]
    top_lip = np.concatenate((top_lip, shape[61:64]))

    low_lip = shape[56:59]
    low_lip = np.concatenate((low_lip, shape[65:68]))

    top_mean = np.mean(top_lip, axis=0)
    low_mean = np.mean(low_lip, axis=0)

    distance = abs(top_mean[1] - low_mean[1])
    return distance

# Parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-w", "--webcam", type=int, default=0, help="index of webcam on system")
args = vars(ap.parse_args())

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 30
YAWN_THRESH = 20  # Adjusted threshold for yawning detection
alarm_status = False
alarm_status2 = False
saying = False
COUNTER_EYE = 0  # Counter for eye drowsiness
COUNTER_YAWN = 0  # Counter for yawning

print("-> Loading the predictor and detector...")
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print("-> Starting Video Stream")

# Try to start the video stream with error handling
vs = VideoStream(src=args["webcam"])
try:
    vs.start()
except Exception as e:
    print(f"Error starting video stream: {e}")
    exit()

time.sleep(1.0)

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Load the shape predictor
current_dir = os.path.dirname(os.path.abspath(__file__))
predictor_filename = 'shape_predictor_68_face_landmarks.dat'
predictor_path = os.path.join(current_dir, predictor_filename)

if not os.path.isfile(predictor_path):
    print(f"Error: Unable to locate the shape predictor file at '{predictor_path}'")
    exit()

predictor = dlib.shape_predictor(predictor_path)

while True:
    frame = vs.read()
    if frame is None:
        print("Error: Unable to read frame from video stream")
        break

    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in rects:
        rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))

        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        eye = final_ear(shape)
        ear = eye[0]
        leftEye = eye[1]
        rightEye = eye[2]

        distance = lip_distance(shape)

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        lip = shape[48:60]
        cv2.drawContours(frame, [lip], -1, (0, 255, 0), 1)

        # Check for eye drowsiness
        if ear < EYE_AR_THRESH:
            COUNTER_EYE += 1

            if COUNTER_EYE >= EYE_AR_CONSEC_FRAMES:
                if not alarm_status:
                    alarm_status = True
                    t = Thread(target=alarm, args=('DANGER!!!! YOU ARE NOT WELL, WAKE UP!!!',))
                    t.daemon = True
                    t.start()

                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        else:
            COUNTER_EYE = 0
            alarm_status = False

        # Check for yawning
        if distance > YAWN_THRESH:
            COUNTER_YAWN += 1

            if COUNTER_YAWN >= 3:  # Adjusted consecutive frames for yawning
                if not alarm_status2 and not saying:
                    alarm_status2 = True
                    t = Thread(target=alarm, args=('STOP DRIVING!!, You need to take some rest or Fresh Air',))
                    t.daemon = True
                    t.start()
        else:
            COUNTER_YAWN = 0
            alarm_status2 = False

    # Display alarm status
    if alarm_status or alarm_status2:
        cv2.putText(frame, "ALARM - YAWN DETECTED", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "MODE ALARM - OFF", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
