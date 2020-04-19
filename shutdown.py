import cv2
import numpy as np
import pyautogui as pg
########## All The work is done by taking the screenshorts, converting them in to gray image and then finding the required items in it. ##########
sizeofScreen = pg.size()            # Getting the size of current screen
locationsOfStartButton = [(sizeofScreen[0], 1), (1, 1), (1, sizeofScreen[1]), (sizeofScreen[0]-2, sizeofScreen[1]-2)]   # Location of all 4 corners for finding the start button.
pathOfScreenshort = 'screenshort.png'  # A screenshort has to be taken whose path should be justified here.

threshold = 0.8


def Close():             #--------DONE FOR WHITE-------------------

    template = cv2.imread('whiteClose.png', 0)
    template1 = cv2.imread('blackClose.png', 0)

    while True:
        pg.screenshot(pathOfScreenshort)
        img = cv2.imread(pathOfScreenshort, 0)

        pg.moveTo(sizeofScreen[0] / 2, sizeofScreen[1] / 2)

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)                                        # Getting the locations of white colored close buttons on the screen.

        res1 = cv2.matchTemplate(img, template1, cv2.TM_CCOEFF_NORMED)
        loc1 = np.where(res1 >= threshold)                                      # Getting the locations of black close buttons.

        for i in range(len(loc[0])):                                            # Going and closing the windows having the white close button....
            pg.moveTo(loc[1][i], loc[0][i])
            pg.moveRel(10,10,1)
            pg.click()

        for i in range(len(loc1[0])):                                           # Going and closing the windows having the black close button...
            pg.moveTo(loc1[1][i], loc1[0][i])
            pg.moveRel(17, 10)
            pg.click()

        if (len(loc[0]) == 0) and (len(loc1[0]) == 0):
            break


def findingTheStartButton():               #----------------DONE FOR WHITE---------------------
    loc = 0
    loc1 = 0
    for i in range(len(locationsOfStartButton)):
        pg.moveTo(locationsOfStartButton[i])                         # Finding the start button.
        pg.sleep(2)
        pg.screenshot(pathOfScreenshort)
        temp = cv2.imread('windowsButton.png', 0)
        whitetemp = cv2.imread('whiteWindowButton.png',0)
        img = cv2.imread(pathOfScreenshort, 0)
        res = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
        whiteres = cv2.matchTemplate(img, whitetemp, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)                                        # Getting the location of start button.
        whiteloc = np.where(whiteres >=threshold)
        if(len(whiteloc[0]))!=0:                                                # Finding Task viewer for white mode.....
            whitetem = cv2.imread('whiteFlag.png',0)
            whiteimg = cv2.imread(pathOfScreenshort,0)
            whiteres = cv2.matchTemplate(whiteimg, whitetem, cv2.TM_CCOEFF_NORMED)
            loc1 = np.where(whiteres >= threshold)                              # Getting loc of white task viewer.
            for j in range(len(loc1[0])):
                pg.moveTo(loc1[1][j], loc1[0][j])                               # Going to task viewer.
            pg.moveRel(0,10)
            return whiteloc, loc1
        if len(loc[0]) != 0:
            tem = cv2.imread('flag.png', 0)                                     # If we get the start button Finding Task viewer.
            pg.screenshot(pathOfScreenshort)
            img = cv2.imread(pathOfScreenshort, 0)
            res = cv2.matchTemplate(img, tem, cv2.TM_CCOEFF_NORMED)
            loc1 = np.where(res >= threshold)                                   # Getting the location of task viewer.

            for j in range(len(loc1[0])):
                pg.moveTo(loc1[1][j], loc1[0][j])                            # Going to task viewer.
            pg.moveRel(0, 5)
            return loc, loc1
    


