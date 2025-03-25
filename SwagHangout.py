import pygame
import sys
gameover = False
while True:
    playercount = int(input("how many players do you want?\n"))
    if playercount < 0 or playercount > 4:
        print("choose a number 1-4")
    else:
        break
pygame.init()
screen = pygame.display.set_mode((1280, 720))
background = pygame.image.load('graphics\\background.bmp')
clock = pygame.time.Clock() 
objects = []

class Playa:
    def __init__(self,img,x,y,height,speed):
        self.img = img
        self.x = x
        self.y = y
        self.height = height
        self.pos = img.get_rect().move(self.x,self.y)
        self.speed = speed
    def hustle(self,x,y):
        self.pos = self.pos.move(x,y)

playas = []        
if playercount > 0:        
    player = pygame.image.load('graphics\\playa.png')        
    playa = Playa(player,100,10,100,3)
    objects.append(playa)
if playercount > 1:
    player2 = pygame.image.load('graphics\\player2.png')
    playa2 = Playa(player2,900,500,100,3)
    objects.append(playa2)
if playercount > 2:
    player3 = pygame.image.load('graphics\\player3.png')
    playa3 = Playa(player3,400,400,100,3)
    objects.append(playa3)
if playercount > 3:
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"{joystick.get_name()} Connected")
    else:
        joystick = None
        print("No controller detected for player 4")
    player4 = pygame.image.load('graphics\\player4.png')
    playa4 = Playa(player4,200,200,100,3)
    objects.append(playa4)

while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    keys = pygame.key.get_pressed()
    if playercount > 0:
        if keys[pygame.K_w]:
            playa.hustle(0,(0-playa.speed))
        if keys[pygame.K_s]:
            playa.hustle(0,playa.speed)
        if keys[pygame.K_d]:
            playa.hustle(playa.speed,0)
        if keys[pygame.K_a]:
            playa.hustle((0-playa.speed),0)

    if playercount > 1:
        if keys[pygame.K_UP]:
            playa2.hustle(0,(0-playa2.speed))
        if keys[pygame.K_DOWN]:
            playa2.hustle(0,playa2.speed)
        if keys[pygame.K_RIGHT]:
            playa2.hustle(playa2.speed,0)
        if keys[pygame.K_LEFT]:
            playa2.hustle((0-playa2.speed),0)
    
    if playercount > 2:
        if keys[pygame.K_y]:
            playa3.hustle(0,(0-playa3.speed))
        if keys[pygame.K_h]:
            playa3.hustle(0,playa3.speed)
        if keys[pygame.K_j]:
            playa3.hustle(playa3.speed,0)
        if keys[pygame.K_g]:
            playa3.hustle((0-playa3.speed),0)    
    
    if joystick:
        stickx = joystick.get_axis(0)
        sticky = joystick.get_axis(1)
        playa4.hustle(stickx*playa4.speed,sticky*playa4.speed)
        
    if keys[pygame.K_BACKQUOTE]:
        command = input("enter command      ")
        try:
            exec(command)
        except:
            print("command failed")
            
    pygame.display.flip()
    for o in objects:
        screen.blit(background, (0, 0))
    for o in objects:
        screen.blit(o.img, o.pos)
    if playercount == 0:
        screen.blit(background, (0, 0))
    pygame.display.update
    clock.tick(60)
    
