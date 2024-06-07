# FYP_DrowinessYawnDetection-Face detect using OpenCV, Haar Cascade, Mosquitto Broker MQTT
untuk projek fyp uitm sem6 - Exhibition Bachelor Sains Komputer

## Dependencies
1. Python 3
2. opencv
3. dlib
4. imutils
5. scipy
6. numpy
7. argparse

# Explaination from this project
Driver drowsiness detection is a project built using Dlib and OpenCV, Haar Cascade & Espeak with Python as a backend language.
<h3>Logic/Basic of project</h3>
The project includes direct working with the 68 facial landmark detector, haar cascade, OpenCV, Espeak, MQTT broker.
The 68 facial landmark detector is a robustly detecting the points on the human face using which 
we determine whether the eyes are open or close, & yawning and will triggering alarm by voice out using Espeak.</br></br>
<center><img src="https://github.com/MirzaAzhar172/FYP_DrowinessYawnDetection-Face/blob/main/mode%20alarm%20off.JPG?raw=true" align="center" height="350"></center>
<h3>Facial_Landmarks_68</h3>
<img src="https://github.com/MirzaAzhar172/FYP_DrowinessYawnDetection-Face/blob/main/68-facial-landmarks.png?raw=true" align="center" height="350">
The 68-landmark detector data (.dat) file can be found <a href="https://github.com/Arijit1080/Drowsiness-and-Yawn-Detection-with-voice-alert-using-Dlib/blob/master/shape_predictor_68_face_landmarks.dat"> CLICK HERE!

<h3>The working of the project</h3>
<ul><li>As you can see the<b> above screenshot</b> where the landmarks ar edetected using webcam and link to ESP32 cam for MQTT.
<li>Now we are taking the ratio which is described as <i>'Sum of distances of vertical landmarks divided by twice the distance between horizontal landmarks'</i>.
<li>The ratio depends system which configures accordingly for 3 main  of sleepy eye, tired, yawn & active.</ul>
<p><img src="https://github.com/MirzaAzhar172/FYP_DrowinessYawnDetection-Face/blob/main/drowsiness.JPG?raw=true" align="center" height="350">
<img src="https://github.com/MirzaAzhar172/FYP_DrowinessYawnDetection-Face/blob/main/Capture.JPG?raw=true" align="center" height="350">
<img src="https://github.com/MirzaAzhar172/FYP_DrowinessYawnDetection-Face/blob/main/yawn.JPG?raw=true" align="center" height="350">

## Setups

Change the threshold values according to your need
```
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 30
YAWN_THRESH = 10`	//change this according to the distance from the camera
```
