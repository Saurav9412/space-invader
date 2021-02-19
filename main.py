import pygame
import random
import math
pygame.init()
#creating the window
window=pygame.display.set_mode((800,600))
#title
pygame.display.set_caption('Space Invader')
#logo
logo=pygame.image.load('shuttle.png')
pygame.display.set_icon(logo)
#title image
#image=pygame.image.load('images.png')
##imageY=0

#background
background=pygame.image.load('background.png')
background=pygame.transform.scale(background,(800,600))
#spaceship
turn=random.randint(0,3)
if turn == 0:
    ship=pygame.image.load('battleship.png')
if turn == 1:
    ship=pygame.image.load('spaceship.png')
if turn == 2:
    ship=pygame.image.load('spaceship1.png')
if turn == 3:
    ship=pygame.image.load('s.png')
playerX=370
playerY=480
playerX_move=0
playerY_move=0

#enemy ships
enemyship=[]
enemyX=[]
enemyY=[]
enemyX_move=[]
enemyY_move=[]
no_of_enemies=5
for i in range (no_of_enemies):
    if i==0:
        enemyship.append(pygame.image.load('alienn.png'))
    if i==1:
        enemyship.append(pygame.image.load('alien.png'))
    if i==2:
        enemyship.append(pygame.image.load('alien1.png'))
    if i==3:
        enemyship.append(pygame.image.load('alien2.png'))
    if i==4:
        enemyship.append(pygame.image.load('alien3.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,150))
    enemyX_move.append(4.5)
    enemyY_move.append(30)


#bullet
bullet=pygame.image.load('gun.png')
bulletX=0
bulletY=480
bullet_state='ready'
bulletX_move=0
bulletY_move=9

#score
score_count=0
scoreX=10
scoreY=10

#def title_image(x,y):
#    window.blit(image,(x,y))

def score(x,y):
    font=pygame.font.Font(None,25)
    score=font.render("SCORE:"+str(score_count),True,(255,255,255))
    window.blit(score,(x,y))

def player(x,y):
    window.blit(ship,(x,y))

def enemy(x,y,i):
    window.blit(enemyship[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    window.blit(bullet,(x+16,y+10))
    bullet_state='fire'

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(bulletX-enemyX,2)+math.pow(bulletY-enemyY,2))
    if distance<=32:
        return True
    else:
        return False


running=True
while running:
    window.blit(background,(0,0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running=False
        #movment when button is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_move= -5
            if event.key == pygame.K_RIGHT:
                playerX_move= 5
            if event.key == pygame.K_UP:
                playerY_move= -5
            if event.key == pygame.K_DOWN:
                playerY_move= 5
            if event.key == pygame.K_SPACE:
                if bullet_state=='ready':
                    bulletX=playerX
                    bulletY=playerY
                    fire_bullet(bulletX,playerY)
        #stop when button is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_move=0
            if event.key == pygame.K_RIGHT:
                playerX_move=0
            if event.key == pygame.K_UP:
                playerY_move=0
            if event.key == pygame.K_DOWN:
                playerY_move=0

    playerX+=playerX_move
    playerY+=playerY_move
    #setting up boundries
    if playerX>736:
        playerX=736
    elif playerX<0:
        playerX=0
    if playerY>536:
        playerY=536
    elif playerY<0:
        playerY=0

    #enemy movement
    for i in range (no_of_enemies):
        enemyX[i]+=enemyX_move[i]
        if enemyX[i]>736:
            enemyX_move[i]= -4.5
            enemyY[i]+=enemyY_move[i]
        if enemyX[i]<0:
            enemyX_move[i]=4.5
            enemyY[i]+=enemyY_move[i]
        collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            score_count+=1
            bulletY=playerY
            bulletX=playerX
            bullet_state='ready'
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(0,150)


        enemy(enemyX[i],enemyY[i],i)

    #bullet movment
    if bullet_state == 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_move
        if bulletY<=0:
            bullet_state='ready'
            bulletY=480
    #title_image(imageX,imageY)
    score(scoreX,scoreY)
    player(playerX,playerY)

    pygame.display.update()
