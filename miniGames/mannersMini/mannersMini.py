#mannersMini.py

from random import *
from pygame import *
from math import *
from tkinter import *
init()
font=font.SysFont("Tw Cen MT Condensed Extra Bold",30)

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

col=(randint(0,20),randint(0,255),randint(0,255))

###Defining variables
size=(800,600) 
screen=display.set_mode(size)
myClock=time.Clock()
mannersLife=3
running=True
clicked=False
arrowNum=0
action=False
actionTime=20
mb=mouse.get_pressed()
commands=[] #list of the commands ###MUST REDEFINE AS EMPTY  
mannersScore=0


#pics
mannersBack=image.load("pics/New Piskel.png")

fJump1=image.load("pics/testSprite007.png")
fJump2=image.load("pics/testSprite008.png")
fJump3=image.load("pics/testSprite009.png")
fJumping=[fJump1,fJump2,fJump3]


bJump1=image.load("pics/testSprite043.png")
bJump2=image.load("pics/testSprite044.png")
bJump3=image.load("pics/testSprite045.png")
bJumping=[bJump1,bJump2,bJump3]

lWalk1=image.load("pics/testSprite013.png")
lWalk2=image.load("pics/testSprite014.png")
lWalk3=image.load("pics/testSprite015.png")
lWalking=[lWalk1,lWalk2,lWalk3]

rWalk1=image.load("pics/testSprite031.png")
rWalk2=image.load("pics/testSprite032.png")
rWalk3=image.load("pics/testSprite033.png")
rWalking=[rWalk1,rWalk2,rWalk3]

fJump=image.load("pics/testSprite108.png")
bJump=image.load("pics/testSprite144.png")
lWalk=image.load("pics/testSprite114.png")
rWalk=image.load("pics/testSprite132.png")
resting=image.load("pics/testSprite107.png")



rect1=Rect(240,450,50,50)
rect2=Rect(330,450,50,50)
rect3=Rect(420,450,50,50)
rect4=Rect(510,450,50,50)

#coresponding rect, coords of the box, first pic, second pic
arrowBoxes=[[rect1,(240,450),fJump1,fJump2,fJump],[rect2,(330,450),bJump1,bJump2,bJump],[rect3,(420,450),lWalk1,lWalk2,lWalk],[rect4,(510,450),rWalk1,rWalk2,rWalk]]


def mMiniBlit(): #function to blit the pictures
    screen.blit(mannersBack,(0,0))
    blitRect=Rect(250,100,300,300)
    blank=screen.subsurface(blitRect).copy() #a blank box of the where the big cat will be 
    screen.blit(resting,(250,100))
    restingPic=screen.subsurface(blitRect).copy() #pic with big cat and the backgroun

    for box in arrowBoxes:
        draw.rect(screen,MINT,box[0])
        screen.blit(box[2],box[1])
    back=screen.copy()#after everything has blit


def command():
    'add a command into the list and command it'
    global arrowNum
    arrowNum=0
    rectNum=0
    ran=randint(0,3)
    commands.append(arrowBoxes[ran])
    screen.blit(back,(0,0))
    speed=40
    done=[] #list of commands that have already been done

    
    while True:
        if len(done)==len(commands) and speed==0:
            break
        if speed==0:
            draw.rect(screen,GRAPE,commands[rectNum][0])
            screen.blit(commands[rectNum][3],commands[rectNum][1])
            done.append(commands[rectNum][0])
            rectNum+=1
            speed=40
        if speed==20:
            screen.blit(back,(0,0))
        speed-=1
            
        display.flip()
        myClock.tick(60)
    screen.blit(back,(0,0))


def check():
    'checks if the answer is right'
    global mannersLife,arrowNum,mannersScore
    rightAns=commands[arrowNum][0]
    for box in arrowBoxes:
        if box[0].collidepoint(mx,my) and clicked:
            if box[0]!=rightAns:
                mannersLife-=1
            elif box[0]==rightAns:
                mannersScore+=10+5*len(commands)
                if len(commands)-1==arrowNum:
                    command()
                    return 
                else:
                    arrowNum+=1
    if arrowBoxes[0][0].collidepoint(mx,my):
        screen.blit(blank,(250,100))
        screen.blit(arrowBoxes[0][4],(250,100))
        
    elif arrowBoxes[1][0].collidepoint(mx,my):
        screen.blit(blank,(250,100))
        screen.blit(arrowBoxes[1][4],(250,100))
        
    elif arrowBoxes[2][0].collidepoint(mx,my):
        screen.blit(blank,(250,100))
        
        screen.blit(arrowBoxes[2][4],(250,100))

    elif arrowBoxes[3][0].collidepoint(mx,my):
        screen.blit(blank,(250,100))
        screen.blit(arrowBoxes[3][4],(250,100))

    else:
        screen.blit(restingPic,(250,100))
                



def bliting():
    global arrowBoxes,mx,my
    ################screen.blit(blank,(250,100))
    scoreText=font.render("Score: "+str(mannersScore),True,BLACK)
    screen.blit(scoreText,(100,50))
    lifeText=font.render("Life: "+str(mannersLife),True,BLACK)
    screen.blit(lifeText,(100,100))
    for box in arrowBoxes:
        draw.rect(screen,MINT,box[0])
        screen.blit(box[2],box[1])
        if box[0].collidepoint((mx,my)):
            draw.rect(screen,GRAPE,box[0])
            screen.blit(box[3],box[1])    
         



def mannersMini():
    mannersLife=3
    running=True
    clicked=False
    arrowNum=0
    action=False
    actionTime=20
    mb=mouse.get_pressed()
    commands=[] #list of the commands ###MUST REDEFINE AS EMPTY  
    mannersScore=0
    mMiniBlit()
    command()
    while running:
        clicked=False
        
        for evt in event.get():

            if evt.type==QUIT:
                running=False
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1:
                    clicked=True
                    

        if mannersLife==0:
            running=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        
        
        
        bliting()
        check()

            
        display.flip()
        omx,omy=mx,my
        myClock.tick(60)
    return "menu"
    quit()



