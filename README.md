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
<h3>Logic of project</h3>
The project includes direct working with the 68 facial landmark detector and also the face detector of the Dlib library.
The 68 facial landmark detector is a robustly trained efficient detector which detects the points on the human face using which 
we determine whether the eyes are open or close, & yawning and will triggering alarm by voice out using Espeak.</br></br>
<center><img src="https://github.com/MirzaAzhar172/FYP_DrowinessYawnDetection-Face/blob/main/mode%20alarm%20off.JPG?raw=true" align="center" height="350"></center>
<h3>Facial_Landmarks_68</h3>
<b>The facial landmarks 68 format for face detection <img src="https://github.com/MirzaAzhar172/FYP_DrowinessYawnDetection-Face/blob/main/68-facial-landmarks.png?raw=true" align="center" height="350"></center>
<b>The 68-landmark detector data (.dat) file can be found <a href=""> CLICK HERE!</a></B>

<h3>The working of the project</h3>
<ul><li>As you can see the<b> above screenshot</b> where the landmarks aredetected using the detector.
<li>Now we are taking the ratio which is described as <i>'Sum of distances of vertical landmarks divided by twice the distance between horizontal landmarks'</i>.
<li>Now this ratio dependent on your system which  configure accordingly for  thresholds of sleeping, drowsy, active.</ul>
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
