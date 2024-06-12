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
<h3>Fundamental/Guidance of this project</h3>
The project works with the 68 facial landmark detector, haar cascade, OpenCV, Espeak, MQTT broker, and Node-red map flow.
The 68 facial landmark detector a robustly detects the points on the human face using which 
we determine whether the eyes are open or closed, & yawning and will trigger alarm by a voice out using Espeak (voice synthesizer).</br></br>
<center><img src="https://github.com/MirzaAzhar172/FYP_DrowinessYawnDetection-Face/blob/main/mode%20alarm%20off.JPG?raw=true" align="center" height="350"></center>
<h3>Facial_Landmarks_68</h3>
<img src="https://github.com/MirzaAzhar172/FYP_DrowinessYawnDetection-Face/blob/main/68-facial-landmarks.png?raw=true" align="center" height="350">
The 68-landmark detector data (.dat) file can be found <a href="https://github.com/Arijit1080/Drowsiness-and-Yawn-Detection-with-voice-alert-using-Dlib/blob/master/shape_predictor_68_face_landmarks.dat"> CLICK HERE!

<h3>OUTPUT FROM PROJECT (WEBCAM)</h3>
<ul><li>As you can see the<b> above screenshot</b> where the landmarks ar edetected using webcam and link to ESP32 cam for MQTT.
<li>Now we are taking the ratio which is described as <i>'Sum of distances of vertical landmarks divided by twice the distance between horizontal landmarks'</i>.
<li>The ratio depends system which is configured accordingly for 3 main  of sleepy eye, tired, yawn & active.</ul>
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
# Using NODE-RED and Slack as transmission data and generate notifications.
Besides using python with libraries, dependencies and MQTT, I used Node-Red for send alarm status by through MQTT to Slack API.
<h3>MAP FLOW</h3>
<li>Python (libraries) -> MQTT -> Node-Red -> Slack API.</ul>
<p><img src="https://github.com/MirzaAzhar172/FYP_DrowinessYawnDetection-Face/blob/main/drowsiness.JPG?raw=true" align="center" height="350">

<h3>STEP BY STEP - configure localhost to create MQTT.</h3>

<li>1.open  Cmd administrator.</li>
<li>2.Client = netsh interface portproxy add v4tov4 listenaddress=192.168.140.44 listenport=1883 connectaddress=127.0.0.1 connectport=1883</li>
<li>3.Server </li>
- netsh interface portproxy add v4tov4 listenaddress=192.168.140.44 listenport=1883 connectaddress=127.0.0.1 connectport=1883
- netsh interface portproxy show all.
<li>5. Open MQTT explorer, linkkan connect address 127.0.0.1 yang dah run dekat Arduino ide untuk link ke MQTT.</li>
<li>6. Run python coding micro sleep alarm yg link webcam.</li>
<li>7. Tgk output dekat MQTT explorer, dia akan link terminal python coding yang run tu je MQTT terminal.</li>
