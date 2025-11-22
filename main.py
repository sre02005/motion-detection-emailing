import os

import cv2
import time
import emailing
import glob
from threading import Thread


count=0
video=cv2.VideoCapture(0)
time.sleep(1)
first_frame=None
status_list=[]

def clean_folder():#last step it is to clear the files fter sending email
    images = glob.glob('files/*png')
    for images in images:
        os.remove(images)


while True:
    status=0

    check,frames=video.read()

    gray_scale=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    guas=cv2.GaussianBlur(gray_scale,(7,7),0)

    if first_frame is None:
        first_frame=guas
    delta_frame=cv2.absdiff(first_frame,guas)
    threshold=cv2.threshold(delta_frame,45,255,cv2.THRESH_BINARY)[1]
    dilate_frame=cv2.dilate(threshold,None,iterations=2)
    #to find what is moving we need  to contour
    contours,check=cv2.findContours(dilate_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour)<10000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frames, (x, y, x + w, y + h), (0, 200, 0), 3)
        if contour.any():
            status=1#whole status and status_list is to determine weather the object is  in the frame or not
            #if in the frame , call the send email, function , if no motion=0, yes motion=1
            #we took last 2 elements of the list to get the exact time object leaves the frame as it enters 1 and leaves 0
            cv2.imwrite(f'files/{count}.png',frames)
            count+=1#all files are now written well with integeer names
            images_list = glob.glob('files/*png')  # all png files are made into list
            index = int(len(images_list)/2)
            email_img = images_list[index]

    status_list.append(status)
    status_list = status_list[-2:]




    print(status_list)

    if status_list[0]==1 and status_list[1]==0:   #it means the object is going to exit
        email_thread=Thread(target=emailing.send_email,args=(email_img,))#args should be a tuple
        email_thread.daemon=True
        clean_thread=Thread(target=clean_folder)
        email_thread.daemon=True#multi threading is happening to prevent  any lag

        email_thread.start()


    cv2.imshow('my frames',frames)
    if cv2.waitKey(1)==ord('q'):
        break
video.release()
clean_thread.start()