#!/user/bin/env python3

"""
A pop out window (Psychopy) running the fan illusion on infinite loop.
Press `escape` key to the close window.
Change parameters in mainLoop.
"""

from psychopy import visual, core, event

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

def mainLoop(degStop, numStop, degMove, numMove, filename):
    finish = False
    """
    Stop: the stationary fan. Move: the moving fan.
    deg: how big the blades are
    num: how many blades per fan
    filename: the name of the gif file
    """
    #create the two fans
    stationary_blades = createBlade(degStop, numStop)
    moving_blades = createBlade(degMove, numMove)

    while finish is not True:
        for blade in stationary_blades:
            animateBlade(blade, speed=0) #stationary
        for blade in moving_blades:
            animateBlade(blade, speed=1) #1 degree per frame
        win.flip()

        if event.getKeys(keyList=['escape']):
            finish = True

mainLoop(degStop=30, numStop = 6, degMove=15, numMove = 6, filename = "")

win.close()
core.quit()
