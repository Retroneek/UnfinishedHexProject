from cmu_graphics import *

###GameAssets###
app.stepsPerSecond= 60
wheel1 = Group(
Arc(200,600,1400,1400,0,60, fill='lightgrey'),
Arc(200,600,1400,1400,120,60, fill='lightgrey'), 
Arc(200,600,1400,1400,240,60, fill='lightgrey'))
wheel2= Group(
Arc(200,600,1400,1400,60,60, fill='grey'),
Arc(200,600,1400,1400,180,60, fill='grey'), 
Arc(200,600,1400,1400,300,60, fill='grey'))
gameWheel1 = Group(Arc(200,200,700,700,0,60, fill='lightgrey'),
Arc(200,200,700,700,120,60, fill='lightgrey'), 
Arc(200,200,700,700,240,60, fill='lightgrey'))
gameWheel2= Group(
Arc(200,200,700,700,60,60, fill='lightgrey'),
Arc(200,200,700,700,180,60, fill='lightgrey'), 
Arc(200,200,700,700,300,60, fill='lightgrey'))
gameWheel1.visible = False
gameWheel2.visible = False
speedUp = Label(0,200,20, visible = False)
hexagonestCChangeCounter = Label(0,200,0, visible = False)
sideChangeCounter = Label(0,200,100)
PlayerStatus=Label('move', 200,100, visible=False)
#track= Sound('https://www.youtube.com/watch?v=jigRSeRYMzA')

cursorFunction = Line(135,200,265,200, visible = False)
gameCursor = RegularPolygon( 265, 200, 5, 3, rotateAngle = 90, fill='orangeRed',visible=False)

hexagon = Group(Rect(0,50,400,75),
    Label('HEXAGON', 150, 70, bold=True, size=35, fill=rgb(250,125,50)), 
    Label('DIFFICULTY: HARD', 200,100,bold=True,size=20,fill='grey'), visible = False)
hexagoner = Group(Rect(-10,50,420,75, border=rgb(0,245,145), borderWidth = 2),
    Label('HEXAGONER', 175, 70, bold=True, size=35, fill=rgb(0,245,145)), 
    Label('DIFFICULTY: HARDER', 200,100,bold=True,size=20,fill='grey'), visible = False)
hexagonest = Group(Rect(0,50,400,75), 
    Label('DIFFICULTY: HARDEST', 200,100,bold=True,size=20,fill='grey'), visible = False)
hexagonestTitleChange =  Label('HEXAGONEST', 185, 70, bold=True, size=35, fill=rgb(0,255,0), visible = False)
hyperhexagon = Group(Rect(0,50,400,75),
    Label('HEXAGON', 150, 70, bold=True, size=35, fill=rgb(50,125,255)),Polygon(190,50,175,25,400,25,400,50), 
    Label('DIFFICULTY: HARDESTER', 200,100,bold=True,size=20,fill='grey'), Label('HYPER MODE',295, 40, size=20, fill='white', bold=True), visible = False)
hyperhexagoner = Group(Rect(0,50,400,75),
    Label('HEXAGONER', 175, 70, bold=True, size=35, fill=rgb(0,130,255)),Polygon(190,50,175,25,400,25,400,50), 
    Label('DIFFICULTY: HARDESTEST', 200,100,bold=True,size=20,fill='grey'), 
    Label('HYPER MODE',295, 40, size=20, fill='white', bold=True), visible = False)
hyperhexagonest = Group(Rect(0,50,400,75), Label('HEXAGONEST', 185, 70, bold=True, size=35, fill='white'), Polygon(190,50,175,25,400,25,400,50), Label('HYPER MODE',295, 40, size=20, fill='white', bold=True), 
    Label('DIFFICULTY: HARDESTESTEST', 200,100,bold=True,size=20,fill='grey'), visible = False)
    
BadBorder=RegularPolygon(200,200,400,6,rotateAngle=30, fill=None, border='black',  borderWidth = 30,visible=False)
BadBorder2=RegularPolygon(200,200,392,6,rotateAngle=30, fill=None, border=(gameCursor.fill),  borderWidth = 20,visible=False)


