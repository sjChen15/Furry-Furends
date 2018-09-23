# Molly Chen and Jenny Chen's FSE

#stuff that needs to be done
'''
story
comments
scoring in general
'''
from glob import *
from pygame import *
from math import *
from random import *
from tkinter import *
init()

####MUSIC#########
mixer.music.load("file.mp3")
mixer.music.play(-1)
####FONT#########
fontOne=font.SysFont("Tw Cen MT Condensed Extra Bold",40)
font1=font.SysFont("Tw Cen MT Condensed Extra Bold",100)

####COLOURS########
RED  =(255,0,0) 
GREEN=(0,255,0)
BLUE= (0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
MINT=(44,214,104)
GRAPE=(55,18,102)
ROSERED=(193,27,27)
LILAC=(220,43,226)
PLUM=(56,26,56)
OLIVE=(85,107,47)
NAVY=(6,13,105)
ORCHID=(218,112,214)
AQUA=(0,255,255)
BEIGE=(255, 246, 199, 255)
BABYBLUE=(137,207,239)
CORALRED=(255,64,64)
lightPink=(255,187,195)
darkPink=(255,141,155)
darkerPink=(241,77,167)

###########SCORE VARIABLES###############
#variables to keep track of each score the player has in total, these variables will determine if the player wins at the end of the game
beaScore=0
manScore=0
phyScore=0
#these variables keep track of the cat's happiness, the lower the hunger and cleanliness, the lower scores the cat will recieve after the mini games
hunger=100
cleanliness=100
happiness=100

#####MINI GAME FUNCTIONS##################

#EATING MINIGAME######################################################################################################
#this minigame is played to keep the cat fed
#the user clicks as many times as he/she can in 15 seconds. the more times they click the higher the score and the more fed the cat is

#loading pics
picturesL=glob("miniGames/eatingMini/*.png") #get all the pictures of the eating mini in a list of strings

eatingPictures=[] #list for the loaded pictures
for pic in picturesL: #load the pictures in the picturesL in a loop
    picture=image.load(pic) #load the picture
    eatingPictures.append(picture) #add it to the list


def blitingFood():
    'blits pictures for the eating minigame'
    screen.blit(eatingPictures[2],(0,0)) #blits the background of the minigame
    timeText=fontOne.render("Time: "+str(timeLeft),True,WHITE) #text for how much time is left
    numberClicked=fontOne.render("Score: "+str(timeClicked),True,WHITE) #text for the score
    screen.blit(timeText,(50,100)) #blit the texts
    screen.blit(numberClicked,(50,200))
    if mouseD: #if the mouse has been clicked
        screen.blit(eatingPictures[1],(300,209)) #a picture of the cat lowering its head is blit, this is so it looks like it is eating
    else:
        screen.blit(eatingPictures[0],(300,200)) #if the mouse isnt clicked, then a regular picture of the cat is blit
        
    if timeLeft>7: #if there are more than 11 seconds left, a picture of a full bowl will be blit
        screen.blit(eatingPictures[3],(290,420)) #every 3 seconds, a bowl of less food is blit until the game ends
    elif timeLeft>5: 
        screen.blit(eatingPictures[4],(290,420))
    elif timeLeft>3:
        screen.blit(eatingPictures[5],(290,420))
    elif timeLeft>1:
        screen.blit(eatingPictures[6],(290,420))
    else:
        screen.blit(eatingPictures[7],(290,420))
        
def eatingMini():
    global timeLeft,timeClicked,mouseU,mouseD,hunger,happiness
    running=True
    timeLeft=10 #the user has 15 seconds to play
    timings=22 #the loop runs slow and it takes about 22 loops for a second to pass
    timeClicked=0 #the variable for the score is reset to 0
    myClock=time.Clock()
    while running:
        clicked=False #reset the clicked and mouseD variables
        mouseD=False
        
        for evt in event.get():

            if evt.type==QUIT:
                running=False
            if evt.type==MOUSEBUTTONDOWN:
                mouseD=True
                if evt.button==1:
                    clicked=True
        
        if timeLeft==0: #if there is no more time left, the loop ends
            running=False
            
        if timings==0: #if the timing counter is at zero a  second is taken off
            timings=22
            timeLeft-=1
        else: #else, a counter is taken off 
            timings-=1

        blitingFood() #blit pictures for the game
        

        if clicked: #if the mouse is clicked, one is added to the score
            timeClicked+=1
            
        display.flip()
        myClock.tick(60)
        
    hunger+=timeClicked #hunger is increased by this game
    if hunger>100: #if the value is over 100, 
        hunger=100 #it is set to 100
    
    return "main" #if the game is finish we return to the main page
    


#CLEANING MINIGAME##############################################################################################

#cleaning mini game pics
background=image.load("miniGames/cleaningMini/background.png") #the background
cat=image.load("Sprite/idle cat thing001.png") #this image will continue to change
catU=image.load("Sprite/idle cat thing001.png") #the image of the cat sitting normaling
catD=image.load("Sprite/idle cat thing002.png")  #image of the cat with its head down, it will be used to make the cat look like its bobbing its head
dirty1=image.load("miniGames/cleaningMini/pics/dirty01.png") #the 3 images of "dirty things"
dirty2=image.load("miniGames/cleaningMini/pics/dirty02.png")
dirty3=image.load("miniGames/cleaningMini/pics/dirty03.png")
dirty=[dirty1,dirty2,dirty3] #a list of the the pics of the "dirty things"

#cleaning minigame rects
cleanRect=(250,150,350,400) #rect of where the cat sits
scoreRect=(0,0,200,200) #rect of where the score, time and the life is

#cleaning mini functions

def dMiniBlit(): #function to blit the pictures
    'blits the pictures for the cleaning mini'
    global clean,scoreBoard,cat
    screen.blit(background,(0,0)) #blit the background
    clean=screen.subsurface(cleanRect).copy() #copies where the cat sits without the cat, so a clean picture of the cat can be blit
    screen.blit(cat,(283,200)) #blit the animal
    scoreBoard=screen.subsurface(scoreRect).copy() #copies the rectangle of the score, life and time

    
def makeDirty():
    'blits an image of a "dirty thing" that needs to be cleaned off'
    global boxX,boxY
    ran=randint(0,len(dirty)-1) #find a random "dirty thing" position. 
    boxX=randint(300,500) #find a random x and y value blit the picture
    boxY=randint(250,400)
    rnBox=Rect(boxX,boxY,60,60) #this is rect of the picture. This will be used to determine if the user has clicked on the picture or not
    
    screen.blit(clean,(250,150)) #blit a picture of the background behind the cat
    screen.blit(cat,(283,200)) #blits the picture of the cat, its head could be up or down
    screen.blit(dirty[ran],(boxX,boxY)) #blit the "dirty thing" picture at the random location
    return rnBox,ran #return the rect of where the image is and the position of the picture in the list.

def throwOut(ran): #the position of the picture is given
    'blits the "dirty thing" in a pile at the side'
    TOX=randint(600,625) #a random x and y valuue is found in a certain area so the placement of the blit is random but in a contained area
    TOY=randint(400,425)
    screen.blit(dirty[ran],(TOX,TOY)) #blit the picture at the x and y position 

def blitPics():
    'blits the pictures that are constantly changing'
    global cat
    scoreText=fontOne.render("Score: "+str(score),True,WHITE) #the score
    lifeText=fontOne.render("Lives: "+str(life),True,WHITE) #the # of lives left
    timeText=fontOne.render("Time: "+str(seconds),True,WHITE) #the time left
    screen.blit(scoreBoard,(0,0)) #a blank picture of where these texts will be blit
    screen.blit(scoreText,(10,50)) #bliting the texts
    screen.blit(lifeText,(10,20))
    screen.blit(timeText,(10,80))

    if secondsCounter==60: #if the secondsCounter is at 60
        cat=catU #then the cat's head is up 
    if secondsCounter==30: #if the secondsCounter is at 30
        cat=catD #the cat's head will be down
    #so every half second the head bobs up or down
    screen.blit(clean,(250,150)) 
    screen.blit(cat,(283,200))
    screen.blit(dirty[currentDirty],(boxX,boxY))
    

def cleaningMini():
    'main cleaning mini game function'
    global currentRect,myClock,mx,my,timer,score,life,seconds,secondsCounter,currentDirty,cleanliness,happiness
    dMiniBlit() #picture bliting function
    currentRect=Rect(0,0,10,10) #define a rectangle for the current "dirty thing"
    currentRect,currentDirty=makeDirty() #run the makeDirty function to start the game and get values of the current rect of the picture and the picture position in the loop
    running=True #so the loop can run
    myClock=time.Clock() 
    mx,my=0,0 #define the current position of the mouse
    score=0 #define the score at 0
    life=3 #define the number of lives
    seconds=10 #player gets 30 seconds to play
    secondsCounter=60 #a variable to count the number of times the loop runs to count the seconds
    
    
    while running:
        clicked=False #reset the variable clicked

        for evt in event.get():
            if evt.type==QUIT:
                running=False 
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1:
                    clicked=True #if the mouse is clicked, variable clicked is true
        if seconds==0: #if the time runs out, the loop ends
            running=False
            
        if life==0: #if the player has no more lives, the game ends
            running=False
            
        mx,my=mouse.get_pos() #get the position of the mouse
        mb=mouse.get_pressed() #if a button on the mouse is pressed

        if currentRect.collidepoint(mx,my) and clicked: #if mouse is on the rect and it is clicked
            currentRect,currentDirty=makeDirty() #run the fuction again to get a new "dirty thing" on the cat
            throwOut(currentDirty) #"throw out" the old picture
            score+=2 #add two points to the score
        elif clicked: #if anywhere else was clicked, the user losses a life
            life-=1

        if secondsCounter==0: #if the counter is at 0, a second has passed because the loop runs 60 times a second
            secondsCounter=60 #reset the counter
            seconds-=1 #subtract a second
        else:
            secondsCounter-=1 #if the counter isnt at 0, 1 is subtracted from the counter to mark another loop has passed

        blitPics() #blit the updated scores and pictures
        
        
        display.flip()
        myClock.tick(60) #runs at 60 loops per second

    cleanliness+=score #cleanliness is increased by this game
    if cleanliness>100: #if the value is over 100, 
        cleanliness=100 #it is set to 100
        
    return "main" #if the loop has ended, the game is over and we return to the main game screen

#APPEARANCE MINIGAME######################################################################################################

#appearance mini game pics
ba=image.load('miniGames/reactionMini/bar.png')
reactionback=image.load('miniGames/reactionMini/reactionback.png')
angry=image.load('miniGames/reactionMini/angryspeechbubble.png')
smile=image.load('miniGames/reactionMini/smilespeechbubble.png')
idle1=image.load("Sprite/idle cat thing001.png")
idle2=image.load("Sprite/idle cat thing002.png")
reactionbackInstr=image.load('miniGames/reactionMini/reactionbackInstr.png')

#appearance mini rects
barRect=Rect(800,180,0,0)
line=Rect(10,180,0,0)


#appearence mini game functions
class Bar():
    def __init__(self,rect,line,count,Barpics,stops,linex,ch,pt,emo,idlept,sp):
        self.rect=rect
        self.line=line
        self.count=count
        self.Barpics=Barpics
        self.stops=stops
        self.linex=linex
        self.ch=ch
        self.pt=pt
        self.emo=emo
        self.idlept=idlept
        self.sp=sp
        
    def move(self):
        global chances,sp,clicked,linex,count,emo,pt
        if clicked:
            self.sp+=1#speed change of bar
            chances-=1#chances to click
            self.stops.append(self.linex)#collects clicked position for points
            self.count=0#reset speed
            if self.linex<300 or self.linex>450:#if they didn't do well
                self.emo=1
            else:#if they did well
                self.emo=2  
            return self.linex
        
        if not clicked and self.count==0:#if they just clicked and regestered a position 
            self.count=4*self.sp# new speed
            self.linex=0#bar starts at beginning
        self.line=Rect(self.linex,0,10,180)#Rectangle that is the white line
        self.linex+=self.count#moves bar
        screen.blit(self.Barpics[0],(0,0))#blit background
        draw.rect(screen,(255,255,255),self.line,0)#blits moving bar
        if chances<20:#after first click
            screen.blit(self.Barpics[self.emo],(0,300))#blit cat emotion relative to the performance of player
        display.flip()
        if self.linex>=800 or self.linex==0:# if moving bar reaches the other end it will come back
            self.count*=-1
            
    def collect(self):#calculating point values for each stop
        global pt
        if 0<self.linex<101 or 700<self.linex<801:#at the two farthest ends
            self.pt+=3
        if 100<self.linex<201 or 600<self.linex<701:
            self.pt+=5
        if 300<self.linex<372 or 418<self.linex<601:
            self.pt+=8
        if 371<self.linex<419:#at an area in the middle
            self.pt+=10
    
    
    def idle(self):#bliting idle cat
        screen.blit(self.Barpics[5],(0,-40))#background
        if self.idlept>5:#idle1
            screen.blit(self.Barpics[3],(250,200))
        else:#idle2
            screen.blit(self.Barpics[4],(250,200))
        if self.idlept==0:
            self.idlept=20
        self.idlept-=1#delaying the change between idle1 and 2

   

def appearanceMini():
    #global and reset all values each time plyer enters game
    global count,stops,linex,chances,pt,emo,idlept,sp,Barpics,clicked,reactionbackInstr,startA,beaScore,happiness,cleanliness,hunger
    instructioned=False
    count=4
    stops=[]
    linex=0
    chances=20
    pt=0
    emo=1
    idlept=20
    sp=1
    Barpics=[ba,angry,smile,idle1,idle2,reactionback]
    #define variables in class
    b=Bar(barRect,line,count,Barpics,stops,linex,chances,pt,emo,idlept,sp)

    running=True
    #blit background
    screen.blit(reactionback,(0,-40))
    display.flip()
    print('hi')
    #mini game loop
    while running:
        clicked=False
        for evnt in event.get():        
            if evnt.type == QUIT:
                running = False
            if evnt.type==MOUSEBUTTONDOWN:
                clicked=True
        

        b.idle()
        pts=fontOne.render("Score: "+str(pt),True,BLACK) #rendering font for points and chances left
        chancesText=fontOne.render("Chances Left: "+str(chances),True,BLACK)
        screen.blit(chancesText,(5,300))
        screen.blit(pts,(5,350))
        p=b.move()
        if clicked:#call the functions 
            if 0<p<100 or 700<p<800:#at the two farthest ends
                pt+=1
            if 100<p<200 or 600<p<700:
                pt+=1
            if 300<p<371 or 418<p<600:
                pt+=2
            if 371<p<418:#at an area in the middle
                pt+=3
        
        if chances<=0: #if there are no more chances left, the game is over
            running=False
        

            
        keys=key.get_pressed()
        
    happyPercent=happiness/100 #happiness determines how much of the score is kept
    pt=int(pt*happyPercent) #multiply the score by that percent
    beaScore+=pt #add the score to the total score
    howDirty=randint(12,17) #random value of how much the cleanliness goes down
    cleanliness-=howDirty #subtract it
    howHungry=randint(12,17) #random num of how much the hunger goes down
    hunger-=howHungry
    if hunger<0: #the hunger and cleanliness can't be less than 0 so if they are, they are set to 0
        hunger=0
    if cleanliness<0:
        cleanliness=0
    return "main"

        
#MANNERS MINIGAME#########################################################################################
#this mini game is a game of simon says

#manners minigaame pics
mannersBack=image.load("miniGames/mannersMini/pics/New Piskel.png")#background

#images for the small boxes
fJump1=image.load("miniGames/mannersMini/pics/testSprite007.png")#forward facing jumping images
fJump2=image.load("miniGames/mannersMini/pics/testSprite008.png")

bJump1=image.load("miniGames/mannersMini/pics/testSprite043.png") #backward facing jumping images
bJump2=image.load("miniGames/mannersMini/pics/testSprite044.png")

lWalk1=image.load("miniGames/mannersMini/pics/testSprite013.png") #walking left images
lWalk2=image.load("miniGames/mannersMini/pics/testSprite014.png")

rWalk1=image.load("miniGames/mannersMini/pics/testSprite031.png") #walking right images
rWalk2=image.load("miniGames/mannersMini/pics/testSprite032.png")

#images for the big cat
fJump=image.load("miniGames/mannersMini/pics/testSprite108.png") #forwards jumping
bJump=image.load("miniGames/mannersMini/pics/testSprite144.png") #backwards jumping
lWalk=image.load("miniGames/mannersMini/pics/testSprite113.png") #walking left 
rWalk=image.load("miniGames/mannersMini/pics/testSprite131.png") #walking right

fJumpR=image.load("miniGames/mannersMini/pics/testSprite109.png") #forwards jumping
bJumpR=image.load("miniGames/mannersMini/pics/testSprite145.png") #backwards jumping
lWalkR=image.load("miniGames/mannersMini/pics/testSprite114.png") #walking left 
rWalkR=image.load("miniGames/mannersMini/pics/testSprite132.png") #walking right
resting=image.load("miniGames/mannersMini/pics/testSprite107.png")

#rects
rect1=Rect(240,450,50,50) #the four boxes that the player clicks on
rect2=Rect(330,450,50,50)
rect3=Rect(420,450,50,50)
rect4=Rect(510,450,50,50)
blitRect=Rect(250,100,300,300) #rect of where the cat is
commandsRestR=Rect(200,430,600,100) #rect of the command boxes in rest

#variables
            #[coresponding rect, coords of the box, small first pic, small second pic of the movement, big picture of the movement]
arrowBoxes=[[rect1,(240,450),fJump1,fJump2,fJump,fJumpR],[rect2,(330,450),bJump1,bJump2,bJump,bJumpR],[rect3,(420,450),lWalk1,lWalk2,lWalk,lWalkR],[rect4,(510,450),rWalk1,rWalk2,rWalk,rWalkR]]
#list of the commands and their cooresponding values/pictures
#arrowBoxes=[[jump facing the front],[jump facing the back],[walk to the left],[walk to the right]]
#a compact list for values


def mMiniBlit(): #function to blit the pictures
    global back,restingPic,blank,commandsRest
    screen.blit(mannersBack,(0,0)) #background picture
    blank=screen.subsurface(blitRect).copy() #a pic of the background of where the cat sits, so pictures of the cat doing other things can be blit ontop 
    screen.blit(resting,(250,100)) #blit the picture of the sitting cat
    
    restingPic=screen.subsurface(blitRect).copy() #pic with big cat and the backgroun

    for box in arrowBoxes: #draw the command boxes and blit their pictures
        draw.rect(screen,MINT,box[0])
        screen.blit(box[2],box[1])
    commandsRest=screen.subsurface(commandsRestR).copy()
    back=screen.copy()#after everything has blit
    scoreAndLife() #blits the score and text

def scoreAndLife():
    global mannersScore,mannersLife
    'loads and blits the score and life for the manners minigame'
    draw.rect(screen,BEIGE,(0,0,200,150))
    scoreText=fontOne.render("Score: "+str(mannersScore),True,BLACK) #the score text
    screen.blit(scoreText,(50,50)) #bliting the score
    lifeText=fontOne.render("Life: "+str(mannersLife),True,BLACK) #lives left in text
    screen.blit(lifeText,(50,100)) #bliting the # of lives left


def command():
    'add a command into the list and command it'
    global commands,back,myClock,speed,arrowNum
    arrowNum=0 #position in the list of the correct answer
    rectNum=0 #position of the rect in the command list that should be highlighted for the simon says command
    ran=randint(0,3) #a random position to generate a new simon says command
    commands.append(arrowBoxes[ran]) #add the random box to the list of commands
    screen.blit(back,(0,0)) #blit the background
    startSpeed=40 #counter of how many loops pass before bliting the next command. it doesnt change so it can keep track of what the original counter was
    speed=40 # same counter but this one changes
    scoreAndLife() #blit the score and # of lives 
    
    while True:
        if rectNum==len(commands) and speed==0: #if the arrowNum plus one is equal to the number of items in the list, then all the commands have been done
            break
        if speed==0: #if the 40 loops have passed, the mint box is drawn as grape instead
            draw.rect(screen,GRAPE,commands[rectNum][0])
            screen.blit(commands[rectNum][3],commands[rectNum][1]) #the picture of the moving action is blit into the box. ex. in the walking left box, the picture of the cat taking another step is blit 
            rectNum+=1 #add one to the rectNum so the next rect in the command list can be blit
            speed=startSpeed-1 #the counter is reset to a speed one less than the last, so the commands are given faster and faster
            startSpeed-=1 #the start speed is changed as well
        if speed==int(startSpeed/2): #halfway the screen is reset to what it looked like before, so the player can see the boxes go from mint to grape and back. This is done so that if there are two of the same commands in the row, the player can see the box changed twice
            screen.blit(commandsRest,(200,430)) #blit the picture where the boxes are not highlighted at all
        speed-=1 #subtract one from the counter to mark a loop has passed

        display.flip()
        myClock.tick(60)

def check():
    'checks if the answer is right'
    global mannersLife,mannersScore,arrowNum
    rightAns=commands[arrowNum][0] #the rect of the right answer
    for box in arrowBoxes: #goes through each box
        if box[0].collidepoint(mx,my) and clicked: #if the mouse is over the box and it is clicked
            if box[0]!=rightAns: #if the box is not the right answer
                mannersLife-=1 #a life is lost
            elif box[0]==rightAns: #if the answer is correct
                mannersScore+=2 #add 2 points to the score
                if len(commands)-1==arrowNum: #position of the right answer(arrowNum) is the position of the last value,

                    command() #a new command is added by running the command function
                    return #and we leave the funcion
                else:
                    arrowNum+=1 #if it isnt the last value, we add one to arrowNum                



def bliting():
    'blits the pictures that change every loop'
    global arrowBoxes,restingPic,back
    for box in arrowBoxes: #for the boxes in arrowBoxes 
        draw.rect(screen,MINT,box[0]) #draw the mint box to reset the command boxes
        screen.blit(box[2],box[1]) #and the small picture in the normal position of that action
        if box[0].collidepoint((mx,my)): #if the box is being collided with
            draw.rect(screen,GRAPE,box[0]) #draw the small box grape
            screen.blit(blank,(250,100)) #blit the background behind the big cat
            
            if moveLoops>10: #if the counter has a value larger than 10, 
                screen.blit(box[4],(250,100)) #blit the large image of the cat in that command
                screen.blit(box[3],box[1]) #blit the movning picture into the small box
            else:
                screen.blit(box[5],(250,100)) #if it is under or equal to 10, blit the big cat in the next movement in the animation
                screen.blit(box[2],box[1]) #and the smaller picture in the next movement




def mannersMini():
    'main game function for the manners minigame'
    global commands,myClock,mannersScore,mannersLife,mx,my,clicked,moveLoops,mb,manScore,happiness,cleanliness,hunger
    mannersLife=3 #variable of how many lives the user has left
    running=True #so the looop runs
    clicked=False #flag to see if the mouse has bee clicked
    arrowNum=0 #position of the right answer
    myClock=time.Clock()
    mb=mouse.get_pressed() #if the mouse is pressed down
    commands=[] #list of the commands 
    mannersScore=0  #score of the minigame
    moveLoops=20 #number of loops until the cat makes a movement 
    mMiniBlit() #call the function to blit the main pictures
    command() #start the game with one simon says
    
    while running:
        clicked=False #reset the clicked flag
        
        for evt in event.get():
            if evt.type==QUIT:
                running=False
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1: 
                    clicked=True #if the mouse is pressed down, clicked is true
                    

        if mannersLife==0: # if the player has no more lives, the loop ends
            running=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()        

        if moveLoops==0:
            moveLoops=20
        else:
            moveLoops-=1
        bliting() #blit the nessecary pictures
        check() #check to see if the user has clicked on the correct answer
        scoreAndLife() #blit the score and life totals
 
        display.flip()
        myClock.tick(60) #60 loops a second

    happyPercent=happiness/100 #happiness determines how much of the score is kept
    mannersScore=int(mannersScore*happyPercent) #multiply the score by that percent
    manScore+=mannersScore #add the score to the total score
    howDirty=randint(12,17) #random value of how much the cleanliness goes down
    cleanliness-=howDirty #subtract it
    howHungry=randint(12,17) #random num of how much the hunger goes down
    hunger-=howHungry
    if hunger<0: #the hunger and cleanliness can't be less than 0 so if they are, they are set to 0
        hunger=0
    if cleanliness<0:
        cleanliness=0
    return "main" #if the game has ended, the game returns to the main page


#PHYSICAL MINIGAME##########################################################################################

#bliting pictures
back=image.load('miniGames/runningMini/mini backgrass.png')
coin=image.load('miniGames/runningMini/coin.png')
rock=image.load('miniGames/runningMini/mountain-rock.png')
r1=image.load('Sprite/testSprite031B.png')
r2=image.load('Sprite/testSprite032B.png')
dor1=image.load('Sprite/testSprite034B.png')
dor2=image.load('Sprite/testSprite035B.png')
upr1=image.load('Sprite/testSprite046B.png')
upr2=image.load('Sprite/testSprite047B.png')
images=[back,r1,r2,dor1,dor2,upr1,upr2,coin,rock]

#defining variables
myClock = time.Clock()
pro=[0,0,0,0,0,0,450]
top=[False,0,True,0,False]
obstacle=[]
place=0
wait=[0,0,0,0]
points=0
coinlis=[]
gameover=False
x1=800
y1=randint(450,550)
coinlis.append([24,50,x1,y1])
point=0

class animal():
    def __init__(self,rect,coinlis,points,pro,wait,top,obstacle,images,gameover,font1):
        self.rect=rect
        self.coinlis=coinlis
        self.points=points
        self.pro=pro
        self.wait=wait
        self.top=top
        self.obstacle=obstacle
        self.images=images
        self.gameover=gameover
        self.font1=font1

        
    def backmove(self):#moving background
        global coinlis ,obstacle ,points
        if self.gameover:
            return True
        keys=key.get_pressed()
        if keys[K_UP]:#up key
            for i in range(len(self.coinlis)):
                self.coinlis[i][2]-=10#coins move closer
            if len(self.obstacle)>0:
                self.obstacle[0][2]-=10#obstacles move closed
            if self.pro[3]<800:
                self.pro[3]+=10
            else:
                self.pro[3]=0
            screen.blit(self.images[0],(-(self.pro[3]),-200))#bliting backround
            screen.blit(self.images[0],(800-self.pro[3],-200))#bliting 2 so that the same background would loop
            display.flip()
            self.changelaneup()#Make cat run upwards
        elif keys[K_DOWN]:
            for i in range(len(self.coinlis)):
                self.coinlis[i][2]-=10#coins move closer
            if len(self.obstacle)>0:
                self.obstacle[0][2]-=10#obstacles move closed
            if pro[3]<800:
                self.pro[3]+=10#background moving
            else:
                self.pro[3]=0
            screen.blit(self.images[0],(-(self.pro[3]),-200))#bliting backround
            screen.blit(self.images[0],(800-self.pro[3],-200))#bliting 2 so that the same background would loop
            display.flip()
            self.changelanedo()#make cat run downwards
        elif keys[K_RIGHT]:
            for i in range(len(self.coinlis)):
                self.coinlis[i][2]-=10#coins move closer
            if len(self.obstacle)>0:
                self.obstacle[0][2]-=10#obstacles move closed
            if self.pro[3]<800:
                self.pro[3]+=10#background moving
            else:
                self.pro[3]=0
            screen.blit(self.images[0],(-(self.pro[3]),-200))#bliting backround
            screen.blit(self.images[0],(800-self.pro[3],-200))#bliting 2 so that the same background would loop
            display.flip()
            self.leftright()#move cat to the right
                
    def leftright(self):
        global points
        score=font1.render(str(self.points),True,(0,0,0))
        screen.blit(score,(0,0))#blit the score
        if self.wait[1]>=7:#stalling for animations
            self.wait[1]=0
            screen.blit(self.images[1],(50,self.pro[6]))
        elif self.wait[1]==0 or 4<self.wait[1]<8:
            screen.blit(self.images[1],(50,self.pro[6]))
            self.wait[1]+=1
        elif 0<self.wait[1]<5:
            screen.blit(self.images[2],(50,self.pro[6]))
            self.wait[1]+=1

    def changelaneup(self):
        global points
        score=font1.render(str(self.points),True,(0,0,0))
        screen.blit(score,(0,0))#blit score in corner
        if self.pro[6]>400:
            self.pro[6]-=3#move upwards
            if self.wait[2]>=7:#stalling animation
                self.wait[2]=0
            if self.wait[2]==0 or 4<self.wait[2]<9:
                screen.blit(self.images[5],(50,self.pro[6]))
                self.wait[2]+=1
            elif 0<self.wait[2]<5:
                screen.blit(self.images[6],(50,self.pro[6]))
                self.wait[2]+=1
        elif self.pro[6]<=400:#if they reach the end they will move towards the right
            self.leftright()
        display.flip()
        
    def changelanedo(self):
        global points
        score=font1.render(str(self.points),True,(0,0,0))
        screen.blit(score,(0,0))
        if self.pro[6]<500:
            self.pro[6]+=3#move downwards
            if self.wait[3]>=7:#stalling animation
                self.wait[3]=0
            if self.wait[3]==0 or 5<self.wait[3]<9:
                screen.blit(self.images[3],(50,self.pro[6]))
                self.wait[3]+=1
            elif 0<self.wait[3]<6:
                screen.blit(self.images[4],(50,self.pro[6]))
                self.wait[3]+=1
        elif self.pro[6]>=500:
            self.leftright()#if they reach the end they will move towards the right
        display.flip()



    def coins(self):#management of coins and obstacles
        global point
        self.rect=Rect(50,self.pro[6]+55,75,30)
        if len(self.coinlis)<5 and self.top[0]==0:#if there are less than 5 coins on screen
            x=800
            y=randint(450,550)#random coin position
            self.coinlis.append([24,50,x,y])
            self.top[3]=50
        if len(self.obstacle)==0 and len(self.coinlis)>0:#making 1 obstacle at a time
            x=800#x is constant
            y=randint(450,550)#random position
            for i in range(len(self.coinlis)):#not in the same position as a coin
                if y==self.coinlis[i][3]:
                    y=randint(450,550)#make another random position
            self.obstacle.append([10,10,x,y])#add position to list

        if len(self.coinlis)!=0:
            i=0
            while i<(len(self.coinlis)-1):#checking if any coins or obstacles are colliding
                if len(self.obstacle)>0:#if there is an obstacle, blit it
                    screen.blit(self.images[8],(self.obstacle[0][2]-10,self.obstacle[0][3]-10))
                screen.blit(self.images[7],(self.coinlis[i][2],self.coinlis[i][3]))#blit the coins
                if self.coinlis[i][2]<0 :#if the coins were missed by the player delete it from list
                    del self.coinlis[i]
                elif self.rect.colliderect(self.coinlis[i][2],self.coinlis[i][3],24,50):#if the coins were taken by player delete from list and add a point
                    del self.coinlis[i]
                    self.points+=1
                    point=self.points
                if len(self.obstacle)>0 and self.obstacle[0][2]<0 :#if an obstacle was missed
                    del self.obstacle[0]
                elif len(self.obstacle)>0 and self.rect.colliderect(self.obstacle[0][2],self.obstacle[0][3],24,50):#if the player hit an obstacle, then gameover
                    self.gameover=True
                i+=1
            

ca=animal(Rect(1, 1, 100, 100),coinlis,points,pro,wait,top,obstacle,images,gameover,font1)
def physicalMini():
    global ca,myClock,pro,top,obstacle,place,coinlis,gameover,images,xl,yl,d,points,wait,font1,phyScore,happiness,cleanliness,hunger,physScore,point
    myClock = time.Clock()
    pro=[0,0,0,0,0,0,450]
    top=[False,0,True,0,False]
    obstacle=[]
    place=0
    wait=[0,0,0,0]
    points=0
    point=0
    coinlis=[]
    gameover=False
    x1=800
    y1=randint(450,550)
    coinlis.append([24,50,x1,y1])
    running = True
    myClock = time.Clock()
    ca=animal(Rect(1, 1, 100, 100),coinlis,points,pro,wait,top,obstacle,images,gameover,font1)
    while running:
        d=False
        for evnt in event.get():        
            if evnt.type == QUIT:
                running = False
            if evnt.type==KEYDOWN:
                d=True

        if ca.backmove():
            running=False
        ca.coins()
        keys=key.get_pressed()
        display.flip()
        
    happyPercent=happiness/100 #happiness determines how much of the score is kept
    point=int(point*happyPercent) #multiply the score by that percent
    phyScore+=point #add the score to the total score
    howDirty=randint(12,17) #random value of how much the cleanliness goes down
    cleanliness-=howDirty #subtract it
    howHungry=randint(12,17) #random num of how much the hunger goes down
    hunger-=howHungry
    if hunger<0: #the hunger and cleanliness can't be less than 0 so if they are, they are set to 0
        hunger=0
    if cleanliness<0:
        cleanliness=0
    return "main"


#####MENU FUNCTIONS######################################################################################################
#menu loading pics
idle1=image.load("Sprite/idle cat thing001.png")
idle2=image.load("Sprite/idle cat thing002.png")
buttonup=image.load("main/buttonup.png")
buttondown=image.load("main/buttondown.png")
ap=image.load("main/appearence.png")
bb=image.load("main/bubbles.png")
fd=image.load("main/food.png")
mn=image.load("main/manners.png")
ps=image.load("main/physical.png")
buttonb=image.load("main/buttonback.png")
mainback=image.load("main/MainBack.png")
mainback2=image.load("main/MainBack2.png")
appearancelvl=image.load("main/appearancelvl.png")
day=image.load("main/daytime.png")
night=image.load("main/nighttime.png")
bars=image.load("main/bars.png")
mannerlvl=image.load("main/mannerlvl.png")

physicallvl=image.load("main/physicallvl.png")

#defining variables
buttons=["food","wash","appearance","manners","physical"]
buttonpics=[]
otherpics=[[mainback,mainback2],[idle1,idle2],[buttonup,buttondown],[fd,bb,ap,mn,ps],buttonb,
           [appearancelvl,mannerlvl,physicallvl],[day,night],bars]
petting=False
values=[0]
buttonpos=[(66,515),(212,515),(358,515),(504,515),(650,515)]
barpos=[[(-40,-20),(20,-20)],(500,10),(520,160),(620,160),(720,160)]
turns=5
days=10
mx,my=0,0
clicked=False
font3=font.SysFont("Tw Cen MT Condensed Extra Bold",40)
font4=font.SysFont("Tw Cen MT Condensed Extra Bold",20)

class Selectionscreen():
    def __init__(self,buttonpics,buttonpos,petting,otherpics,values,buttons,barpos,turns,days):
        self.buttonpics=buttonpics
        self.buttonpos=buttonpos
        self.petting=petting
        self.otherpics=otherpics
        self.values=values
        self.buttonpos=buttonpos
        self.buttons=buttons
        self.barpos=barpos
        self.turns=turns
        self.days=days
    def idleAnimal(self):
        global mb,mx,my,running,clicked,returning,beaScore,manScore,phyScore,happiness,hunger,cleanliness,font3,turns
        if self.turns==1 and self.days==0:#if there are no moves or turns left
            returning="contest"
            running=False
        app=font4.render(str(beaScore),True,WHITE) #the scores of the three mini games
        ma=font4.render(str(manScore),True,WHITE)
        ph=font4.render(str(phyScore),True,WHITE)
        
        happy=font3.render(str(happiness),True,(255,255,255)) #the values of happiness hunger and cleanliness in order
        hungry=font3.render(str(hunger),True,(255,255,255))
        cle=font3.render(str(cleanliness),True,(255,255,255))
        
        day=font1.render(str(self.days),True,(255,255,255))
        #sun or moon icon at top left
        if self.turns>2:#if it is day
            screen.blit(self.otherpics[0][0],(0,0))
            screen.blit(self.otherpics[6][0],self.barpos[0][0])
        else:#if it is night
            screen.blit(self.otherpics[0][1],(0,0))
            screen.blit(self.otherpics[6][1],self.barpos[0][1])
        #blit bars of values
        screen.blit(self.otherpics[7],self.barpos[1])
        
        screen.blit(cle,(650,20)) #bliting the cleanliness, hunger and happiness values
        screen.blit(hungry,(650,70))
        screen.blit(happy,(650,125))

        
        #blit number of days left
        screen.blit(day,(160,50))
        
        for i in range(3):#blit training lvls
            screen.blit(self.otherpics[5][i],self.barpos[2+i])
        
        screen.blit(app,(535,180)) #bliting the 3 mini game scores
        screen.blit(ma,(635,180))
        screen.blit(ph,(735,180))
            
        if self.values[0]>10:#idle cat
            screen.blit(self.otherpics[1][0],(275,200))
        else:
            screen.blit(self.otherpics[1][1],(275,200))
        if self.values[0]==0:
            screen.blit(self.otherpics[1][0],(275,200))
            self.values[0]=20
        self.values[0]-=1
        #pink area behind buttons
        screen.blit(self.otherpics[4],(0,0))
        for i in self.buttonpos:#blit button frames
            screen.blit(self.otherpics[2][0],i)
        for i in range(5):#blit content of buttons
            screen.blit(self.otherpics[3][0+i],(self.buttonpos[i][0]+5,self.buttonpos[i][1]+5))
            # if a button was pressed
            if Rect(self.buttonpos[i][0],self.buttonpos[i][1],80,80).collidepoint(mx,my) and mb[0]==1:
                #take away a turn
                if self.turns==0:
                    self.turns=5
                    self.days-=1
                elif self.turns!=0:
                    self.turns-=1
                #blit the button frame as pressed
                screen.blit(self.otherpics[2][1],self.buttonpos[i])
                screen.blit(self.otherpics[3][0+i],(self.buttonpos[i][0]+5,self.buttonpos[i][1]+5))

                #go to different minigames depending on button pressed
                if self.buttons[i]=="appearance":
                    returning="appearanceMini"
                    running=False
                elif self.buttons[i]=="wash":
                    returning="cleaningMini"
                    running=False
                elif self.buttons[i]=="food":
                    returning="eatingMini"
                    running=False
                elif self.buttons[i]=="manners":
                    returning="mannersMini"
                    running=False
                elif self.buttons[i]=="physical":
                    #resetting variables to play again
                    myClock = time.Clock()
                    pro=[0,0,0,0,0,0,450]
                    top=[False,0,True,0,False]
                    obstacle=[]
                    place=0
                    wait=[0,0,0,0]
                    points=0
                    coinlis=[]
                    gameover=False
                    screen.blit(images[0],(0,-200))
                    screen.blit(images[1],(50,450))
                    x1=800
                    y1=randint(450,550)
                    coinlis.append([24,50,x1,y1])
                    ca=animal(Rect(1, 1, 100, 100),coinlis,points,pro,wait,top,obstacle,images,gameover,font1)
                    returning="physicalMini"
                    running=False
        display.flip()

select=Selectionscreen(buttonpics,buttonpos,petting,otherpics,values,buttons,barpos,turns,days)

def main():
    global mb,mx,my,clicked,returning,running,days,happiness,cleanliness,hunger,turns
    
    
    running=True
    returning="exit" #a variable that will return the next page
    while running:
        clicked=False
        for evt in event.get():          
            if evt.type == QUIT:
                running = False
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1:
                    clicked=True
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        

        if days==0: #if there are no days left , then the game ends 
            returning="contest" #the returning page will be the contest page
            running=False #the loop ends

        if hunger==0: #if the pet's hunger is at 0, the cat dies from hunger
            returning="youLose" #the page returned is you lose
            running=False

        if cleanliness==0: #if the cat is too dirty, it runs away and you lose
            returning="youLose" #return the page youLose
            running=False #loops ends
            
        happiness=int((cleanliness+hunger)/2) #happiness is determined by the average of the cleanliness and hunger
        select.idleAnimal()
        
        display.flip()
    return returning #return the page 

def instructions():
    running = True
    inst = glob("startMenu/instructions/*.png") #take all the pictures in this folder are the pictures of the instructions

    instrPages=[] #list of loaded instruction pages
    for pic in inst: #load the pictures in a loop
        picture=image.load(pic)
        instrPages.append(picture) #add it to the list
        
    pageNum=0 #current page of instructions
    while running:
        clicked=False #reset the flags
        rightClicked=False
        
        for evt in event.get():          
            if evt.type == QUIT:
                running = False
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1:  #if the left clicked is clicked then click is true
                    clicked=True
                if evt.button==3: #if the right click is clicked, rightClicked is true
                    rightClicked=True
        
        if clicked: #if the mouse is clicked, the page number increases
            if pageNum==7: #unless it is the last page
                running=False #then the loop ends
            else:
                pageNum+=1
                
        if rightClicked: #if the mouse is right clicked
            if pageNum==0: #if the page is the first one
                running=False #the loop ends
            else:
                pageNum-=1 #otherwise, the page number goes back
        
            
        if key.get_pressed()[K_ESCAPE]:
            running = False #if escape is pressed, the loop ends 

        screen.blit(instrPages[pageNum],(0,0))
        display.flip()
    return "menu" #return to the menu
        
def credit():
    running = True
    cred = image.load("startMenu/CreditsPage.png") #load the picuture
    screen.blit(cred,(0,0)) #blits the picture
    while running:
        for evt in event.get():          
            if evt.type == QUIT:
                running = False
        if key.get_pressed()[K_ESCAPE]: running = False

        display.flip()
    return "menu" #returns to menu when the loop is done
    

def story():
    running = True
    story=image.load("startMenu/Letterfull.png") #load the story picture
    screen.blit(story,(0,0)) #bliting the story
    while running:
        for evt in event.get():          
            if evt.type == QUIT:
                running = False
        if key.get_pressed()[K_ESCAPE]: running = False #if escape is pressed, the loop ends
        display.flip()
    return "menu" #returns to menu 
    


def menu():
    global beaScore,manScore,phyScore,cleanliness,happiness,hunger,days,turns
    pic=image.load("startMenu/home.png") #the start menu background
    startText=fontOne.render("Start",True,WHITE) 
    instructionsText=fontOne.render("Instructions",True,WHITE)
    creditsText=fontOne.render("Credits",True,WHITE)
    storyText=fontOne.render("Story",True,WHITE) #are we doing this?
    running = True
    myClock = time.Clock()
    buttons = [Rect(100,y*80+230,190,40) for y in range(4)] #the rects for the buttons
    vals = ["main","instructions","credits","story"] #the pages that can be returned in a list
    while running:
        for evt in event.get():          
            if evt.type == QUIT: #if the x is pressed, the exit page us returned so the game is closed
                return "exit"

        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        
        screen.blit(pic,(0,0)) #blit the background picture
        for r,v in zip(buttons,vals): 
            draw.rect(screen,lightPink,r) #draw the rectangles 
            if r.collidepoint(mpos): #if the mouse hovers over a rectange, the box is drawn as a darker pink
                draw.rect(screen,darkerPink,r,2)
                if mb[0]==1: #if the box is clicked, 
                    val=v #the value is taken to return
                    running=False #the loop ends
                    
            else: #if it the mouse is not over a box
                draw.rect(screen,darkPink,r,2) #a dark pink boarder is drawn
                screen.blit(startText,(155,237)) #and all the texts are blit
                screen.blit(instructionsText,(110,317))
                screen.blit(creditsText,(140,397))
                screen.blit(storyText,(155,477))
                
        display.flip()
    return val #when the loop ends, the page is returned

def contest():
    global beaScore,manScore,phyScore
    running=True
    winOrLose=False #variable to see if the user won or not, true if won, false if lost
    #find a random # between 0 and 1000 to help determine if the cat wins (will be explained later)
    bResult=randint(0,800)
    mResult=randint(0,800)
    pResult=randint(0,800)

    #if all three of the scores are over 800 then they automatically win because the random number is between 0 and 800 to win
    #but if all three were not over the 800, like in a real pet contest, the cat still has a chance to win
    #so there is a chance that the cat still wins, but the chance is smaller if the score is lower
    #the cat must win in all 3 categories to win
    print(bResult,mResult,pResult)
    print(beaScore,manScore,phyScore)
    if beaScore>bResult and manScore>= mResult and phyScore>=pResult: 
        winOrLose=True
    else:
        winOrLose=False
    timeRun=0 #keep track of how many loops have passed
    while timeRun<1000: #make a loop to spam 100 random colours to create drama
        for evt in event.get():          
            if evt.type == QUIT:
                running = False
        col=(randint(0,255),randint(0,255),randint(0,255))
        screen.fill(col)
        display.flip()
        timeRun+=1

    if winOrLose: #if win or lose if True, the player won 
        return "win" #and the win page can be used
    else:
        return "youLose"  #else, the player loses and they go to the lose screen

def youLose():
    running = True
    starveDeath=image.load("EndGame/death.png") #load all the lose screens
    unhappyLose=image.load("EndGame/Gameover.png")
    lostToMax=image.load("EndGame/Lose.png")

    while running:
        for evt in event.get():          
            if evt.type == QUIT:
                running = False
                
        if hunger==0: #if the hunger variable is 0, the cat starved to death
            screen.blit(starveDeath,(0,0)) #the pic is blit
        elif cleanliness==0: #if the cleanliness variable is 0, the cat ran away
            screen.blit(unhappyLose,(0,0)) 
        else: #if none of the others was the reason why the player was sent here, that means the player lost to Max
            screen.blit(lostToMax,(0,0))
            
        if key.get_pressed()[K_ESCAPE]: running = False #if escape is pressed, the loop ends
        display.flip()
        
    return "exit" #exits the game after 

def win():
    running = True
    winPic = image.load("EndGame/Win.png") #load the picuture
    headD=image.load("Sprite/idle cat thing001.png")
    headU=image.load("Sprite/idle cat thing002.png")
    screen.blit(winPic,(0,0)) #blits the picture
    winningD=60 #victry dance counter for loops
    while running:
        for evt in event.get():          
            if evt.type == QUIT:
                running = False
        if key.get_pressed()[K_ESCAPE]: running = False
        
        screen.blit(winPic,(0,0)) #blits the picture

        if winningD==0:
            winningD=60
        else:
            winningD-=1
        
        if winningD>30: #blits the head up if the counter is over 60
            screen.blit(headU,(300,100))
        else: #if its not over 30 then the head down is blit
            screen.blit(headD,(300,100))
        
            
        display.flip()
    return "exit" #game is over, so the we exit

screen = display.set_mode((800, 600))
running = True
x,y = 0,0
page = "menu"
while page != "exit":
    if page == "menu": #a page system where the functions return page names
        page = menu() #when the page name is given, it's cooresponding function is called
    if page == "main":
        page = main()
    if page == "instructions":
        page = instructions()    
    if page == "story":
        page = story()    
    if page == "credits":
        page = credit()
    if page == "appearanceMini":
        page=appearanceMini()
    if page == "cleaningMini":
        page = cleaningMini()
    if page == "mannersMini":
        page = mannersMini()
    if page == "eatingMini":
        page = eatingMini()
    if page == "physicalMini":
        page = physicalMini()
    if page == "contest":
        page = contest()
    if page== "youLose":
        page = youLose()
    if page== "win":
        page=win()

quit()


