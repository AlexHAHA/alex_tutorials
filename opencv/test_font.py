import numpy as np 
import cv2

frame = cv2.imread('sources/dog.jpg')

def fun_addtext(frame):
    label  = ['SIMPLEX', 'PLAIN',   'DUPLEX',
             'COMPLEX', 'TRIPLEX', 'SMALL', 
             'SCRIPT1', 'SCRIPT2', 'SCRIPT3']

    points = [(200*x,50*y) for y in range(1,4) for x in range(0,3)]
    print(points)
    fonts = [cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_PLAIN,   cv2.FONT_HERSHEY_DUPLEX,
             cv2.FONT_HERSHEY_COMPLEX, cv2.FONT_HERSHEY_TRIPLEX, cv2.FONT_HERSHEY_COMPLEX_SMALL, 
             cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, cv2.FONT_HERSHEY_SCRIPT_COMPLEX, cv2.FONT_HERSHEY_SCRIPT_COMPLEX]

    for l, p, f in zip(label,points,fonts):
        # 图像，文字内容， 坐标 ，字体，大小，颜色，字体厚度
        cv2.putText(frame, l, p, f, 1.0, (255,0,0), 2)

def fun1():
    global frame
    h, w = frame.shape[0:2]
    print(w,h)
    frame = cv2.resize(frame, (int(w/2),int(h/2)))
    fun_addtext(frame)
    cv2.imshow('dog',frame)

    cv2.waitKey(10000)



if __name__ == '__main__':
    fun1()