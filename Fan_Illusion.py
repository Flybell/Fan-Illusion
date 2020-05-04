#!/user/bin/env python3

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

def mainLoop(numBig, numSmall):
    finish = False

    small_blades = drawBlade(15, numSmall)
    big_blades = drawBlade(30, numBig)

    while finish is not True:
        for blade in big_blades:
            animateBlade(blade, speed=0)
        for blade in small_blades:
            animateBlade(blade, speed= 1)

        win.flip()

        if event.getKeys(keyList=['escape']):
            finish = True

def demoLoop(num = 4):
    """ creates a gif file from screenshots (png files)
    of one entire cycle (360 degrees)"""
    small_blades = drawBlade(15, num)
    big_blades = drawBlade(30, num)

    for speed in range(0, 359):
        for blade in big_blades:
            animateBlade(blade, speed=0)
        for blade in small_blades:
            animateBlade(blade, speed = 1)
        win.flip()
        win.getMovieFrame() #screenshot

    print("creating gif file")
    create_png_folder()
    win.saveMovieFrames("png/stimuli.png")
    create_gif()

mainLoop(4, 1)
#demoLoop()

win.close()
core.quit()
