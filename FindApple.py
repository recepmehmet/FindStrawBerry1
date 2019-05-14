import cv2 #Main Library
import numpy as np  # means matrix folder
from os import walk#For find the folder we are using this



def Find_Strawberry(camera_percent):# General function we will call this function in main folder.
    #We are creating the function with 'def'
    openTheCamera = cv2.VideoCapture(0)  # we open the camera

    # 0 => In computer, it uses default camera such as,laptop camera
    # 1 => Out computer, when we connect with usb we use with that way(EXTENTİON PART)
    def Camera_Set_Up(display, percent):
        camera_width = int(display.shape[1] * percent / 100)  # we are resize the width of camera with percently
        camera_heigth = int(display.shape[0] * percent / 100)  # we are resize the heigth of camera with percently

        dimension = (camera_width, camera_heigth)# we dont do anything just for return we collect the result

        return cv2.resize(display, dimension, interpolation=cv2.INTER_AREA)  # we have to use this library for all

    # size chancing

    while True:  # we enter the infinitive loop

        if openTheCamera.isOpened():  # security for coming respond from camera
            ret, display = openTheCamera.read()

            convertToGray = cv2.cvtColor(display, cv2.COLOR_BGR2GRAY)

            for dirpath, dirnames, filenames in walk(
                    'banana'):  # we are taking folder directly in source code folder

                for size in filenames:  # in python we are looping with elemans so it will give directly eleman names.
                    # such as strawberry3.jpg
                    takenPicture = cv2.imread('{}'.format(size),0)#This eleman has to be 'strawberry3.jpg'.
                    # So we have to changeto format for all picture
                    # 0 means you make be gray color

                    widthOfObject, heigthOfObject = takenPicture.shape

                    if widthOfObject > 977 or widthOfObject < 251 or heigthOfObject > 977 or heigthOfObject < 251:
                        # We have to apply this if condition because sometimes the picture bigger than camera so
                        # We have to small this picture side
                        takenPicture = cv2.resize(takenPicture, (280, 320), interpolation=cv2.INTER_AREA)
                        widthOfObject, heigthOfObject = takenPicture.shape

                    else:
                        takenPicture, widthOfObject, heigthOfObject

                    res = cv2.matchTemplate(convertToGray, takenPicture,
                                            cv2.TM_CCOEFF_NORMED)  # Apply template matching and
                    # normally , we have 6 template matching and we decision to this.

                    proficiencyOfValue = 0.8  # threshold value we can change
                    localCompareValue = np.where(res > proficiencyOfValue)

                    for parameter in zip(*localCompareValue[::-1]):
                        cv2.rectangle(display, parameter, (parameter[0] + heigthOfObject, parameter[1] + widthOfObject),
                                      (0, 255, 0), 2)

                        accuracyRate = str(res * 100)  # We try give accuracy percent . But I am not sure right result.
                        accuracyRate = accuracyRate.replace('[', '').replace(']', '')
                        # In the result give some bracket and undesirable string so we delete that
                        Write = 'Apple' + accuracyRate
                        # For strawberry we want show this name and accuracy rate
                        cv2.putText(display, Write, (parameter[0], parameter[1]),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
                    res = []  # We make empty this array

            new_Display = Camera_Set_Up(display, camera_percent)
            #we create
            cv2.imshow("Display", new_Display)

            if cv2.waitKey(25) & 0xFF == ord('q'):  # per 25 millisecond, take photo
                break  # when press the 'q' the program will be quit
        else:
            ret = False

    openTheCamera.release()
    cv2.destroyAllWindows()


Find_Strawberry(100)
