# Face Detection and Tracking
### Introduction
Real time "Face Detection and tracking" using Arduino-UNO, webcam, servo motor and OpenCV library in Python.  
This project explains and shows code for the webcam connected to computer via usb. If you want to connect webcam or camera sensor directly to the arduino board then you may need to edit the code.  
In this Project, Video processing is done by the computer.

### Features
* Written in Pyhton and Arduino Software
* No installation required

### What's included
```
detection&tracking/
  |-- arduino_file/
		|--arduino.ino
		|--setup.png
  |-- python_file/
		|--haarcascade_frontalface_default.xml
		|--to_save_faces.py
		|--tracking_code.py

```

### Requirement:
opencv2 (cv2), serial (This Module should be installed for the python to run fresh_tomatoes.py)

### Hardware Setup:
* Connect servo motor to the arduino. If you are not sure about the circuit please check this link by Arduino  
https://www.arduino.cc/en/Tutorial/Sweep
* Mount web-camera on the servo motor and connect web-cam to the computer. Check setup.png in the arduino_file folder
* Here, 3d printed stand was used to hold servo motor on the ground and mount webcam on it.

### Instruction:
* Download detection&tracking zip
* Run `to_save_faces.py`. If any required module is not installed, install it.  
If you do not have haarcascade_frontalface_default.xml in your pc then download provided file, change path in the code and write proper path.
* If it runs alright, then you need to connect Arduino-UNO with your computer and upload this arduino.ino program to it.
* Now, run `tracking_code.py`.


#### Note:
* provided xml file is by Intel Corporation for Open Source Computer Vision Library.  
You can also create your own classfier.
* For Reference, goto http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html

