import pygame, random, time, sys

#Creating my first game window
#intialze the pygame

pygame.init()
# creat the sceen that we can see
d = 20

screen = pygame.display.set_mode((800,600))  # the high and weigh

# changing the title, logo, and the background color  or the background by image

caption = "WAR"      #caption
pygame.display.set_caption(caption)
# logo
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)
# backggrond
background = pygame.image.load("background.jpg")
# set player image  PLAYER

Player = pygame.image.load("rocket.png")
playerX = 370
playerY = 500
playerChangeX = 0
playerChangeY = 0
#CORONA
# hiện thị nhiều corona :
corona = pygame.image.load("virus.png")
coronaX = []
coronaY = []
coronaChangeX = []
coronaChangeY =  []
for i in range(6):
    coronaX.append(random.randrange(1,81))
    coronaY.append(random.randrange(1,41))
    coronaChangeX.append(0.5)
    coronaChangeY.append(0)

# bullet

Bullet = pygame.image.load("bullet.png")
bulletX = playerX
bulletY = playerY
bulletChangeX = 0
bulletChangeY = 0
bulletStatus = False

# điểm
score = 0
# GAME OVER

# hiện thị điểm

def Show_score(choice = 1 ):
    if choice == 1:
        font = pygame.font.Font("freesansbold.ttf", 20)
        x = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(x, (10, 10))
    else:
        font = pygame.font.Font("freesansbold.ttf", 70)
        x = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(x, (270, 250 ))
# hiện thị  player
def Show_player(x,y):
    screen.blit(Player, (x, y))
#hiện thị corona
def Show_corona(x,y):
    screen.blit(corona, (x*10,y*10))
#hien thi dan:
def Show_bullet(x,y):
    global bulletStatus
    bulletStatus = True
    screen.blit(Bullet, (x, y))
# tính khoảng cách :
def Distance(coronaX, coronaY, bulletX, bulletY):      # để quyết định là trúng hay chưa !
    from math import sqrt
    distance = sqrt((bulletX-coronaX)**2 + (bulletY - coronaY)**2)
    if distance <= 20 :
        return True
    else : return False
# hiện thị Game over text:

def GAMEOVER():
    Show_score(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

# GAME LOOP
running = True
while running:
    pygame.time.delay(50)
    #screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # di chuyển người chơi
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChangeX = -d
            if event.key == pygame.K_RIGHT:
                playerChangeX  = d
            if event.key == pygame.K_DOWN:
                playerChangeY  = d
            if event.key == pygame.K_UP:
                playerChangeY  = -d
            if event.key == pygame.K_SPACE:
                if bulletStatus is False :
                    bulletX = playerX
                    bulletY = playerY
                    Show_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:        #giữ cho nó liên tục khi giữ nút
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChangeX =0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerChangeY =0

    # giữ cho người chơi trong màn hình
    playerX +=playerChangeX
    playerY+=playerChangeY
    if playerX >=736 : playerX =736
    if playerX <=0 : playerX =0
    if playerY >=535 :playerY =535
    if playerY <=0 : playerY =0

    # hiện thị người chơi
    Show_player(playerX, playerY)

        # di chuyển virus  :
    for i in range(6):
        if Distance(coronaX[i]*10, coronaY[i]*10 , playerX, playerY) :
            for j in range(6):
                coronaY[j] = 2000
                GAMEOVER()

        coronaX[i] += coronaChangeX[i]
        if coronaX[i]*10 >= 736 :
            coronaChangeX[i] = -0.5
            coronaY[i] += 1
        if coronaX[i]*10 <=0 :
            coronaChangeX[i] = 0.5
            coronaY[i] += 1
        #hiện thị virus:
        Show_corona(coronaX[i], coronaY[i])
        """
        #sinh tiếp corona : T_T:
        coronaX = random.randrange(1, 81)
        coronaY = random.randrange(1, 41)
        """
        trungdan = Distance(coronaX[i] * 10 , coronaY[i] * 10 , bulletX, bulletY)
        if trungdan :
            bulletY = 500
            bulletStatus = False
            score += 10
            # random lại virus :
            coronaX[i] = random.randrange(1, 81)
            coronaY[i] = random.randrange(1, 41)
        #else: print ("NOT ")
     # di chuyen dan :
    if bulletY <= 0:
        bulletY = playerY
        bulletX = playerX
        bulletStatus = False
    if bulletStatus == True:
        Show_bullet(bulletX, bulletY)
        bulletY -= 20
    Show_score(1)
    # BẮT BUỘC PHẢI CÓ Á
    pygame.display.update()
    pygame.display.flip()