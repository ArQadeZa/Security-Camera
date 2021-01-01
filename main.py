###################################################################
############         Author : Matthew Tannous          ############
############            Date : 01/01/2021              ############
###################################################################

import cv2
import pyautogui

def ScreenOff():
    cv2.destroyAllWindows()  # destroys all the windows
    pyautogui.hotkey('win','r') #opens run window
    pyautogui.typewrite('cmd\n') #types cmd and then presses enter
    pyautogui.typewrite('rundll32.exe user32.dll, LockWorkStation\n') # locks the computer

def __init__():
    face_cascade =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0) #captures the first webcam in the system

    while True:
        ret_flag , frame =  cap.read()

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #changes the color of the frame to grayscale
        faces = face_cascade.detectMultiScale(gray,1.1,4) #detect faces

        if(len(faces) == 0):
            ScreenOff()
        else:
            for (x,y,w,h) in faces:                                  #aligns the rectangle with the detected faces
                cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),5)


        cv2.imshow('frame',frame)           #displays the current frame

        if (cv2.waitKey(1) & 0xFF == ord('q')): #if g is pressed the program quits
            break

    cap.release() #releases the capture
    cv2.destroyAllWindows() #destroys all the windows

__init__()