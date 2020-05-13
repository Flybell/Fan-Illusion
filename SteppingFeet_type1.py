import math, numpy, random #handy system and math functions
from psychopy import core, event, visual, gui #these are the psychopy modules
from gifMethods import create_png_folder, create_gif


myWin = visual.Window(color='white', units='pix', size=[800,800], allowGUI=False, fullscr=False)#creates a window
myClock = core.Clock() #this creates and starts a clock which we can later read

#create shapes
movingFoot1 = visual.Rect(myWin, width=20, height=400, fillColor="black", lineColor=None)
movingFoot2 = visual.Rect(myWin, width=20, height=400, fillColor="black", lineColor=None)
movingFoot3 = visual.Rect(myWin, width=20, height=400, fillColor="black", lineColor=None)
#movingFoot2 = visual.Rect(myWin, width=80, height=400, fillColor="white", lineColor=None)
verticalBar = visual.Rect(myWin, width=20, height=400, fillColor='black', lineColor=None)

#create a bar for the user to control speed and direction
"""myScaleSpeed = visual.RatingScale(myWin, pos=[0, -360], low=1, high=10,  textSize=0.5, lineColor='black',  tickHeight=False, scale=None, showAccept=False, singleClick=True)
informationSpeed=visual.TextStim(myWin, pos=[0,-385], text='', height=18, color='black')
myScaleTransparent = visual.RatingScale(myWin, pos=[0, -255], low=0, high=100,  textSize=0.5, lineColor='black',  tickHeight=False, scale=None, showAccept=False, singleClick=True)
informationTransparent=visual.TextStim(myWin, pos=[0,-280], text='', height=18, color='black')"""

#title=visual.TextStim(myWin, pos=[0,305], text='Stepping Feet Illusion', height=24, color='green')

# draw n vertical bars, half black half white
def drawBars(width, nBars):

    left = - width * (nBars - 1) //  2 #previous version neglected to change the float to integer by // instead of /
    for x in range(left, -left, width*2):
            verticalBar.setPos([x, 0])
            verticalBar.draw()

# move the rectangles
def animateSteps(speed):

    movingFoot1.setPos([speed, 0], operation="+")
    movingFoot2.setPos([speed, 0], operation="+")
#    movingFoot3.setPos([speed, 0], operation="+")

#    movingFoot2.setPos([speed, 0], operation="+")

    movingFoot1.draw()
    movingFoot2.draw()
#    movingFoot3.draw()
#    movingFoot4.draw()
#    movingFoot2.draw()

# the main loop
def mainLoop(width=40, nBars=20, speed=1.5):

    finished = False
    verticalBar.setWidth(width)
    xMargin = width * nBars // 2 - width
    movingFoot1.setPos([-xMargin, 0])
    movingFoot2.setPos([-xMargin+40, 0])
#    movingFoot3.setPos([-xMargin+40, 0])

#    movingFoot2.setPos([-xMargin, -50])

    while not finished:

        drawBars(width, nBars)
        animateSteps(speed)
        #move back and forth
        if movingFoot1.pos[0] >xMargin or movingFoot1.pos[0] < -xMargin:
            speed = - speed
#        title.draw()
#        myScaleSpeed.draw()
#        informationSpeed.draw()

#        myScaleTransparent.draw()
#        informationTransparent.draw()
        myWin.flip()
        myWin.getMovieFrame() #takes a screenshot of each frame

#        if myScaleSpeed.noResponse ==False: #some new value has been selected with the mouse
#            speed = myScaleSpeed.getRating()
#            informationSpeed.setText(str(speed))
#            myScaleSpeed.reset()

#        if myScaleTransparent.noResponse ==False: #some new value has been selected with the mouse
#            transparent = myScaleTransparent.getRating()
#            verticalBar.setOpacity(1 - transparent / 100.)
#            informationTransparent.setText(str(transparent)+"%")
#            myScaleTransparent.reset()

        if event.getKeys(keyList=['escape']):
            finished =True

        waitUntil = myClock.getTime() + 1 / 60.   # one second divided by 60 (most monitors are 60Hz), which is 0.016
        while myClock.getTime() <waitUntil:
            pass

    #creates gif file out of screenshots
    print("creating gif file")
    create_png_folder()
    myWin.saveMovieFrames("png/stimuli.png")
    create_gif("stepping_feet_type1.gif") #infinite loop gif
    print("finished")

mainLoop() #enters the main loop
myWin.close() #closes the window
core.quit() #quits
