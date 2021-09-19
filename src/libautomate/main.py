# Library main

import io
from time import sleep
import pyautogui

#----------------------------------------------------------------------------


def findImgAndClick(strImagePath):
    imgLocation = pyautogui.locateOnScreen(strImagePath)
    if imgLocation is None:
        return False
    else:
        center = pyautogui.center(imgLocation)
        pyautogui.click(center.x, center.y)
    return True
    

def zeroInByImgSeqAndClick(listImgPaths):
    idx = 1
    screenSize = pyautogui.size()
    # print(screenSize)
    imgLocation = None
    regionRect = (0, 0, screenSize[0], screenSize[1])
    for imgPath in listImgPaths:
        imgLocation = pyautogui.locateOnScreen(imgPath, region=regionRect)
        print(idx, imgLocation, regionRect)
        if imgLocation is None:        
            return idx-1    # return idx of last img that was found        
        regionRect = (imgLocation.left, imgLocation.top, imgLocation.width, imgLocation.height)
        idx += 1
    # Final img has been found
    if imgLocation is not None: 
        center = pyautogui.center(imgLocation)
        pyautogui.click(center.x, center.y)
        return idx-1   # return idx of last img that was found, which is also the last img in this case
    return -1 # error!


def findImgInListAndClick(listImgPaths):
    idx = 1
    for imgPath in listImgPaths:
        if findImgAndClick(imgPath):
            return idx
        idx += 1
    return -1    
    