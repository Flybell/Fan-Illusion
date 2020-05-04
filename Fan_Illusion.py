#!/user/bin/env python3

"""

"""

from psychopy import visual, core, event
from gifMethods import create_png_folder, create_gif

win = visual.Window([600, 600], color = "white")

def create_blade(degree, ori):
    return visual.RadialStim(
    win = win,
    color= 1,
    visibleWedge= [0,degree],
    radialCycles= 0,
    angularCycles= 90//degree,
    ori = ori
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

        if event.getKeys(keyList=['escape']):
            finish = True

def demoLoop(degStop, numStop, degMove, numMove, filename):
    """ creates a gif file from screenshots (png files)
    of one entire cycle (360 degrees)"""

    stationary_blades = drawBlade(degStop, numStop)
    moving_blades = drawBlade(degMove, numMove)

    frame = 0
    for frame in range(0, 719):
        frame +=1
        for blade in stationary_blades:
            animateBlade(blade, speed=0)
        for blade in moving_blades:
            animateBlade(blade, speed=1)
        win.flip()
        win.getMovieFrame() #screenshot

    print("creating gif file")
    create_png_folder()
    win.saveMovieFrames("png/stimuli.png")
    create_gif(filename)
    print("finished")

#mainLoop(4, 1)
demoLoop(degStop=15 , numStop = 12, degMove=30, numMove = 1, filename = "radial_stepping_feet.gif")

win.close()
core.quit()
