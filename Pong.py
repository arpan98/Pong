import pygame
import random
import math
import time
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
 
pygame.init()
 
size = (800, 500)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Pong!")
font=pygame.font.SysFont('Calibri',25,True,False)
clock = pygame.time.Clock()
done=False
speed_player=0
speed_ai=0
y_player=210
y_ai=210
score_player=0
score_ai=0
x_circle=400
y_circle=250
speed_circle_x=0
speed_circle_y=4
reset=True
 
while not done:                         #main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #quit
            done = True

        if event.type==pygame.KEYDOWN:      #Key press
            if event.key==pygame.K_UP:
                speed_player=-7
            if event.key==pygame.K_DOWN:
                speed_player=7

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:  
                speed_player=0
            if event.key==pygame.K_DOWN:
                speed_player=0


    
    if reset==True:                    #reset
        x_circle=400
        y_circle=250
        a=random.randrange(2)+7
        b=random.randrange(2)+8
        m1=-1
        m2=random.randrange(-1,2,2)
        reset=False
        speed_circle_x=m1*a
        speed_circle_y=m2*b

    #---- AI ---
    if y_circle>y_ai+40:
        speed_ai=7
    if y_circle<y_ai+40:
        speed_ai=-7
    
    
    if x_circle<40 and speed_circle_x<0:    #player point
        score_player+=1
        reset=True
        time.sleep(0.5)
    if x_circle>760 and speed_circle_x>0:   #ai point
        score_ai+=1
        reset=True
        time.sleep(0.5)
    if y_circle<10 and speed_circle_y<0:     #reflect up
        speed_circle_y=b
        y_circle=10
    if y_circle>490 and speed_circle_y>0:   #reflect down
        speed_circle_y=-b
        y_circle=490
    if x_circle>=733 and x_circle<=739 and speed_circle_x>0 and y_circle>=y_player-6 and y_circle<=y_player+86:
        if speed_player>0:
            speed_circle_y+=1
        if speed_player<0:
            speed_circle_y-=1
        speed_circle_x=-a
    if x_circle>=53 and x_circle<=59 and speed_circle_x<0 and y_circle>=y_ai-6 and y_circle<=y_ai+86:
        speed_circle_x=a

    screen.fill(BLACK)

    if score_ai==20:
        done=True
        text=font.render("Computer won "+str(score_ai) + " - " + str(score_player),True,WHITE)
        screen.blit(text,[250,235])
    elif score_player==20:
        done=True
        text=font.render("You won "+str(score_player) + " - " + str(score_ai),True,WHITE)
        screen.blit(text,[270,235])

    if done==False:
    # --- Drawing code should go here
        text2=font.render(str(score_player),True,WHITE)
        text1=font.render(str(score_ai),True,WHITE)
        screen.blit(text1,[350,10])
        screen.blit(text2,[430,10])
    
        if y_player>420 and speed_player>0:
            speed_player=0
            y_player=420
        if y_player<0 and speed_player<0:
            speed_player=0
            y_player=0
        if y_ai>420 and speed_ai>0:
            speed_ai=0
            y_ai=420
        if y_ai<0 and speed_ai<0:
            speed_ai=0
            y_ai=0
        y_player+=speed_player

        x_circle+=speed_circle_x
        y_circle+=speed_circle_y
        pygame.draw.circle(screen,GREEN,[x_circle,y_circle],6,3)
    
        pygame.draw.rect(screen,BLUE,[750,y_player,10,80]) #player

        y_ai+=speed_ai     
        pygame.draw.rect(screen,RED,[40,y_ai,10,80])   #ai
        
        pygame.draw.line(screen,WHITE,[400,0],[400,500],2)
 
    pygame.display.flip()
 
    clock.tick(60)
time.sleep(3)
pygame.quit()
