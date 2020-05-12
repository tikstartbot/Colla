print("Motortest test2.py")
#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
print("Set up GPIO Pin")

# set up Enable motor
GPIO.setup(7, GPIO.OUT)  # Connected to R-EN Motor1 FL
GPIO.setup(11, GPIO.OUT) # Connected to L-EN Motor1 FL
GPIO.setup(33, GPIO.OUT) # Connected to R-EN Motor2 FR
GPIO.setup(37, GPIO.OUT) # Connected to L-EN Motot2 FR

#set up driver motor 
GPIO.setup(13, GPIO.OUT) # Connected to FL RPWM Motor1
GPIO.setup(15, GPIO.OUT) # Connected to FL LPWM Motor1
GPIO.setup(12, GPIO.OUT) # Connected to FR RPWM Motor2
GPIO.setup(16, GPIO.OUT) # Connected to FR LPWM Motor2
GPIO.setup(29, GPIO.OUT) # Connected to BL RPWM Motor3
GPIO.setup(31, GPIO.OUT) # Connected to BL LPWM Motor3
GPIO.setup(18, GPIO.OUT) # Connected to BR RPWM Motor4
GPIO.setup(22, GPIO.OUT) # Connected to BR LPWM Motor4

# Drive the motor forward
print("GO Forward")

GPIO.output(7, GPIO.HIGH)  # Set R-EN Motor1 FL
GPIO.output(11, GPIO.HIGH) # Set L-EN Motor1 FL
GPIO.output(33, GPIO.HIGH) # Set R-EN Motor2 FR
GPIO.output(37, GPIO.HIGH) # Set L-EN Motor2 FR

# FL-CW , FR-CCW , BL-CW, BR-CCW
GPIO.output(13, GPIO.HIGH) # Set RPWM motor1 FL
GPIO.output(15, GPIO.LOW)  # Set LPWM motor1 FL
GPIO.output(12, GPIO.LOW)  # Set RPWM motor2 FR
GPIO.output(16, GPIO.HIGH) # Set LPWM motor2 FR
GPIO.output(29, GPIO.HIGH) # Set RPWM motor3 BL
GPIO.output(31, GPIO.LOW)  # Set LPWM motor3 BL
GPIO.output(18, GPIO.LOW)  # Set RPWM motor4 BR
GPIO.output(22, GPIO.HIGH) # Set LPWM motor4 BR    

# Wait 5 seconds
time.sleep(5)

# Drive the motor backward
print("Go Backward")

GPIO.output(7, GPIO.HIGH)  # Set R-EN Motor1 FL
GPIO.output(11, GPIO.HIGH) # Set L-EN Motor1 FL
GPIO.output(33, GPIO.HIGH) # Set R-EN Motor2 FR
GPIO.output(37, GPIO.HIGH) # Set L-EN Motor2 FR

#FL-CCW,FR-Cw,BL-CCW,BR-CW
GPIO.output(13, GPIO.LOW)  # Set RPWM motor1 FL
GPIO.output(15, GPIO.HIGH) # Set LPWM motor1 FL
GPIO.output(12, GPIO.HIGH) # Set RPWM motor2 FR
GPIO.output(16, GPIO.LOW)  # Set LPWM motor2 FR
GPIO.output(29, GPIO.LOW)  # Set RPWM motor3 BL
GPIO.output(31, GPIO.HIGH) # Set LPWM motor3 BL
GPIO.output(18, GPIO.HIGH) # Set RPWM motor4 BR
GPIO.output(22, GPIO.LOW)  # Set LPWM motor4 BR

# Wait 5 seconds
time.sleep(5)

# Drive the motor turn left
print("Turn Left")

GPIO.output(7, GPIO.HIGH)  # Set R-EN Motor1 FL
GPIO.output(11, GPIO.HIGH) # Set L-EN Motor1 FL
GPIO.output(33, GPIO.HIGH) # Set R-EN Motor2 FR
GPIO.output(37, GPIO.HIGH) # Set L-EN Motor2 FR

#FL-No,FR-CCw,BL-NO,BR-CCW

GPIO.output(13, GPIO.LOW)  # Set RPWM motor1
GPIO.output(15, GPIO.LOW)  # Set LPWM motor1
GPIO.output(12, GPIO.LOW)  # Set RPWM motor2
GPIO.output(16, GPIO.HIGH) # Set LPWM motor2
GPIO.output(29, GPIO.LOW)  # Set RPWM motor3
GPIO.output(31, GPIO.LOW)  # Set LPWM motor3
GPIO.output(18, GPIO.LOW)  # Set RPWM motor4
GPIO.output(22, GPIO.HIGH) # Set LPWM motor4 

# Wait 5 seconds
time.sleep(5)

# Drive the motor turn right
print("Turn Right")

GPIO.output(7, GPIO.HIGH)  # Set R-EN Motor1 FL
GPIO.output(11, GPIO.HIGH) # Set L-EN Motor1 FL
GPIO.output(33, GPIO.HIGH) # Set R-EN Motor2 FR
GPIO.output(37, GPIO.HIGH) # Set L-EN Motor2 FR

#FL-CW,FR-No,BL-CW,BR-No

GPIO.output(13, GPIO.HIGH) # Set RPWM motor1
GPIO.output(15, GPIO.LOW)  # Set LPWM motor1
GPIO.output(12, GPIO.LOW)  # Set RPWM motor2
GPIO.output(16, GPIO.LOW)  # Set LPWM motor2
GPIO.output(29, GPIO.HIGH) # Set RPWM motor3
GPIO.output(31, GPIO.LOW)  # Set LPWM motor3
GPIO.output(18, GPIO.LOW)  # Set RPWM motor4
GPIO.output(22, GPIO.LOW)  # Set LPWM motor4 

# Wait 5 seconds
time.sleep(5)

# Reset all the GPIO pins by setting them to LOW motor stop
print("Everything stop")

# Drive the motor stop
GPIO.output(7, GPIO.LOW)  # Set R-EN Motor1 FL
GPIO.output(11, GPIO.LOW) # Set L-EN Motor1 FL
GPIO.output(33, GPIO.LOW) # Set R-EN Motor2 FR
GPIO.output(37, GPIO.LOW) # Set L-EN Motor2 FR

#FL-No,FR-No,BL-NO,BR-No

GPIO.output(13, GPIO.LOW) # Set RPWM motor1
GPIO.output(15, GPIO.LOW) # Set LPWM motor1
GPIO.output(12, GPIO.LOW) # Set RPWM motor2
GPIO.output(16, GPIO.LOW) # Set LPWM motor2
GPIO.output(29, GPIO.LOW) # Set RPWM motor3
GPIO.output(31, GPIO.LOW) # Set LPWM motor3
GPIO.output(18, GPIO.LOW) # Set RPWM motor4
GPIO.output(22, GPIO.LOW) # Set LPWM motor4 

#clean GPI channel
GPIO.cleanup()

print("Test complete")

