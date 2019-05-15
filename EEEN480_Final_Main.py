import cv2  # Main Library
import numpy as np  # means matrix folder
from os import walk  # For find the folder we are using this
from os.path import join

def Find_Fruits(camera_percent):  # General function we will call this function in main folder.
    # We are creating the function with 'def'
    openTheCamera = cv2.VideoCapture(0)  # we open the camera

    # 0 => In computer, it uses default camera such as,laptop camera
    # 1 => Out computer, when we connect with usb we use with that way(EXTENTİON PART)
    def Camera_Set_Up(display, percent):
        camera_width = int(display.shape[1] * percent / 100)  # we are resize the width of camera with percently
        camera_heigth = int(display.shape[0] * percent / 100)  # we are resize the heigth of camera with percently

        dimension = (camera_width, camera_heigth)  # we dont do anything just for return we collect the result

        return cv2.resize(display, dimension, interpolation=cv2.INTER_AREA)  # we have to use this library for all

    # size chancing

    while True:  # we enter the infinitive loop

        if openTheCamera.isOpened():  # security for coming respond from camera
            ret, display = openTheCamera.read()

            convertToGray = cv2.cvtColor(display,
                                         cv2.COLOR_BGR2GRAY)  # We convert to gray who is coming the camera data

            for dirpath, dirnames, filenames in walk(
                    'cherry'):  # we are taking folder directly in source code folder

                for size in filenames:  # in python we are looping with elemans so it will give directly eleman names.
                    # such as cherry1.jpg
                    if size == filenames[len(filenames)-1]:
                        break
                    else:
                        print(size)
                        takenPicture = cv2.imread('{}'.format(size), 0)  # This eleman has to be 'cherry3.jpg'.
                        # So we have to change to format for all picture
                        # 0 means you make be gray color

                        widthOfObject, heigthOfObject = takenPicture.shape

                        if widthOfObject > 200 or widthOfObject < 80 or heigthOfObject > 200 or heigthOfObject < 80:
                            # We have to apply this if condition because sometimes the picture bigger than camera so
                            # We have to small this picture side
                            takenPicture = cv2.resize(takenPicture, (120, 110), interpolation=cv2.INTER_AREA)
                            widthOfObject, heigthOfObject = takenPicture.shape

                        else:
                            takenPicture, widthOfObject, heigthOfObject

                        res = cv2.matchTemplate(convertToGray, takenPicture,
                                                cv2.TM_CCOEFF_NORMED)  # Apply template matching and
                        # normally , we have 6 template matching and we decision to this.

                        proficiencyOfValue = 0.7  # threshold value we can change
                        localCompareValue = np.where(res > proficiencyOfValue)
                        # We are comparing the constant value and chancable values
                        # According to this matching result, we decide the acceptable or not
                        if localCompareValue:
                            for parameter in zip(*localCompareValue[::-1]):
                                cv2.rectangle(display, parameter,
                                              (parameter[0] + heigthOfObject, parameter[1] + widthOfObject),
                                              (0, 255, 0), 2)

                                accuracyRate = str(
                                    res * 100)  # We try give accuracy percent . But I am not sure right result.
                                accuracyRate = accuracyRate.replace('[', '').replace(']', '')
                                # In the result give some bracket and undesirable string so we delete that
                                Write = 'Cherry' + accuracyRate
                                # For cherry we want show this name and accuracy rate
                                cv2.putText(display, Write, (parameter[0], parameter[1]),
                                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
                            res = []  # We make empty this array

            for dirpath, dirnames, filenames in walk(
                    'lemon'):  # we are taking folder directly in source code folder

                for size in filenames:  # in python we are looping with elemans so it will give directly eleman names.
                    # such as lemon1.jpg
                    takenPicture = cv2.imread('{}'.format(join(dirpath, size)), 0)  # This eleman has to be 'lemon3.jpg'.
                    # So we have to changeto format for all picture
                    # 0 means you make be gray color

                    widthOfObject, heigthOfObject = takenPicture.shape

                    if widthOfObject > 230 or widthOfObject < 260 or heigthOfObject > 250 or heigthOfObject < 320:
                        # We have to apply this if condition because sometimes the picture bigger than camera so
                        # We have to small this picture side
                        takenPicture = cv2.resize(takenPicture, (250, 300), interpolation=cv2.INTER_AREA)
                        widthOfObject, heigthOfObject = takenPicture.shape

                    else:
                        takenPicture, widthOfObject, heigthOfObject

                    res = cv2.matchTemplate(convertToGray, takenPicture,
                                            cv2.TM_CCOEFF_NORMED)  # Apply template matching and
                    # normally , we have 6 template matching and we decision to this.

                    proficiencyOfValue = 0.7  # threshold value we can change
                    localCompareValue = np.where(res > proficiencyOfValue)

                    for parameter in zip(*localCompareValue[::-1]):
                        cv2.rectangle(display, parameter, (parameter[0] + heigthOfObject, parameter[1] + widthOfObject),
                                      (0, 255, 0), 2)

                        accuracyRate = str(res * 100)  # We try give accuracy percent . But I am not sure right result.
                        accuracyRate = accuracyRate.replace('[', '').replace(']', '')
                        # In the result give some bracket and undesirable string so we delete that
                        Write = 'Lemon' + accuracyRate
                        # For lemon we want show this name and accuracy rate
                        cv2.putText(display, Write, (parameter[0], parameter[1]),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
                    res = []  # We make empty this array
            for dirpath, dirnames, filenames in walk(
                    'banana'):  # we are taking folder directly in source code folder

                for size in filenames:  # in python we are looping with elemans so it will give directly eleman names.
                    # such as lemon3.jpg
                    takenPicture = cv2.imread('{}'.format(join(dirpath, size)), 0)  # This eleman has to be 'lemon3.jpg'.
                    # So we have to changeto format for all picture
                    # 0 means you make be gray color

                    widthOfObject, heigthOfObject = takenPicture.shape

                    if widthOfObject > 400 or widthOfObject < 410 or heigthOfObject > 100 or heigthOfObject < 150:
                        # We have to apply this if condition because sometimes the picture bigger than camera so
                        # We have to small this picture side
                        takenPicture = cv2.resize(takenPicture, (600, 200), interpolation=cv2.INTER_AREA)
                        widthOfObject, heigthOfObject = takenPicture.shape

                    else:
                        takenPicture, widthOfObject, heigthOfObject

                    res = cv2.matchTemplate(convertToGray, takenPicture,
                                            cv2.TM_CCOEFF_NORMED)  # Apply template matching and
                    # normally , we have 6 template matching and we decision to this.

                    proficiencyOfValue = 0.7  # threshold value we can change
                    localCompareValue = np.where(res > proficiencyOfValue)

                    for parameter in zip(*localCompareValue[::-1]):
                        cv2.rectangle(display, parameter,
                                      (parameter[0] + heigthOfObject, parameter[1] + widthOfObject),
                                      (0, 255, 0), 2)

                        accuracyRate = str(
                            res * 100)  # We try give accuracy percent . But I am not sure right result.
                        accuracyRate = accuracyRate.replace('[', '').replace(']', '')
                        # In the result give some bracket and undesirable string so we delete that
                        Write = 'Banana' + accuracyRate
                        # For banana we want show this name and accuracy rate
                        cv2.putText(display, Write, (parameter[0], parameter[1]),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
                    res = []  # We make empty this array

            for dirpath, dirnames, filenames in walk(
                    'apple'):  # we are taking folder directly in source code folder

                for size in filenames:  # in python we are looping with elemans so it will give directly eleman names.
                    # such as lemon3.jpg
                    takenPicture = cv2.imread('{}'.format(size), 0)  # This eleman has to be 'lemon3.jpg'.
                    # So we have to changeto format for all picture
                    # 0 means you make be gray color

                    widthOfObject, heigthOfObject = takenPicture.shape

                    if widthOfObject > 200 or widthOfObject < 250 or heigthOfObject > 220 or heigthOfObject < 270:
                        # We have to apply this if condition because sometimes the picture bigger than camera so
                        # We have to small this picture side
                        takenPicture = cv2.resize(takenPicture, (250, 260), interpolation=cv2.INTER_AREA)
                        widthOfObject, heigthOfObject = takenPicture.shape

                    else:
                        takenPicture, widthOfObject, heigthOfObject

                    res = cv2.matchTemplate(convertToGray, takenPicture,
                                            cv2.TM_CCOEFF_NORMED)  # Apply template matching and
                    # normally , we have 6 template matching and we decision to this.

                    proficiencyOfValue = 0.7  # threshold value we can change
                    localCompareValue = np.where(res > proficiencyOfValue)

                    for parameter in zip(*localCompareValue[::-1]):
                        cv2.rectangle(display, parameter,
                                      (parameter[0] + heigthOfObject, parameter[1] + widthOfObject),
                                      (0, 255, 0), 2)

                        accuracyRate = str(
                            res * 100)  # We try give accuracy percent . But I am not sure right result.
                        accuracyRate = accuracyRate.replace('[', '').replace(']', '')
                        # In the result give some bracket and undesirable string so we delete that
                        Write = 'Apple' + accuracyRate
                        # For banana we want show this name and accuracy rate
                        cv2.putText(display, Write, (parameter[0], parameter[1]),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
                    res = []  # We make empty this array


            new_Display = Camera_Set_Up(display, camera_percent)
            # we create new camera dimension
            cv2.imshow("Display", new_Display)

            if cv2.waitKey(50) & 0xFF == ord('q'):  # per 25 millisecond, take photo
                break  # when press the 'q' the program will quit
        else:
            ret = False

    openTheCamera.release()
    cv2.destroyAllWindows()


Find_Fruits(100)