#!/user/bin/env python3

"""

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

def drawBlade(deg, num):
    blades = []
    for ori in range(0, 360, 360//num):
        blade = create_blade(deg, ori)
        blade.setPos([0, 0])
        blades.append(blade)
    return blades

def animateBlade(blade, speed):
    blade.setOri(speed, operation="+")
    blade.draw()

def mainLoop(degStop, numStop, degMove, numMove, filename):
    finish = False

    stationary_blades = drawBlade(degStop, numStop)
    moving_blades = drawBlade(degMove, numMove)

    while finish is not True:
        for blade in stationary_blades:
            animateBlade(blade, speed=0)
        for blade in moving_blades:
            animateBlade(blade, speed=1)
        win.flip()

        if event.getKeys(keyList=['escape']): #escape to end
            finish = True

def demoLoop(degStop, numStop, degMove, numMove, filename):
    """ creates a gif file from screenshots (png files)
    of one entire cycle (360 degrees)"""

    stationary_blades = drawBlade(degStop, numStop)
    moving_blades = drawBlade(degMove, numMove)

    frame = 0
    for frame in range(0, 719): #loops two cycles
        frame +=1
        for blade in stationary_blades:
            animateBlade(blade, speed=0)
        for blade in moving_blades:
            animateBlade(blade, speed=1)
        win.flip()
        win.getMovieFrame() #takes a screenshot of each frame

    #creates gif file out of screenshots
    print("creating gif file")
    create_png_folder()
    win.saveMovieFrames("png/stimuli.png")
    create_gif(filename) #infinite loop gif
    print("finished")

#mainLoop(degStop=30, numStop = 6, degMove=15, numMove = 6, filename = "")
demoLoop(degStop=30, numStop = 6, degMove=15, numMove = 6, filename = "6x6.gif")

win.close()
core.quit()
