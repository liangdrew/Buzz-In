#This program is meant to simulate buzzers for time-based team quiz games

import time, sys, pygame
from pygame.locals import *

print "Welcome to MakeyMakey Quiz by Andrew Liang."
print
time.sleep(0.5)
print "To set up, please ensure that the MakeyMakey breadboard is connected."
print
time.sleep(0.5)
passover=raw_input("When ready, press the 'enter' key.")
print
time.sleep(0.5)
print "Let's begin!"
time.sleep(0.5)
print
print "INSTRUCTIONS"
print "---------------"
print "Press 'Y' if the answer is correct and 'N' if incorrect."
print "Press 'P' at any time to print scores."
print "Press 'ESC' to exit the program."
print

pygame.mixer.pre_init(22050,-16,2,1024)
pygame.init()  
screensize=(600,400)
screen=pygame.display.set_mode(screensize)
pygame.display.set_caption("MaKeyMaKey Quiz by Andrew Liang")
background=pygame.Surface(screensize).convert()
background.fill((255,255,255))
blueSFX=pygame.mixer.Sound("blueSFX.ogg")
redSFX=pygame.mixer.Sound("redSFX.ogg")
greenSFX=pygame.mixer.Sound("greenSFX.ogg")
yellowSFX=pygame.mixer.Sound("yellowSFX.ogg")
blackSFX=pygame.mixer.Sound("blackSFX.ogg")
clock=pygame.time.Clock()

loop=True
nextQ=1
bluecount=0
bluecountwrong=0 #total attempts
redcount=0
redcountwrong=0
greencount=0
greencountwrong=0
yellowcount=0
yellowcountwrong=0
blackcount=0
blackcountwrong=0
bluegate=1
redgate=1
greengate=1
yellowgate=1
blackgate=1
name=""
yes=0

while loop:
   clock.tick(30)
   
   for ev in pygame.event.get():
      
      if ev.type==QUIT:
         loop=False
         print "See you next time."
      if ev.type==KEYDOWN and ev.key==K_ESCAPE:
         loop=False
         print "See you next time."
      if ev.type==KEYDOWN and ev.key==K_p:
         print
         print "Scores:"
         print "--------------"
         print "Red Team: ",redcount," correct ",redcountwrong," attempted" 
         print "Blue Team: ",bluecount," correct ",bluecountwrong," attempted"
         print "Green Team: ",greencount," correct ",greencountwrong," attempted"
         print "Yellow Team: ",yellowcount," correct ",yellowcountwrong," attempted"
         print "Black Team: ",blackcount," correct ",blackcountwrong," attempted"
         print "--------------"
         print
            
      if nextQ==1:
                
         if ev.type==KEYDOWN:
            if ev.key == K_UP and bluegate==1: #blue
               background.fill((0,0,255))
               pygame.display.set_caption("Blue Team!")
               print "Blue team!"
               blueSFX.play()
               name="blue"
               nextQ=0
               yes=1
               
            elif ev.key == K_RIGHT and redgate==1: #red
               background.fill((255,51,51))
               pygame.display.set_caption("Red Team!")
               print "Red team!"
               redSFX.set_volume(0.6)
               redSFX.play()
               name="red"
               nextQ=0
               yes=1
               
            elif ev.key == K_DOWN and greengate==1: #green
               background.fill((0,153,0))
               pygame.display.set_caption("Green Team!")
               print "Green team!"
               greenSFX.set_volume(0.6)
               greenSFX.play()
               name="green"
               nextQ=0
               yes=1
      
               
            elif ev.key == K_LEFT and yellowgate==1: #yellow
               background.fill((255,255,102))
               pygame.display.set_caption("Yellow Team!")
               print "Yellow team!"
               yellowSFX.set_volume(0.6)
               yellowSFX.play()
               name="yellow"
               nextQ=0
               yes=1
               
            elif ev.key == K_SPACE and blackgate==1: #black
               background.fill((0,0,0))
               pygame.display.set_caption("Black Team!")
               print "Black team!"
               blackSFX.set_volume(0.6)
               blackSFX.play()
               name="black"
               nextQ=0
               yes=1
      
      if ev.type==KEYDOWN and ev.key==K_y and yes==1: #yes var is to gate y/n keys
         bluegate=1
         redgate=1
         greengate=1
         yellowgate=1
         blackgate=1
         background.fill((255,255,255))
         nextQ=1
         if name=="blue":
            bluecount+=1
            bluecountwrong+=1
            print "-correct"
            yes=0
         if name=="red":
            redcount+=1
            redcountwrong+=1
            print "-correct"
            yes=0
         if name=="green":
            greencount+=1
            greencountwrong+=1
            print "-correct"
            yes=0
         if name=="yellow":
            yellowcount+=1
            yellowcountwrong+=1
            print "-correct"
            yes=0
         if name=="black":
            blackcount+=1
            blackcountwrong+=1
            print "-correct"
            yes=0
         print
      
      if ev.type==KEYDOWN and ev.key==K_n and yes==1:
         nextQ=1
         print "-incorrect"
         print
         background.fill((255,255,255))
         if name=="blue":
            bluecountwrong+=1
            bluegate=0
            yes=0
         if name=="red":
            redcountwrong+=1
            redgate=0
            yes=0
         if name=="green":
            greencountwrong+=1
            greengate=0
            yes=0
         if name=="yellow":
            yellowcountwrong+=1
            yellowgate=0
            yes=0
         if name=="black":
            blackcountwrong+=1
            blackgate=0
            yes=0
         
   screen.blit(background, (0,0))
   pygame.display.flip()
       
pygame.quit()
sys.exit()




    