WEtop = Arc(200,200,600,600,370,60, fill=gameWheel1.fill, visible = False)
WEbottom = Arc(200,200,600,600,150,60, fill=gameWheel2.fill, visible = False)

objectSpawn = Label(1,200,50, visible = False)
playhex=RegularPolygon(200,200,50,6,fill='maroon',border='orangeRed',borderWidth=3,visible=False)
stageBar2 = Polygon(0,0,0,30,115,30,140,0, visible = False)
stageBar = Polygon(400,0,400,50,315,50, 290,30, 250, 30, 225,0, visible = False)
timeLogo = Label('TIME:', 280, 15, fill='white', bold = True, size = 20)
seconds1=Label(0,380,30, fill='white', bold=True, size = 20)
seconds2=Label(0,370,30, fill='white',  bold=True, size = 20)
minute1= Label(0,350,30, fill='white',  bold=True, size = 20)
minute2= Label(0,340,30, fill='white',  bold=True, size = 20)
Colon= Label(":",360,30, fill='white',  bold=True, size = 20)
counterv= Label(0,130,60, visible = False)
stageName = Label('POINT', 55, 15, fill='white', bold = True,  size = 20)
gameSelect = RegularPolygon(200,430,125,6, rotateAngle=90, visible = False, fill='maroon', border='orangeRed', borderWidth=5)
logo = Group( Label('SUPER', 100, 150, fill='white', bold=True, size=40), Label('PYTHAGON', 200, 190, fill='white', bold=True, size=50))
sAC = Label(0,30,20, visible = False)
pSTT = Group(Polygon(30,300,370,300,350,350,50,350, fill=rgb(100,100,100), border=rgb(200,200,200), borderWidth=3),Label('PRESS SPACE TO START', 200, 325, fill='white',  bold=True, size=22))
sTS = Polygon(75,200,325,200,300,240,100,240, fill='maroon', border=rgb(250,125,50), borderWidth = 2.5, visible = False)
startSpace = Label("CLICK TO START", 200,160, fill='white', bold=True, size = 20, visible = False)
sTS.centerY = 160
leftButtonShadow = Polygon(12,303,87,303,112,353,37,353,visible=False)
rightButtonShadow = Polygon(37,303,112,303,87,353,12,353,visible=False)
leftButton = Polygon(15,300,90,300,115,350,40,350, fill = 'maroon', border = 'orangeRed',visible=False)
RightButton = Polygon(40,300,115,300,90,350,15,350, fill = 'maroon', border = 'orangeRed',visible=False)
arrowsGuides = Group(Polygon(35,325, 40, 310, 55, 340),Polygon(85,335,50,335, 40, 315, 75, 315),visible=False)
arrowsGuides2 = Group(Polygon(35,325, 60, 310, 45, 340),Polygon(75,335,45,335, 55, 315, 85, 315),visible=False)
rightButtonShadow.centerX = 338
arrowsGuides.centerX = 65
RightButton.centerX = 335
gameCounter = Label(0,10,20, visible = False)
flashCounter = Label(0,20,20, visible = False)
levelCounter= Label(0,330,20, visible = False)
playhexCounter= Label(0,400,20, visible = False)
gameDifficulty = Label(0,200,40, visible = False)
spaceCounter= Label(0,40,20, visible = False)
arrowsGuides2.rotateAngle = 180
arrowsGuides2.centerX = 335
speedlevel = Label(0,200,30, visible = False)
directionChange = Label(0, 200, 50, visible = False)
gameFlash = Rect(0,0,400,400, fill='white', visible=False)
###Bad Borders###
###Animation Station###
def onStep():
    playhex.toFront()
    gameCursor.toFront()
    gameFlash.toFront()

    if(gameCounter.value==1):
        arrowsGuides.visible=True
        arrowsGuides2.visible=True
        RightButton.visible=True
        leftButton.visible=True
        leftButtonShadow.visible=True
        rightButtonShadow.visible=True
        
    
    wheel1.rotateAngle +=.15
    wheel2.rotateAngle+=.15
    counterv.value+=1
    if(gameCounter.value==2):
        stageBar.toFront()
        stageBar2.toFront()
        timeLogo.toFront()
        stageName.toFront()
        minute1.toFront()
        minute2.toFront()
        seconds1.toFront()
        seconds2.toFront()
        Colon.toFront()
        #track.play(loop=True)
        
        arrowsGuides.visible=False
        arrowsGuides2.visible=False
        RightButton.visible=False
        leftButton.visible=False
        leftButtonShadow.visible=False
        rightButtonShadow.visible=False
        gameCursor.visible=True
        

        WEbottom.startAngle = (gameWheel1.rotateAngle-300+((sideChangeCounter.value)*60))
        WEtop.startAngle = (gameWheel2.rotateAngle-120+((sideChangeCounter.value)*60))
        if(sideChangeCounter.value == 0):
            WEtop.fill= gameWheel1.fill
            WEbottom.fill= gameWheel2.fill
        if(sideChangeCounter.value == 1):
            WEtop.fill= gameWheel2.fill
            WEbottom.fill= gameWheel1.fill
        if(sideChangeCounter.value == 2):
            WEtop.fill= gameWheel1.fill
            WEbottom.fill= gameWheel2.fill
        if(sideChangeCounter.value == 3):
            WEtop.fill= gameWheel2.fill
            WEbottom.fill= gameWheel1.fill
        if(sideChangeCounter.value == 4):
            WEtop.fill= gameWheel1.fill
            WEbottom.fill= gameWheel2.fill
        if(sideChangeCounter.value == 5):
            WEtop.fill= gameWheel2.fill
            WEbottom.fill= gameWheel1.fill
        BadBorder.rotateAngle = (gameWheel1.rotateAngle)
        BadBorder.radius-=1
        BadBorder2.rotateAngle= (gameWheel1.rotateAngle)
        BadBorder2.radius-=1
        BadBorder.border = (gameCursor.fill)
        BadBorder2.border = (gameCursor.fill)
        if(gameCursor.hitsShape(BadBorder)==True):
            if(gameCursor.hitsShape(WEbottom)==True or gameCursor.hitsShape(WEtop)==True):
                PlayerStatus.value='safe'
            else:
                PlayerStatus.value='dead'
                BadBorder.radius+=1
                Label('YOU DIED',200,200,size=60)
                app.stop()
        if(BadBorder.radius<=2):
            sideChangeCounter.value = randrange(0,5)
            print(sideChangeCounter.value)
        if(BadBorder.radius==200):
            objectSpawn.value=randrange(1,4)
        if(BadBorder.radius==2):
            BadBorder.radius=400
        if(BadBorder2.radius==2):
            BadBorder2.radius=400        

        if(objectSpawn.value==3):
            if(BadBorder.radius>=399):
                BadBorder2.visible=True
                BadBorder.visible=True
                WEtop.visible=True
                WEbottom.toFront()
                WEtop.toFront()
                print(300)
        if(objectSpawn.value==2):
            if(BadBorder.radius>=399):
                BadBorder2.visible=False
                BadBorder.visible=True
                WEtop.visible=True
                WEbottom.visible=True
                timeLogo.toFront()
                stageBar.toFront()
                minute1.toFront()
                minute2.toFront()
                seconds1.toFront()
                seconds2.toFront()
                print(200)


        if(objectSpawn.value==1):
            if(BadBorder.radius>=399):
                BadBorder2.visible=False
                BadBorder.visible=True
                WEtop.visible=True
                WEbottom.visible=False
                timeLogo.toFront()
                stageBar.toFront()
                minute1.toFront()
                minute2.toFront()
                seconds1.toFront()
                seconds2.toFront()
                print(300)


        
        if(counterv.value>=60):
            seconds1.value+=1
            counterv.value=0
        
        if(seconds1.value>9):
            directionChange.value = randrange(1,5)
            seconds2.value+=1
            seconds1.value=0
        if(seconds2.value>=6):
            minute1.value+=1
            seconds2.value=0
        if(minute1.value>9):
            minute2.value+=1
            minute1.value=0
        if(seconds2.value == 1 ):
            stageName.value = 'LINE'
        if(seconds2.value == 2):
            stageName.value = 'TRIANGLE'
        if(seconds2.value == 3):
            stageName.value = 'SQUARE'
        if(seconds2.value == 4):
            if(seconds1.value == 5):
                stageName.value = 'PENTAGON'
        if(minute1.value >= 1):
            stageName.value = 'HEXAGON'
            if (gameDifficulty.value == 1):
                gameDifficulty.value = 4
                flashCounter.value = 1
    if(levelCounter.value == 3):
        hexagonestTitleChange.visible = True
        hexagonestCChangeCounter.value +=1
        if(hexagonestCChangeCounter.value == 15):
            hexagonestTitleChange.fill = rgb(225,26,164)
        elif(hexagonestCChangeCounter.value == 30):
            hexagonestTitleChange.fill = rgb(0,225,255)
        elif(hexagonestCChangeCounter.value == 45):
            hexagonestTitleChange.fill = rgb(225,225,0)
        elif(hexagonestCChangeCounter.value == 60):
            hexagonestCChangeCounter.value = 0
            hexagonestTitleChange.fill = rgb(0,225,0)
    if(playhexCounter.value>=.950):
        playhexCounter.value=0
        playhex.radius=50
        

    if (flashCounter.value == 1):
        gameFlash.visible = True
        gameFlash.opacity -=2
        if (gameFlash.opacity <= 0):
            gameFlash.visible = False
            flashCounter.value = 0
            gameFlash.opacity = 10
    if (gameCounter.value == 1):
        if(sAC.value == 1):
            gameSelect.rotateAngle +=5
            if (gameSelect.rotateAngle == 150):
                sAC.value = 0
                gameSelect.rotateAngle = 90
        elif(sAC.value == 2):
            gameSelect.rotateAngle -=5
            if (gameSelect.rotateAngle == 30):
                sAC.value = 0
                gameSelect.rotateAngle = 90
    elif (gameCounter.value == 2):
        stageBar2.visible = True
        gameCursor.centerX = cursorFunction.x2
        gameCursor.centerY = cursorFunction.y2
        hexagonestTitleChange.visible = False
        gameWheel1.visible = True
        gameWheel2.visible = True
        wheel1.visible = False
        wheel2.visible = False
        hexagon.visible = False
        hexagoner.visible = False
        hexagonest.visible = False
        hyperhexagon.visible = False
        hyperhexagoner.visible = False
        hyperhexagonest.visible = False
        startSpace.visible = False
        sTS.visible = False
        gameSelect.visible = False
        playhex.visible = True
        playhex.rotateAngle += speedlevel.value
        gameWheel1.rotateAngle += speedlevel.value
        gameWheel2.rotateAngle += speedlevel.value
        cursorFunction.rotateAngle += speedlevel.value
        gameCursor.rotateAngle += speedlevel.value
        playhexCounter.value+=.03333
        playhex.radius+=.25
        if (gameDifficulty.value == 1):
            if(seconds2.value >= 1):
                if(seconds1.value >= speedUp.value):
                    if (directionChange.value <= 2):
                        speedlevel.value = 1
                    if (directionChange.value >= 3):
                        speedlevel.value = -1
            gameWheel1.fill = rgb(110,40,0)
            gameWheel2.fill = rgb(150,70,0)
            gameCursor.fill = rgb(255,125,40)
            playhex.border = rgb(255,125,40)
            playhex.fill = rgb(110,40,0)
        if (gameDifficulty.value == 2):
            gameWheel1.rotateAngle += .75
            gameWheel2.rotateAngle += .75
            
        if (gameDifficulty.value == 6):
            gameWheel1.rotateAngle += 1
            gameWheel2.rotateAngle += 1
            playhex.rotateAngle +=1
            cursorFunction.rotateAngle +=1
            gameCursor.rotateAngle +=1
            if(seconds2.value >= 1):
                if(seconds1.value >= speedUp.value):
                    if (directionChange.value <= 2):
                        speedlevel.value = 2
                    if (directionChange.value >= 3):
                        speedlevel.value = -2
            gameWheel1.fill = rgb(165,165,165)
            gameWheel2.fill = rgb(125,125,125)
            gameCursor.fill = rgb(255,255,255)
            playhex.border = rgb(255,255,255)
            playhex.fill = rgb(125,125,125)
            
            if(seconds2.value >= 1):
                if(seconds1.value >= speedUp.value):
                    if (directionChange.value <= 2):
                        speedlevel.value = 2
                    if (directionChange.value >= 3):
                        speedlevel.value = -2
            if(minute1.value == 1):
                gameCursor.fill = rgb(0,150,255)
                gameWheel1.fill=rgb(0,50,179)
                gameWheel2.fill=rgb(0,120,221)
                playhex.border = rgb(0,150,255)
                playhex.fill = rgb(0,50,125)
            if(minute1.value == 2):
                gameCursor.fill = rgb(250,0,210)
                gameWheel1.fill=rgb(170,0,140)
                gameWheel2.fill=rgb(0,100,221)
                playhex.border = rgb(250,0,210)
                playhex.fill = rgb(0,50,125)
                
                
