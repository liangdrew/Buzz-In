#This program is meant to simulate buzzers for time-based team quiz games

import time
import sys
import pygame
from pygame.locals import *

print "Welcome to MakeyMakey Quiz by Andrew Liang."
print
time.sleep(0.5)
print "To set up, please ensure that the MakeyMakey breadboard is connected."
print
time.sleep(0.5)
#passover=raw_input("When ready, press the 'enter' key.")
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

pygame.mixer.pre_init(22050,-16,2,4096)
pygame.init()  
screensize=(600,400)
screen=pygame.display.set_mode(screensize)
pygame.display.set_caption("MaKeyMaKey Quiz by Andrew Liang")
background=pygame.Surface(screensize).convert()
background.fill((255,255,255))
blueSFX=pygame.mixer.Sound("audio/blueSFX.ogg")
redSFX=pygame.mixer.Sound("audio/redSFX.ogg")
greenSFX=pygame.mixer.Sound("audio/greenSFX.ogg")
yellowSFX=pygame.mixer.Sound("audio/yellowSFX.ogg")
blackSFX=pygame.mixer.Sound("audio/blackSFX.ogg")
clock=pygame.time.Clock()

loop=True
nextQ=1

blue_count=0      # Number of correct answers
red_count=0
green_count=0
yellow_count=0
black_count=0

blue_count_wrong=0     # Number of total attempts
red_count_wrong=0
green_count_wrong=0
yellow_count_wrong=0
black_count_wrong=0

blue_gate=1
red_gate=1
green_gate=1
yellow_gate=1
black_gate=1
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
         print "Red Team: ",red_count," correct ",red_count_wrong," attempted" 
         print "Blue Team: ",blue_count," correct ",blue_count_wrong," attempted"
         print "Green Team: ",green_count," correct ",green_count_wrong," attempted"
         print "Yellow Team: ",yellow_count," correct ",yellow_count_wrong," attempted"
         print "Black Team: ",black_count," correct ",black_count_wrong," attempted"
         print "--------------"
         print
            
      if nextQ==1:
                
         if ev.type==KEYDOWN:
            if ev.key == K_UP and blue_gate==1: #blue
               background.fill((0,0,255))
               pygame.display.set_caption("Blue Team!")
               print "Blue team!"
               blueSFX.play()
               name="blue"
               nextQ=0
               yes=1
               
            elif ev.key == K_RIGHT and red_gate==1: #red
               background.fill((255,51,51))
               pygame.display.set_caption("Red Team!")
               print "Red team!"
               redSFX.set_volume(0.6)
               redSFX.play()
               name="red"
               nextQ=0
               yes=1
               
            elif ev.key == K_DOWN and green_gate==1: #green
               background.fill((0,153,0))
               pygame.display.set_caption("Green Team!")
               print "Green team!"
               greenSFX.set_volume(0.6)
               greenSFX.play()
               name="green"
               nextQ=0
               yes=1
      
               
            elif ev.key == K_LEFT and yellow_gate==1: #yellow
               background.fill((255,255,102))
               pygame.display.set_caption("Yellow Team!")
               print "Yellow team!"
               yellowSFX.set_volume(0.6)
               yellowSFX.play()
               name="yellow"
               nextQ=0
               yes=1
               
            elif ev.key == K_SPACE and black_gate==1: #black
               background.fill((0,0,0))
               pygame.display.set_caption("Black Team!")
               print "Black team!"
               blackSFX.set_volume(0.6)
               blackSFX.play()
               name="black"
               nextQ=0
               yes=1
      
      if ev.type==KEYDOWN and ev.key==K_y and yes==1: #yes var is to gate y/n keys
         blue_gate=1
         red_gate=1
         green_gate=1
         yellow_gate=1
         black_gate=1
         background.fill((255,255,255))
         nextQ=1
         if name=="blue":
            blue_count+=1
            blue_count_wrong+=1
            print "-correct"
            yes=0
         if name=="red":
            red_count+=1
            red_count_wrong+=1
            print "-correct"
            yes=0
         if name=="green":
            green_count+=1
            green_count_wrong+=1
            print "-correct"
            yes=0
         if name=="yellow":
            yellow_count+=1
            yellow_count_wrong+=1
            print "-correct"
            yes=0
         if name=="black":
            black_count+=1
            black_count_wrong+=1
            print "-correct"
            yes=0
         print
      
      if ev.type==KEYDOWN and ev.key==K_n and yes==1:
         nextQ=1
         print "-incorrect"
         print
         background.fill((255,255,255))
         if name=="blue":
            blue_count_wrong+=1
            blue_gate=0
            yes=0
         if name=="red":
            red_count_wrong+=1
            red_gate=0
            yes=0
         if name=="green":
            green_count_wrong+=1
            green_gate=0
            yes=0
         if name=="yellow":
            yellow_count_wrong+=1
            yellow_gate=0
            yes=0
         if name=="black":
            black_count_wrong+=1
            black_gate=0
            yes=0
         
   screen.blit(background, (0,0))
   pygame.display.flip()
       
pygame.quit()
sys.exit()




    




