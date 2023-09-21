# first try to get temp gradient on image

import cv2
import numpy as np
import argparse


# Load the input image
image = cv2.imread('test_case4.jpg')
cv2.imshow("ORIGINAL", image)


cv2.waitKey(0)


# Use the cvtColor() function to grayscale the image gray 8
gray8_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

gray16_image=gray8_image

x_mouse = 0
y_mouse = 0

L1=[]
def mouse_events(event, x, y, flags, param):
    # mouse movement event
    if event == cv2.EVENT_MOUSEMOVE:
    # update global mouse coordinates
        global x_mouse
        global y_mouse
        print("Hi",end="")
        x_mouse = x
        y_mouse = y

        # create thermal video fps variable (8 fps in this case)
        fps = 8

        pixel_flame_gray8 = gray8_image [y_mouse,x_mouse]
        gray16_image=gray8_image

        print(pixel_flame_gray8)

        #print(L1)
        cv2.circle(gray8_image, (x_mouse, y_mouse), 2, (0, 0, 0), -1)
        cv2.circle(gray8_image, (x_mouse, y_mouse), 2, (0, 0, 0), -1)

        cv2.putText(gray16_image,"{0:.1f} ".format(pixel_flame_gray8),(x_mouse-80, y_mouse-15), cv2.FONT_HERSHEY_PLAIN, 1,(255,0,0),2)

        jet_palette = cv2.applyColorMap(gray8_image, cv2.COLORMAP_JET)
        cv2.imshow("jet", jet_palette)

        


# pixel_flame_gray8

cv2.imshow('gray8', gray16_image)
cv2.setMouseCallback('gray8', mouse_events)

print("HI OVER")
print(L1)

'''
#pixel_flame_gray8 = gray8_image [y_mouse,x_mouse]
#print(pixel_flame_gray8)

gray8_image=np.zeros((120,160),dtype=np.int8)
gray8_image=cv2.normalize(gray16_image,gray8_image,0,255,cv2.NORM_MINMAX)

gray8_image=np.uint8(gray8_image)

cv2.circle(gray8_image, (x_mouse, y_mouse), 2, (0, 0, 0), -1)
cv2.circle(gray8_image, (x_mouse, y_mouse), 2, (0, 0, 0), -1)
'''


#cv2.putText(gray16_image,"{0:.1f} ".format(pixel_flame_gray8),(x_mouse-80, y_mouse-15), cv2.FONT_HERSHEY_PLAIN, 1,(255,0,0),2)
#cv2.imshow("gray16", gray16_image)

#inferno_palette = cv2.applyColorMap(gray8_image, cv2.COLORMAP_INFERNO)
#cv2.imshow("inferno", inferno_palette)

#jet_palette = cv2.applyColorMap(gray8_image, cv2.COLORMAP_JET)
#cv2.imshow("jet", jet_palette)

#viridis_palette = cv2.applyColorMap(gray8_image, cv2.COLORMAP_VIRIDIS)
#cv2.imshow("viridis", viridis_palette)


    #cv2.imshow("ans",result)

    screen1= np.concatenate((result_temp,frame2), axis=0)
    screen2= np.concatenate((result.plot(),result_temp2), axis=0)

    screen=np.concatenate((screen1,screen2),axis=1)
    cv2.imshow("out",screen)
    
    cv2.setMouseCallback("out",mouse_events)


    if cv2.waitKey(10) & 0xFF==ord("q"):
        break

cv2.imshow("out",result_temp)
cv2.imshow("out2",plt.show())

vid.release()
cv2.destroyAllWindows
