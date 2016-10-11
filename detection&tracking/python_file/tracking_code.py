 __author__ = "Brindal Patel"
## this program is based on the haar_cascade classifier which are based on  Viola and Jones algorithm
## this program is creating database of the detected face during real time

## Used microcontroller board: ""Arduino Uno""



import numpy as np
import cv2
import serial

ser = serial.Serial(port='COM5',baudrate=9600,timeout=1)
# this is for the opening communication between computer and Arduino Uno using serial portion
# make sure to check your COM-Port number, if it is different change it in above line.
# If you are using different baudrate than edit according to that

#This function can be used to send serial data to Arduino Uno to do something
def servo_rotate_serialdata(motornum, AngleServo):
    ser.write(chr(255))
    ser.write(chr(motornum))
    ser.write(chr(AngleServo))


#this function will create the box arround the detcted face
def create_box(a,b,c,d):
    cv2.rectangle(imag,(a,b),(a+c,b+d),(0,255,0),2)

def variable_itteration(l):
    l=l+1
    return(l)

def write_image():
    save_image= imag[y:y+h, x:x+w] #cut out the face portion from image
    cv2.imwrite("hey%d.png"%(n),save_image)

def angle_servo(angle):
    #prov=90
    if angle>230:
        prov=2
        servo_rotate_serialdata(1,prov)

    elif angle<195:
        prov=1
        servo_rotate_serialdata(1,prov)


# this is usual path for windows user. If you are not able to find a xml file on your machine or online, check the github repository.
face_casc = cv2.CascadeClassifier('C:\Python27\libs\haarcascade_frontalface_default.xml')

videoWeb = cv2.VideoCapture(0)

n=0

while (videoWeb.isOpened()):

    ret,imag = videoWeb.read()
    #cv2.imshow('xyz',imag)
    faces = face_casc.detectMultiScale(imag, 1.2, 5, minSize=(10,10),maxSize=(500,500))
    for (x,y,w,h) in faces:
        create_box(x,y,w,h)
        n=variable_itteration(n)
        # If you want to save all the detected face,then uncomment the following line
        # write_image()

        # calling function to send serial data of angle to rotate servo motor
        angle_servo(x)

    cv2.imshow('image',imag)

    # to add exit key
    k=cv2.waitKey(10)
    # 27 is for the escape key, you can easily google the number and switchwith other keys
    if k==27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
