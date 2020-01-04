import RPi.GPIO as GPIO
import time
 
class FourWheelDriveCar():
    # Define the number of all the GPIO that will used for the 4wd car
 
    def __init__(self):
        '''
        1. Read pin number from configure file
        2. Init all GPIO configureation
        '''
        self.LEFT_BEHIND_1 = 31
        self.LEFT_BEHIND_2 = 33
 
        self.RIGHT_BEHIND_1 = 35
        self.RIGHT_BEHIND_2 = 37
 
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.LEFT_BEHIND_1, GPIO.OUT)
        GPIO.setup(self.LEFT_BEHIND_2, GPIO.OUT)
        GPIO.setup(self.RIGHT_BEHIND_1, GPIO.OUT)
        GPIO.setup(self.RIGHT_BEHIND_2, GPIO.OUT)
 
    def reset(self):
        # Rest all the GPIO as LOW
        GPIO.output(self.LEFT_BEHIND_1, GPIO.LOW)
        GPIO.output(self.LEFT_BEHIND_2, GPIO.LOW)
        GPIO.output(self.RIGHT_BEHIND_1, GPIO.LOW)
        GPIO.output(self.RIGHT_BEHIND_2, GPIO.LOW)
 
    def __forword(self):
        self.reset()
        GPIO.output(self.LEFT_BEHIND_1, GPIO.HIGH)
        GPIO.output(self.LEFT_BEHIND_2, GPIO.LOW)
        GPIO.output(self.RIGHT_BEHIND_1, GPIO.HIGH)
        GPIO.output(self.RIGHT_BEHIND_2, GPIO.LOW)
 
    def __backword(self):
        self.reset()
        GPIO.output(self.LEFT_BEHIND_2, GPIO.HIGH)
        GPIO.output(self.LEFT_BEHIND_1, GPIO.LOW)
        GPIO.output(self.RIGHT_BEHIND_2, GPIO.HIGH)
        GPIO.output(self.RIGHT_BEHIND_1, GPIO.LOW)
 
    def __turnLeft(self):
        '''
        To turn left, the LEFT_FRONT wheel will move backword
        All other wheels move forword
        '''
        self.reset()
        GPIO.output(self.LEFT_BEHIND_1, GPIO.HIGH)
        GPIO.output(self.LEFT_BEHIND_2, GPIO.LOW)
        GPIO.output(self.RIGHT_BEHIND_1, GPIO.LOW)
        GPIO.output(self.RIGHT_BEHIND_2, GPIO.LOW)
 
    def __turnRight(self):
        '''
        To turn right, the RIGHT_FRONT wheel move backword
        All other wheels move forword
        '''
        self.reset()
        GPIO.output(self.LEFT_BEHIND_1, GPIO.LOW)
        GPIO.output(self.LEFT_BEHIND_2, GPIO.LOW)
        GPIO.output(self.RIGHT_BEHIND_1, GPIO.HIGH)
        GPIO.output(self.RIGHT_BEHIND_2, GPIO.LOW)
 
    def __backLeft(self):
        '''
        To go backword and turn left, the LEFT_BEHIND wheel move forword
        All other wheels move backword
        '''
        self.reset()
        GPIO.output(self.LEFT_BEHIND_1, GPIO.LOW)
        GPIO.output(self.LEFT_BEHIND_2, GPIO.HIGH)
        GPIO.output(self.RIGHT_BEHIND_2, GPIO.LOW)
        GPIO.output(self.RIGHT_BEHIND_1, GPIO.LOW)
 
    def __backRight(self):
        '''
        To go backword and turn right, the RIGHT_BEHIND wheel move forword
        All other wheels move backword
        '''
        self.reset()
        GPIO.output(self.LEFT_BEHIND_2, GPIO.LOW)
        GPIO.output(self.LEFT_BEHIND_1, GPIO.LOW)
        GPIO.output(self.RIGHT_BEHIND_1, GPIO.LOW)
        GPIO.output(self.RIGHT_BEHIND_2, GPIO.HIGH)
 
    def __stop(self):
        self.reset()
 
    def carMove(self, direction):
        '''
        Car move according to the input paramter - direction
        '''
        if direction == 'F':
            self.__forword()
        elif direction == 'B':
            self.__backword()
        elif direction == 'R':
            self.__turnRight()
        elif direction == 'L':
            self.__turnLeft()
        elif direction == 'BL':
            self.__backLeft()
        elif direction == 'BR':
            self.__backRight()
        elif direction == 'S':
            self.__stop()
        else:
            print("The input direction is wrong! You can just input: F, B, L, R, BL,BR or S")
