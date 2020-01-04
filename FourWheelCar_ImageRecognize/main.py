import picamera
import ImagePredict
import CarClass
import time

# stop the car move
CarClass.FourWheelDriveCar().carMove('S')
print('stop the car move')

# take pic
camera = picamera.PiCamera()

# loop for image take pictures
while(True):
      
    camera.capture('motion.jpg')
    print('camera take the picture')
    
    # image recognition class
    imgpredict = ImagePredict.ImagePredict(path='motion.jpg')
    imRecog = imgpredict.dataTest()
    print('predict the picture')
    print('imRecog=',imRecog)
    
    # if is the goal
    if imRecog == 'class1' :
        
        CarClass.FourWheelDriveCar().carMove('B')
        time.sleep(1)
        CarClass.FourWheelDriveCar().carMove('BR')
        time.sleep(1)
        CarClass.FourWheelDriveCar().carMove('R')
        time.sleep(1)
        CarClass.FourWheelDriveCar().carMove('F')
        time.sleep(1)
        CarClass.FourWheelDriveCar().carMove('BL')
        time.sleep(1)
        CarClass.FourWheelDriveCar().carMove('L')
        time.sleep(1)
        CarClass.FourWheelDriveCar().carMove('F')
        time.sleep(1)       
        CarClass.FourWheelDriveCar().carMove('S')