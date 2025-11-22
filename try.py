import streamlit as st
import cv2
import time
date=time.strftime("%A")
st.title('motion detector')
start=st.button('start')
stop=st.button('stop')
if start:
    video = cv2.VideoCapture(0)
    image=st.image([])
    while True:
        ret,frame=video.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        now=time.strftime("%H:%M:%S")
        cv2.putText(img=frame,text=date,org=(50,50),fontScale=2
                    ,color=(255,2,10),thickness=2,fontFace=cv2.FONT_HERSHEY_PLAIN,lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=
                                    f'{now}', org=(50, 100), fontScale=2
                    , color=(2, 2, 255), thickness=3, fontFace=cv2.FONT_HERSHEY_PLAIN, lineType=cv2.LINE_AA)

        image.image(frame)
if stop:
    st.success('byeeeeeee')
    st.stop()


