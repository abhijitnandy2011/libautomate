# Copyright (C) 2021 - Abhijit Nandy


# Lib

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
        # pyautogui.click(strImagePath)
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
    # Final img NOT found
    if imgLocation is None: 
        return -1 # error!
    # Final img has been found
    center = pyautogui.center(imgLocation)
    pyautogui.click(center.x, center.y)
    return idx-1   # return idx of last img that was found, which is also the last img in this case

    

def zeroInByImgInListSeqAndClick(listImgsInListPaths):
    idx = 1
    screenSize = pyautogui.size()
    # print(screenSize)
    imgLocation = None
    #Start with whole screen search    
    regionRect = (0, 0, screenSize[0], screenSize[1])
    # Go through each list in listImgsInListPaths
    # Each entry is also a list containing possibilities for that level
    for listImgPaths in listImgsInListPaths:        
        imgLocation = None
        possibsIdx = 1
        # Go through the possibilities for this level
        for imgPath in listImgPaths:
            imgLocation = pyautogui.locateOnScreen(imgPath, region=regionRect)
            # print(idx, possibsIdx, imgLocation, regionRect)
            if imgLocation is None:
                # Try next img in list for this level
                continue
            regionRect = (imgLocation.left, imgLocation.top, imgLocation.width, imgLocation.height)
            possibsIdx += 1
        # None of the possibilities were found at this level, abort
        if imgLocation is None:
            return idx-1    # return idx of last level that had an img found        
    # Final img NOT found
    if imgLocation is None:
        return -1 # error!
    # Final img has been found
    center = pyautogui.center(imgLocation)
    pyautogui.click(center.x, center.y)
    return idx-1   # return idx of last img that was found, which is also the last img in this case
    


def findImgInListAndClick(listImgPaths):
    idx = 1
    for imgPath in listImgPaths:
        if findImgAndClick(imgPath):
            return idx
        idx += 1
    return -1


def findImgInListClickType(listImgPaths, strTypeThis, interval=0.25):
    idx = findImgInListAndClick(listImgPaths)
    if idx > 0:
        # Can type now
        pyautogui.write(strTypeThis, interval) 
        return idx
    return -1
        
    
    