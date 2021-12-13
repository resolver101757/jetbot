import time
from Adafruit_MotorHAT import Adafruit_MotorHAT
import atexit

class Robot ():
    def __init__(self):
        self.mh = Adafruit_MotorHAT(addr=0x60,i2c_bus=1)
        self.motor_left = self.mh.getMotor(1)
        self.motor_right = self.mh.getMotor(2)
        self.motor_left.setSpeed(150)
        self.motor_right.setSpeed(150)
        self.motor_left.run(Adafruit_MotorHAT.FORWARD)
        self.motor_right.run(Adafruit_MotorHAT.FORWARD)
        self.motor_left.run(Adafruit_MotorHAT.RELEASE)
        self.motor_right.run(Adafruit_MotorHAT.RELEASE)
        atexit.register(self.turn_off_motors)

    def turn_off_motors(self):
        self.motor_left.run(Adafruit_MotorHAT.RELEASE)
        self.motor_right.run(Adafruit_MotorHAT.RELEASE)

    def forward(self):
        self.motor_left.run(Adafruit_MotorHAT.FORWARD)
        self.motor_right.run(Adafruit_MotorHAT.FORWARD)

    def backward(self):
        self.motor_left.run(Adafruit_MotorHAT.BACKWARD)
        self.motor_right.run(Adafruit_MotorHAT.BACKWARD)

    def left(self):
        self.motor_left.run(Adafruit_MotorHAT.FORWARD)
        self.motor_right.run(Adafruit_MotorHAT.BACKWARD)

    def right(self):
        self.motor_left.run(Adafruit_MotorHAT.BACKWARD)
        self.motor_right.run(Adafruit_MotorHAT.FORWARD)

    def stop(self):
        self.motor_left.run(Adafruit_MotorHAT.RELEASE)
        self.motor_right.run(Adafruit_MotorHAT.RELEASE)

robot = Robot()
