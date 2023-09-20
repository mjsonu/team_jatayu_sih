import cv2
import os
import numpy as np
import seaborn as sb
import pandas as pd
from matplotlib import pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from ultralytics import YOLO


x_mouse=0
y_mouse=0


plot1 = plt.subplot2grid((2, 2), (0, 0))
plot2 = plt.subplot2grid((2, 2), (1, 0), rowspan=2)

model = YOLO("yolov5m6u.pt")


vid=cv2.VideoCapture("test_case4.jpg")


def mouse_events(event,x,y,flags,param):

    if event==cv2.EVENT_MOUSEMOVE:

        global x_mouse
        global y_mouse

        x_mouse=x
        y_mouse=y



while True:
    
    success,frame=vid.read()
    frame2= cv2.resize(frame, (960, 540))

    # object detection
    results = model.predict(frame2)
    
    result=results[0]
    #cv2.imshow("frame",result.plot())
    

    # temperature part
    
    gray8=cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)

    data=gray8[y_mouse,x_mouse]
    print(data)

    cv2.circle(gray8, (x_mouse, y_mouse), 2, (0, 0, 0), -1)
    cv2.putText(gray8,"{0:.1f}".format(data),(x_mouse-80, y_mouse-15), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),5)

    result_temp= cv2.applyColorMap(gray8, cv2.COLORMAP_JET)
    result_temp2= cv2.applyColorMap(gray8, cv2.COLORMAP_MAGMA)
