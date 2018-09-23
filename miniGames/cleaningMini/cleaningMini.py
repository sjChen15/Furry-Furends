#cleaningMini.py

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

size=(800,600) 
screen=display.set_mode(size)
#variables
coordsX,coordsY=283,200

#rects
cleanRect=(250,150,350,400)
scoreRect=(0,0,200,200)

#pics
background=image.load("background.png")
cat=image.load("pics/testSprite056.png")

dirty1=image.load("pics/dirty01.png")
dirty2=image.load("pics/dirty02.png")
dirty3=image.load("pics/dirty03.png")

soap=image.load("pics/soap.png") #cursor image

dirty=[dirty1,dirty2,dirty3]

def dMiniBlit(): #function to blit the pictures
    'blits the pictures for the cleaning mini'
    global clean,scoreBoard,aCopy
    screen.blit(background,(0,0)) #blit the background
    screen.blit(cat,(coordsX,coordsY)) #blit the animal
    clean=screen.subsurface(cleanRect).copy()
    scoreBoard=screen.subsurface(scoreRect).copy()
    aCopy=screen.copy()
    
def makeDirty():
    ran=randint(0,len(dirty)-1)
    boxX=randint(300,500)
    boxY=randint(250,400)
    rnBox=Rect(boxX,boxY,60,60) 
    
    screen.blit(clean,(250,150))
    screen.blit(dirty[ran],(boxX,boxY))
    return rnBox,ran

def throwOut(ran):
    TOX=randint(600,625)
    TOY=randint(400,425)
    screen.blit(dirty[ran],(TOX,TOY))

def blitPics():
    global aCopy
    screen.blit(aCopy,(0,0))
    scoreText=font.render("Score: "+str(score),True,WHITE)
    lifeText=font.render("Live: "+str(life),True,WHITE)
    timeText=font.render("Time: "+str(seconds),True,WHITE)
    screen.blit(scoreBoard,(0,0))
    screen.blit(scoreText,(10,50))
    screen.blit(lifeText,(10,20))
    screen.blit(timeText,(10,80))
    
    screen.blit(soap,(mx-10,my-10))
    aCopy=screen.copy()
    
def cleaningMini():
    global score,life,seconds,mx,my,aCopy
    dMiniBlit()
    currentRect=Rect(0,0,10,10)
    currentRect,currentDirty=makeDirty()
    running=True 
    myClock=time.Clock()
    mx,my=0,0
    timer=500
    score=0
    life=3
    seconds=60
    secondsCounter=60
    col=screen.get_at((0,0))
    #rects
    cleanRect=(250,150,350,400)
    scoreRect=(0,0,200,200)
    aCopy=screen.copy()
    while running:
        clicked=False
        
        for evt in event.get():

            if evt.type==QUIT:
                running=False
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1:
                    clicked=True

        aCopy=screen.copy()
        if seconds==0:
            running=False
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()

        blitPics()
        
        if currentRect.collidepoint(mx,my) and clicked:
            currentRect,currentDirty=makeDirty()
            throwOut(currentDirty)
            score+=1
        elif clicked:
            life-=1

        if life==0:
            running=False

        if secondsCounter==0:
            secondsCounter=60
            seconds-=1
        else:
            secondsCounter-=1
            
        
        
        display.flip()
        omx,omy=mx,my
        myClock.tick(60)
    quit()
    return "main"


cleaningMini()
