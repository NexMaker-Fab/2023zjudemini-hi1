from flask import Flask, request, jsonify
import json
from datetime import datetime
from flask_cors import CORS
import os
from calculate import analyze_posture
import RPi.GPIO as GPIO
import time
import threading
import Adafruit_PCA9685

app = Flask(__name__)
CORS(app)  # 启用CORS

BtnPin = 19
Gpin    = 5
Rpin    = 6

# Helper function to make 
baseline_data = {}
current_data = {}
current_posture={'head_tilt': True, 'body_tilt': True, 'nose_shoulder_distance_normal': True}
servo_pwm = Adafruit_PCA9685.PCA9685()

servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
#setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    servo_pwm.set_pwm(channel, 0, pulse)

def set_servo_angle(channel,angle):
    angle=4096*((angle*11)+500)/20000
    servo_pwm.set_pwm(channel,0,int(angle))

servo_pwm.set_pwm_freq(45)

def GPIO_setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
    GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
    GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V) 


    
GPIO_setup()
set_servo_angle(3,0)
set_servo_angle(4,0)

# Function to handle button press
def button_listener():
    global baseline_data
    global current_data
    while True:
        if GPIO.input(BtnPin) == GPIO.HIGH:  # Button pressed
            baseline_data = current_data
            print(baseline_data)
            print('Start timing for 3 seconds')
            GPIO.output(Gpin, GPIO.HIGH)
            GPIO.output(Rpin, GPIO.LOW)
            time.sleep(15)  # 25mins should be 1500s
            baseline_data={}
            set_servo_angle(4,60) # ANGLE
            time.sleep(1)
            set_servo_angle(4,0)
            GPIO.output(Gpin, GPIO.LOW)
            GPIO.output(Rpin, GPIO.HIGH)
            #baseline_data={}
            # time.sleep(0.3)  # Debounce delay

def format_data(input_keypoints):
    formatted_data = {}
    if len(input_keypoints) == 0:
        print(input_keypoints)
        return formatted_data
    keypoints = input_keypoints[0]["keypoints"]
    for kp in keypoints:
        formatted_data[kp["name"]] = {"x": kp["x"], "y": kp["y"]}
    return formatted_data

@app.route('/upload_pose_data', methods=['POST'])
def upload_pose_data():
    global baseline_data
    global current_data
    global current_posture
    pose_data = request.json
    current_data = format_data(pose_data)
    # print('------------------------------------')
    # print(current_data)
    # print(type(current_data))
    # print('------------------------------------')
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f'pose_data/{timestamp}.json'
    print('get data')
    # current_data  = json.dumps(pose_data[0], indent=4)  # save data in current data
    if  current_data !={}:
        result = analyze_posture(baseline_data, current_data)
        print(result)
        if result['head_tilt'] == True or result['body_tilt'] == True:
            print('head tilt')
            set_servo_angle(3,35)
            time.sleep(1)
            set_servo_angle(3,0)
        

        

    # with open(file_name, 'w') as f:
    #     json.dump(pose_data, f, ensure_ascii=False, indent=4)
    # print(timestamp)
    
    return jsonify({'message': 'Data received and stored'}), 200

if __name__ == '__main__':
    thread = threading.Thread(target=button_listener)
    thread.start()
    app.run(debug=True, port=5000)
    
