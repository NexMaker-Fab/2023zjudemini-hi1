    import numpy as np
    import cv2
    import os
    import time  
    import RPi.GPIO as GPIO
    import Adafruit_PCA9685
    import threading


    servo_pwm = Adafruit_PCA9685.PCA9685()


    def set_servo_angle(channel,angle):
        angle=4096*((angle*11)+500)/20000
        servo_pwm.set_pwm(channel,0,int(angle))
    set_servo_angle(3,90) 
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)
    TARGET_X = 400
    TARGET_Y = 250
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    def get_center(frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))
        if len(faces) > 0:
            max_area = 0
            max_face = faces[0]
            for face in faces:
                (x, y, w, h) = face
                area = w * h
                if area > max_area:
                    max_area = area
                    max_face = face
            (x, y, w, h) = max_face
            center_x = x + w // 2
            center_y = y + h // 2
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
            return (center_x, center_y)
        else:
            return None
        
    def get_center_threaded(frame, result):   
        center = get_center(frame)
        result['center'] = center
        #print('true')

    try:
        while True:
            ret, frame = cap.read()
            frame = cv2.flip(frame, 180)
            if not ret:
                break
            center = get_center(frame)
            # 创建一个字典来存储线程结果
            center_result = {}
            # 启动线程来执行get_center函数
            threading.Thread(target=get_center_threaded, args=(frame, center_result)).start()

            cv2.imshow('frame', frame)
            #if 'center' in center_result:
                #center = center_result['center']
            if center is not None:
                (x, y) = center
                x_diff = x - TARGET_X
                y_diff = y - TARGET_Y
                print('x_diff')
                if abs(x_diff) > 100:
                    set_servo_angle(3,0)
                    #time.sleep(3)
                        
                else :
                    set_servo_angle(3,90)
                    
            else:
                set_servo_angle(3,90)           
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        GPIO.cleanup()
        cap.release()
        cv2.destroyAllWindows()   