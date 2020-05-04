#!/user/bin/env python3

"""
Creates gif files of fan illusion demos.
Change parameters in demoLoop
"""

from psychopy import visual, core, event
from gifMethods import create_png_folder, create_gif

win = visual.Window([300, 300], color = "white")

def create_blade(degree, ori):
    return visual.RadialStim(
    win = win,
    color= 1,
    visibleWedge= [0,degree],
    radialCycles= 0,
    angularCycles= 90//degree,
    ori = ori,
    size = 1.5
    )

def createBlade(deg, num):
    blades = []
    for ori in range(0, 360, 360//num):
        blade = create_blade(deg, ori)
        blade.setPos([0, 0])
        blades.append(blade)
    return blades

def animateBlade(blade, speed):
    blade.setOri(speed, operation="+")
    blade.draw()

def demoLoop(degStop, numStop, degMove, numMove, filename):
    """
    Stop: the stationary fan.
    Move: the moving fan.
    deg: how big the blades are
    num: how many blades per fan
    filename: the name of the gif file
    """
    #create the two fans
    stationary_blades = createlade(degStop, numStop)
    moving_blades = createBlade(degMove, numMove)

    frame = 0
    for frame in range(0, 719): #loops two cycles
        frame +=1
        for blade in stationary_blades:
            animateBlade(blade, speed=0) #stationary
        for blade in moving_blades:
            animateBlade(blade, speed=1) #one degree per frame
        win.flip()
        win.getMovieFrame() #takes a screenshot of each frame

    #creates infinite loop gif file out of screenshots
    print("creating gif file")
    create_png_folder()
    win.saveMovieFrames("png/stimuli.png") #load png files to folder
    create_gif(filename)
    print("finished")

demoLoop(degStop=30, numStop = 6, degMove=15, numMove = 1, filename = "xxx.gif")

win.close()
core.quit()