###GameFunctions###
def onKeyPress(keys):
    if (gameCounter.value == 0):
        if ('space' == keys):
            gameCounter.value = 1
            flashCounter.value = 1
            pSTT.visible = False
            logo.visible = False
            gameSelect.visible = True
            levelCounter.value+=1
            sTS.visible = True
            startSpace.visible = True
       
def onKeyHold(keys):
    if (gameCounter.value == 1):
        if ('right' in keys):
            sAC.value = 1
            RightButton.centerX = 338
            RightButton.centerY = 328
            arrowsGuides2.centerX = 338
            arrowsGuides2.centerY = 328
            if (gameSelect.rotateAngle == 100):
                levelCounter.value+=1
        if ('left' in keys):
            sAC.value = 2
            leftButton.centerX = 62
            leftButton.centerY = 328
            arrowsGuides.centerX = 62
            arrowsGuides.centerY = 328

            if (gameSelect.rotateAngle == 80):
                levelCounter.value-=1

        if (levelCounter.value > 6):
            levelCounter.value=1
            print(000)
            
        elif (levelCounter.value < 1):
            levelCounter.value=6
            print(6)
    if (gameCounter.value == 2):
        if ('right' in keys):
            cursorFunction.rotateAngle += 4
            gameCursor.rotateAngle += 4
        if ('left' in keys):
            cursorFunction.rotateAngle -= 4
            gameCursor.rotateAngle -= 4
    if(levelCounter.value==1):
        wheel1.fill=rgb(110,40,0)
        wheel2.fill=rgb(150,70,0)
        leftButton.fill='maroon'
        leftButton.border = 'orangeRed'
        RightButton.fill='maroon'
        RightButton.border = 'orangeRed'
        gameSelect.border = rgb(255,125,40)
        gameSelect.fill = rgb(110,40,0)
        sTS.border = 'orangeRed'
        sTS.fill = 'maroon'
        hexagon.visible = True
        hexagoner.visible = False
        hyperhexagonest.visible = False
    if(levelCounter.value==2):
        wheel1.fill=rgb(10,10,10)
        wheel2.fill=rgb(25,25,25)
        leftButton.fill=rgb(10,245,145)
        leftButton.border=rgb(10,245,145)
        RightButton.fill=rgb(10,245,145)
        RightButton.border=rgb(10,245,145)
        gameSelect.border = rgb(10,245,145)
        gameSelect.fill = rgb(10,10,10)
        sTS.border = rgb(10,245,145)
        sTS.fill = rgb(10,245,145)
        hexagoner.visible = True
        hexagon.visible = False
        hexagonest.visible = False
        hexagonestTitleChange.visible = False
    if(levelCounter.value==3):
        wheel1.fill=rgb(0, 175, 0)
        wheel2.fill=rgb(0, 125, 0)
        gameSelect.border = rgb(0,255,0)
        gameSelect.fill = rgb(0,100,0)
        leftButton.fill=rgb(0,100,0)
        leftButton.border=rgb(0,255,0)
        RightButton.fill=rgb(0,100,0)
        RightButton.border=rgb(0,255,0)
        sTS.border = rgb(0,255,0)
        sTS.fill = rgb(0,100,0)
        hexagonest.visible = True
        hexagoner.visible = False
        hyperhexagon.visible = False
    if(levelCounter.value==4):
        wheel1.fill=rgb(0,50,179)
        wheel2.fill=rgb(0,100,221)
        leftButton.fill=rgb(0,50,125)
        leftButton.border=rgb(0,150,255)
        RightButton.fill=rgb(0,50,125)
        RightButton.border=rgb(0,150,255)
        gameSelect.border = rgb(0,150,255)
        gameSelect.fill = rgb(0,50,125)
        sTS.border = rgb(0,150,255)
        sTS.fill = rgb(0,50,125)
        hexagonest.visible = False
        hyperhexagon.visible = True
        hyperhexagoner.visible = False
        hexagonestTitleChange.visible = False
        gameDifficulty.value = 4
    if(levelCounter.value==5):
        wheel1.fill=rgb(245,245,245)
        wheel2.fill=rgb(225,225,255)
        leftButton.fill=rgb(0,130,255)
        leftButton.border=rgb(0,130,255)
        RightButton.fill=rgb(0,130,255)
        RightButton.border=rgb(0,130,255)
        gameSelect.border = rgb(0,130,255)
        gameSelect.fill = rgb(245,245,245)
        sTS.border = rgb(0,130,255)
        sTS.fill = rgb(0,130,255)
        hyperhexagon.visible = False
        hyperhexagoner.visible = True
        hyperhexagonest.visible = False
    if(levelCounter.value==6):
        wheel1.fill=rgb(165,165,165)
        wheel2.fill=rgb(125,125,125)
        leftButton.fill=rgb(125,125,125)
        leftButton.border=rgb(255,255,255)
        RightButton.fill=rgb(125,125,125)
        RightButton.border=rgb(255,255,255)
        gameSelect.border = rgb(255,255,255)
        gameSelect.fill = rgb(125,125,125)
        sTS.border = rgb(255,255,255)
        sTS.fill = rgb(125,125,125)
        hyperhexagoner.visible = False
        hyperhexagonest.visible = True
        hexagon.visible = False
    
def onMousePress(mouseX, mouseY):
    if (gameCounter.value == 1):
        speedlevel.value = .25
        gameFlash.opacity = 100
        flashCounter.value = 1
        gameCounter.value = 2
        if(levelCounter.value==1):
            gameDifficulty.value = 1
            speedUp.value = (randrange(1,4))
            print(1)
        elif(levelCounter.value==2):
            gameDifficulty.value = 2
            print(2)
        elif(levelCounter.value==3):
            gameDifficulty.value = 3
            print(3)
        elif(levelCounter.value==4):
            gameDifficulty.value = 4
            print(4)
        elif(levelCounter.value==5):
            gameDifficulty.value = 5
            print(5)
        elif(levelCounter.value==6):
            gameDifficulty.value = 6
            print(6)
def onKeyRelease(key):
    leftButton.centerX = 65
    leftButton.centerY = 325
    arrowsGuides.centerX = 65
    arrowsGuides.centerY = 325
    RightButton.centerX = 335
    RightButton.centerY = 325
    arrowsGuides2.centerX = 335
    arrowsGuides2.centerY = 325

cmu_graphics.run()
