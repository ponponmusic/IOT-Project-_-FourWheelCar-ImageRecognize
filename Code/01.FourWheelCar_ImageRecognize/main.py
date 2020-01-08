import picamera
import ImagePredict
import CarClass
import time

# car object
car = CarClass.FourWheelDriveCar()

# stop the car move
car.carMove('S')
print('stop the car move')

# take pic
camera = picamera.PiCamera()

# image recognition class
imgpredict = ImagePredict.ImagePredict()

# loop for image take pictures
while(True):
      
    camera.capture('motion.jpg')
    print('camera take the picture')
    
    
    imRecog = imgpredict.dataTest(path = 'motion.jpg')
    print('predict the picture')
    print('imRecog=',imRecog)
    
    # if is the goal
    if imRecog == 'class1' :
        
        car.carMove('B')
        time.sleep(5)
        car.carMove('BR')
        time.sleep(5)
        car.carMove('R')
        time.sleep(5)
        car.carMove('F')
        time.sleep(5)
        car.carMove('BL')
        time.sleep(5)
        car.carMove('L')
        time.sleep(5)
        car.carMove('F')
        time.sleep(5)       
        car.carMove('S')