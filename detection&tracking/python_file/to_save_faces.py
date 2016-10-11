## this program is based on the haar_cascade classifier which are based on  Viola and Jones algorithm
## __author__ = 'Brindal Patel'
## this program is creating database of the detected face during real time


import numpy as np
import cv2
#import Image


# this function will create the box arround the detcted face
def create_box(a,b,c,d):
    cv2.rectangle(imag,(a,b),(a+c,b+d),(0,255,0),2)

def variable_itteration(l):
    l=l+1
    return(l)

# number from where you want to start a name of the file
n=140

# this is usual path for windows user.
face_casc = cv2.CascadeClassifier('C:\Python27\libs\haarcascade_frontalface_default.xml')

vid = cv2.VideoCapture(0)
while (vid.isOpened()):
    ret,imag = vid.read()

    faces = face_casc.detectMultiScale(imag, 1.2, 5, minSize=(10,10),maxSize=(500,500))

    for (x,y,w,h) in faces:
        n=variable_itteration(n)
        create_box(x,y,w,h)
        save_image = imag[y:y+h, x:x+w] # cut out the face portion from image
        cv2.imwrite("hey%d.png"%(n),save_image)
        print n

    cv2.imshow('image',imag)
    k=cv2.waitKey(10) # escape key to exit
    if k==27:
        break

# to close all the window
cv2.waitKey(0)
cv2.destroyAllWindows()