def shiftingRight():            #----------------------Done For White-----------------------------------
    template = cv2.imread('shift.png', 0)
    whitetemplate = cv2.imread('whiteShift.png',0)
    while True:
        pg.screenshot(pathOfScreenshort)                                    # Shifting right till the task viewer is gone (Taken as REFERENCE)
        img = cv2.imread(pathOfScreenshort, 0)
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        whiteres = cv2.matchTemplate(img,whitetemplate,cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        whiteloc = np.where(whiteres >= threshold)
        print('loc',loc[0])
        print('whiteLoc',whiteloc[0])
        if len(whiteloc[0]!=0):
            pg.moveRel(4,0)
        elif len(loc[0] != 0):
            pg.moveRel(4, 0)
        else:
            break
    
    pg.moveRel(4, 20)
    template = cv2.imread('standingLines.png', 0)               # Finding the standing lines (Taken as REFERENCE)
    whiteTemplate = cv2.imread('whiteStandingLines.png',0)
    pg.screenshot(pathOfScreenshort)
    img = cv2.imread(pathOfScreenshort, 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    whiteRes = cv2.matchTemplate(img, whiteTemplate, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    whiteLoc = np.where(whiteRes >= threshold)
    if len(whiteLoc[0]) != 0:
        for i in range(len(whiteLoc[0])):
            pg.moveTo(whiteLoc[1][i], whiteLoc[0][i])
        pg.moveRel(35, 5, 1)
    if len(loc[0]) != 0:
        for i in range(len(loc[0])):
            pg.moveTo(loc[1][i], loc[0][i])
        pg.moveRel(35, 5, 1)

def shiftingDown():                     #-----------------------Done for white------------------- 
    template = cv2.imread('shift.png', 0)
    whiteTemplate = cv2.imread('whiteShift.png', 0)
    while True:
        pg.screenshot(pathOfScreenshort)
        img = cv2.imread(pathOfScreenshort, 0)
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        whiteRes = cv2.matchTemplate(img, whiteTemplate, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        whiteLoc = np.where(whiteRes >= threshold)
        if len(loc[0] != 0):
            pg.moveRel(0, 4)
        elif len(whiteLoc[0] != 0):
            pg.moveRel(0, 4)
        else:
            break
    pg.moveRel(0, 4)
    template = cv2.imread('sleepingWithbox.png', 0)                    # Finding the sleeping lines (Taken as REFERENCE)
    whiteTemplate = cv2.imread('whiteSleepingWithBox.png', 0)
    pg.screenshot(pathOfScreenshort)
    img = cv2.imread(pathOfScreenshort, 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    whiteRes = cv2.matchTemplate(img, whiteTemplate, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    whiteLoc = np.where(whiteRes >= threshold)
    if len(loc[0]) != 0:
        for i in range(len(loc[0])):
            pg.moveTo(loc[1][i], loc[0][i])
        pg.moveRel(10, 70)
    if len(whiteLoc[0]) != 0:
        for i in range(len(whiteLoc[0])):
            pg.moveTo(whiteLoc[1][i], whiteLoc[0][i])
        pg.moveRel(10, 70)



Close()
loc, loc1 = findingTheStartButton()

if abs(loc1[1][0] - loc[1][0]) > 100:                                       # Finding wether the taskbar is horizontal or vertical.
    count = 0                                                               # For horizontal taskbar.
    close = 0
    pos = 0
    shiftingRight()
    template = cv2.imread("closeTheProgram.png", 0)
    whiteTemplate = cv2.imread('whiteCloseTheProgram.png', 0)
    template1 = cv2.imread("unpin.png", 0)
    whiteTemplate1 = cv2.imread('whiteUnpin.png', 0)
    template2 = cv2.imread("taskbarSetting.png", 0)
    whiteTemplate2 = cv2.imread('whiteTaskbarSetting.png', 0)

    while True:
        oldPos = pos
        pos = pg.position()                                                   # Getting current position of mouse pointer.
        pg.rightClick()

        pg.screenshot(pathOfScreenshort)
        img = cv2.imread(pathOfScreenshort, 0)

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        whiteRes = cv2.matchTemplate(img, whiteTemplate, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)                                      # Finding the location of close the program button.
        whiteLoc = np.where(whiteRes >= threshold)

        res1 = cv2.matchTemplate(img, template1, cv2.TM_CCOEFF_NORMED)
        whiteRes1 = cv2.matchTemplate(img, whiteTemplate1, cv2.TM_CCOEFF_NORMED)
        loc1 = np.where(res1 >= threshold)                                    # Finding the location of unpin the program button.
        whiteLoc1 = np.where(whiteRes1 >= threshold)
        
        res2 = cv2.matchTemplate(img, template2, cv2.TM_CCOEFF_NORMED)
        whiteRes2 = cv2.matchTemplate(img, whiteTemplate2, cv2.TM_CCOEFF_NORMED)
        loc2 = np.where(res2 >= threshold)                                    # Finding the location of taskbar setting button.
        whiteLoc2 = np.where(whiteRes2 >= threshold)
        #=======================================================================================================================================
        if (len(loc[0]) != 0) and (len(loc1[0] != 0)):                        # If we have both unpin and close button then click on the close button and make count = 0.
            for i in range(len(loc[0])):
                pg.moveTo(loc[1][i], loc[0][i])
            pg.click()
            if pos == oldPos:
                close += 1
                if close == 10:
                    Close()
                    close = 0
                    findingTheStartButton()
                    shiftingRight()
            count = 0
            pg.moveTo(pos)

        elif len(loc[0]) != 0:                                                # If we have only close button then just close the program and make count = 0.
            for i in range(len(loc[0])):
                pg.moveTo(loc[1][i], loc[0][i])
            pg.click()
            if pos == oldPos:
                close += 1
                if close == 10:
                    Close()
                    close = 0
                    findingTheStartButton()
                    shiftingRight()
            count = 0
            pg.moveTo(pos)

        elif len(loc1[0]) != 0:                                                                 # If we have only unpin button then just move on...
            count = 0
            pg.moveRel(4, 0)

        if len(loc2[0]) != 0:                                                 # If we are having the taskbar setting button increment the count by 1.
            pg.moveRel(4, 0)
            count += 1
            if count == 10:                                                   # If we get taskbar setting for more than 10 times then we assume that all the programs running in the background are closed.
                pg.click()
                break

    pg.screenshot(pathOfScreenshort)
    template = cv2.imread('windowsButton.png', 0)
    img = cv2.imread(pathOfScreenshort, 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)  # Getting the position of start button
    for j in range(len(loc[0])):
        pg.moveTo(loc[1][j], loc[0][j])
    pg.click()
    pg.sleep(1)

    template = cv2.imread('settingPower.png', 0)
    pg.screenshot(pathOfScreenshort)
    img = cv2.imread(pathOfScreenshort, 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    for i in range(len(loc[0])):
        pg.moveTo(loc[1][i], loc[0][i])
    pg.moveRel(10, 55)
    pg.click()  # Clicking the poweroff button
    pg.sleep(1)
    template = cv2.imread('powerOffButton.png', 0)
    pg.screenshot(pathOfScreenshort)
    img = cv2.imread(pathOfScreenshort, 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for j in range(len(loc[0])):
        pg.moveTo(loc[1][j], loc[0][j], 1)

    pg.moveRel(20, 10)
    pg.click()
    pg.click()

else:                                                                       # For vertical taskbar.
    close = 0
    count = 0                                                               # Same instructions as above.
    pos = 0
    shiftingDown()
    template = cv2.imread("closeTheProgram.png", 0)
    template1 = cv2.imread("unpin.png", 0)
    template2 = cv2.imread("taskbarSetting.png", 0)

    while True:
        oldPos = pos
        pos = pg.position()
        pg.rightClick()

        pg.screenshot(pathOfScreenshort)
        img = cv2.imread(pathOfScreenshort, 0)

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        res1 = cv2.matchTemplate(img, template1, cv2.TM_CCOEFF_NORMED)
        loc1 = np.where(res1 >= threshold)

        res2 = cv2.matchTemplate(img, template2, cv2.TM_CCOEFF_NORMED)
        loc2 = np.where(res2 >= threshold)

        if (len(loc[0]) != 0) and (len(loc1[0] != 0)):
            for i in range(len(loc[0])):
                pg.moveTo(loc[1][i], loc[0][i])
            pg.click()
            if pos == oldPos:
                close += 1
                if close == 10:
                    Close()
                    close = 0
                    findingTheStartButton()
                    shiftingDown()
            count = 0
            pg.moveTo(pos)

        elif len(loc[0]) != 0:
            for i in range(len(loc[0])):
                pg.moveTo(loc[1][i], loc[0][i])
            pg.click()
            if pos == oldPos:
                close += 1
                if close == 10:
                    Close()
                    close = 0
                    findingTheStartButton()
                    shiftingDown()
            count = 0
            pg.moveTo(pos)

        elif len(loc1[0]) != 0:
            count = 0
            pg.moveRel(0, 4)

        if len(loc2[0]) != 0:
            pg.moveRel(0, 4)
            count += 1
            if count == 8:
                pg.click()
                break

    pg.screenshot(pathOfScreenshort)
    template = cv2.imread('windowsButton.png', 0)
    img = cv2.imread(pathOfScreenshort, 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)  # Getting the position of start button
    for j in range(len(loc[0])):
        pg.moveTo(loc[1][j], loc[0][j])
    pg.click()
    pg.sleep(1)

    template = cv2.imread('settingPower.png', 0)
    pg.screenshot(pathOfScreenshort)
    img = cv2.imread(pathOfScreenshort, 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    for i in range(len(loc[0])):
        pg.moveTo(loc[1][i], loc[0][i])
    pg.moveRel(10, 55)
    pg.click()                                                          # Clicking the poweroff button
    pg.sleep(1)
    template = cv2.imread('powerOffButton.png', 0)
    pg.screenshot(pathOfScreenshort)
    img = cv2.imread(pathOfScreenshort, 0)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for j in range(len(loc[0])):
        pg.moveTo(loc[1][j], loc[0][j])

    pg.moveRel(20, 10)
    pg.click()
    pg.click()
