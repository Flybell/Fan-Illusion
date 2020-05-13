#!/user/bin/env python3

"""
The fan illusion
Parameters: define stationary fan, moving fan

SYNOPSIS
========
::
    python3 Fan_Illusion.py

DESCRIPTION
===========
A pop out window (Psychopy) will run the fan illusion on infinite loop.
Press `escape` key to close the window and end the program.

"""
from psychopy import visual, core, event
from gifMethods import create_png_folder, create_gif


def blade_object(degree, ori):
    """each fan is made up of wedges or "blades"
       this function creates a single blade based on its size (degree) and orientation"""
    return visual.RadialStim(
    win = win,
    color= 1,
    visibleWedge= [0,degree],
    radialCycles= 0,
    angularCycles= 90//degree,
    ori = ori,
    size = 1.5
    )

def createFan_custom(deg, num, speed):
    """output: a list of blades that constitute a fan"""
    created_fan = []
    for ori in range(0,num):
        created_fan.append((blade_object(deg, ori*2*deg), speed))
    return created_fan

def createFan_full(deg, num, speed):
    """input: a tuple (deg, num, speed)
       output: a list of (blade object, speed) tuples that constitute each fan"""
    created_fan = []
    if deg*num <360:
        for ori in range(0, 360, 360//num): #evenly distribute blades
            created_fan.append((blade_object(deg, ori), speed))
        return created_fan
    else:
        raise ValueError("Cannot create fan")

def animateBlade(blade, speed):
    """moves each blade with speed (degree per frame)"""
    blade.setOri(speed, operation="+")
    blade.draw()

def Valid(deg, num):
    """ checks whether a fan is possible to make
        if the number of blades x size (in degrees) > 360, not possible"""
    if deg*num >360:
        print("That is an impossible fan. Try again.")
        return False
    else:
        return True

def mainLoop(filename):
    """infinitely loops the fans
       input: list of fan tuples (deg, num, speed)"""
    finish = False
    #create fans
    fans = []
    fans.append(createFan_custom(15, 2, 1))
    fans.append(createFan_full(30, 6, 0))
#    fans.append(createFan_full((7.5, 24, 1)))
#    fans = [createFan(fan) for fan in fan_list]
    #animate fans
    frame = 0
    for frame in range(0, 719): #loops two cycles
        frame +=1
        for fan in fans:
            for blade in fan:
                animateBlade(blade[0], speed=blade[1])
        win.flip()
        win.getMovieFrame() #takes a screenshot of each frame

    #creates infinite loop gif file out of png screenshots
    #higher resolution than directly outputing gif file
    print("creating gif file")
    create_png_folder()
    win.saveMovieFrames("png/stimuli.png") #load png files to folder
    create_gif(filename)
    print("finished")

win = visual.Window([300, 300], color = "white")
mainLoop("weak_mc.gif")


win.close()
core.quit()
