import random
import time
import pygame

pygame.init()

display_width = 1000
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (220, 0, 0)
orange = (255, 140, 0)
green = (0, 150, 0)
blue = (0, 0, 255)
yellow = (245, 245, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Chase's Trash Adventure")

clock = pygame.time.Clock()

puppyImg = pygame.image.load('chase200.png')
background = pygame.image.load('trash.png')
coffeeImg = pygame.image.load('coffee.png')
tamponImg = pygame.image.load('tampon.png')
cocaImg = pygame.image.load('coca.png')
catFoodImg = pygame.image.load('catfood.png')
yum1Img = pygame.image.load('yum1.png')
yum2Img = pygame.image.load('yum2.png')
yum3Img = pygame.image.load('yum3.png')
yum4Img = pygame.image.load('yum4.png')
warn1Img = pygame.image.load('warn1.png')
warn2Img = pygame.image.load('warn2.png')
warn3Img = pygame.image.load('warn3.png')
warn4Img = pygame.image.load('warn4.png')
warn5Img = pygame.image.load('warn5.png')
speedup1Img = pygame.image.load('speedup1.png')
speedup2Img = pygame.image.load('speedup2.png')
speedup3Img = pygame.image.load('speedup3.png')
speedup4Img = pygame.image.load('speedup4.png')
speedup5Img = pygame.image.load('speedup5.png')
frameImg = pygame.image.load('frame.png')
start1Img = pygame.image.load('start1.png')
start2Img = pygame.image.load('start2.png')
starthoverImg = pygame.image.load('starthover.png')
chase1Img = pygame.image.load('chase1.png')
chasehoverImg = pygame.image.load('chasehover.png')


def puppy(x, y):
    gameDisplay.blit(puppyImg, (x, y))

def chase1(x, y):
    gameDisplay.blit(chase1Img, (x, y))

def chasehover(x, y):
    gameDisplay.blit(chasehoverImg, (x, y))


def tampon(x, y):
    gameDisplay.blit(tamponImg, (x, y))


def coffee(x, y):
    gameDisplay.blit(coffeeImg, (x, y))


def coca(x, y):
    gameDisplay.blit(cocaImg, (x, y))


def catfood(x, y):
    gameDisplay.blit(catFoodImg, (x, y))


def yum1(x, y):
    gameDisplay.blit(yum1Img, (x, y))


def yum2(x, y):
    gameDisplay.blit(yum2Img, (x, y))


def yum3(x, y):
    gameDisplay.blit(yum3Img, (x, y))


def yum4(x, y):
    gameDisplay.blit(yum4Img, (x, y))


def warn1(x, y):
    gameDisplay.blit(warn1Img, (x, y))


def warn2(x, y):
    gameDisplay.blit(warn2Img, (x, y))


def warn3(x, y):
    gameDisplay.blit(warn3Img, (x, y))


def warn4(x, y):
    gameDisplay.blit(warn4Img, (x, y))


def warn5(x, y):
    gameDisplay.blit(warn5Img, (x, y))


def speedup1(x, y):
    gameDisplay.blit(speedup1Img, (x, y))


def speedup2(x, y):
    gameDisplay.blit(speedup2Img, (x, y))


def speedup3(x, y):
    gameDisplay.blit(speedup3Img, (x, y))


def speedup4(x, y):
    gameDisplay.blit(speedup4Img, (x, y))


def speedup5(x, y):
    gameDisplay.blit(speedup5Img, (x, y))


def frame(x, y):
    gameDisplay.blit(frameImg, (x, y))


def start1(x, y):
    gameDisplay.blit(start1Img, (x, y))


def start2(x, y):
    gameDisplay.blit(start2Img, (x, y))


def starthover(x, y):
    gameDisplay.blit(starthoverImg, (x, y))


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text, placement, size, color):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((display_width / 2), placement)
    gameDisplay.blit(TextSurf, TextRect)


def pause_game(pause):
    while pause is True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    pause = False
        gameDisplay.blit(background, (0, 0))
        frame(200, 100)
        message_display("Pause", 275, 70, black)
        pygame.display.update()
        clock.tick(10)


def start_menu():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(background, (0, 0))
        frame(200, 100)
        message_display("Chase's Trash Adventure", 175, 35, black)

        mouse = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            start2(305, 230)
            chase1(515, 230)
        elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            starthover(300, 225)
            chase1(515, 230)
            pygame.display.update()
            clock.tick(30)
            game_loop()
        elif 480 > mouse[0] > 300 and 405 > mouse[1] > 225:
            if event.type == pygame.MOUSEBUTTONDOWN:
                start2(305, 230)
                chase1(515, 230)
                pygame.display.update()
                clock.tick(30)
            elif event.type == pygame.MOUSEBUTTONUP:
                starthover(300, 225)
                chase1(515, 230)
                pygame.display.update()
                clock.tick(30)
                game_loop()
            else:
                starthover(300, 225)
                chase1(515, 230)
                pygame.display.update()
                clock.tick(30)
        elif 675 > mouse[0] > 560 and 390 > mouse[1] > 245:
            if event.type == pygame.MOUSEBUTTONDOWN:
                puppy(520, 235)
                start1(300, 225)
                pygame.display.update()
                clock.tick(30)
            elif event.type == pygame.MOUSEBUTTONUP:
                chasehover(515, 230)
                start1(300, 225)
                pygame.display.update()
                clock.tick(30)
            else:
                start1(300, 225)
                chasehover(515, 230)
                pygame.display.update()
                clock.tick(30)

        else:
            start1(300, 225)
            chase1(515, 230)
        pygame.display.update()
        clock.tick(30)


def score_board(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Cat Food Eaten: " + str(count), True, white)
    gameDisplay.blit(text, (10, 10))


def stomach_ache(count):
    font = pygame.font.SysFont(None, 25)
    if count == 0:
        acheText = font.render("Stomach Ache: [                     ]", True, green)
        gameDisplay.blit(acheText, (10, 30))
    elif count == 1:
        acheText = font.render("Stomach Ache: [///////////          ]", True, yellow)
        gameDisplay.blit(acheText, (10, 30))
    elif count == 2:
        acheText = font.render("Stomach Ache: [////////////////     ]", True, orange)
        gameDisplay.blit(acheText, (10, 30))
    elif count == 3:
        acheText = font.render("Stomach Ache: [/////////////////////]", True, red)
        gameDisplay.blit(acheText, (10, 30))


def tamponeaten(count):
    frame(200, 100)
    message_display("Gross!! You Ate a Tampon..", 185, 35, black)
    message_display("Score: " + str(count), 275, 45, green)
    message_display("GAME OVER", 390, 50, red)
    tampon(300, 210)
    tampon(643, 208)
    pygame.display.update()
    time.sleep(4)

    game_loop()


def too_much(count):
    frame(200, 100)
    message_display("Your Stomach Really Hurts..", 175, 35, black)
    message_display("Oh No! You Shit on the Rug!", 205, 25, black)
    message_display("Score: " + str(count), 275, 40, green)
    message_display("GAME OVER", 390, 55, (200, 0, 0))
    coca(285, 240)
    puppy(560, 200)

    pygame.display.update()
    time.sleep(4.5)

    game_loop()


def game_loop():
    catFoodEaten = 0
    cocaEaten = 0
    iCatFood = 0
    iCoca = 0
    iCoffee = 0
    x = (display_width * 0.45)
    y = (display_height * 0.745)
    x_change = 0
    levelChange = 1
    chaseSpeed = 3
    tamponSpeed = 8
    cocaSpeed = random.randrange(4)
    coffeeSpeed = random.randrange(4)
    catfoodSpeed = random.randrange(4)
    tampony = -6000
    tamponx = random.randrange(0, display_width - 45)
    coffeey = -95
    coffeex = random.randrange(0, display_width - 45)
    cocay = -94
    cocax = random.randrange(0, display_width - 100)
    catfoody = -42
    catfoodx = random.randrange(0, display_width - 75)
    eatCoffee = False
    eatCoca = False
    eatCatFood = False

    gameExit = False


    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -chaseSpeed
                elif event.key == pygame.K_RIGHT:
                    x_change = chaseSpeed

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and x_change < 0:
                    x_change = -chaseSpeed
                if event.key == pygame.K_RIGHT and x_change > 0:
                    x_change = 0
                if event.key == pygame.K_LEFT and x_change < 0:
                    x_change = 0
                if event.key == pygame.K_LEFT and x_change > 0:
                    x_change = chaseSpeed
                if event.key == pygame.K_p:
                    pause = True
                    pause_game(pause)
        x += x_change
        if x + 50 <= tamponx <= x + 150:
            if display_height - 148 < tampony < display_height - 30:
                tamponeaten(catFoodEaten)
                x -= x_change
        if x > display_width * .84 or x < - 40:
            x -= x_change  # stops chase from moving
        gameDisplay.blit(background, (0, 0))
        puppy(x, y)
        if -4000 <= tampony < display_height:
            tampony += tamponSpeed + levelChange
        else:
            tamponSpeed = 7 + levelChange
            tamponx = random.randrange(0, display_width - 45)
            tampony = -2000
        if -250 <= coffeey < display_height:
            coffeey += coffeeSpeed + levelChange
        else:
            coffeeSpeed = random.randrange(4) + levelChange
            coffeex = random.randrange(0, display_width - 45)
            coffeey = -200
        if -148 <= cocay < display_height:
            cocay += cocaSpeed + levelChange
        else:
            cocaSpeed = random.randrange(4) + levelChange
            cocax = random.randrange(0, display_width - 100)
            cocay = -148
        if -148 <= catfoody < display_height:
            catfoody += catfoodSpeed + levelChange
        else:
            catfoodSpeed = random.randrange(4) + levelChange
            catfoodx = random.randrange(0, display_width - 75)
            catfoody = -42
        tampon(tamponx, tampony)
        if eatCoca is True:
            iCoca += 1
        if eatCatFood is True:
            iCatFood += 1
        if eatCoffee is True:
            iCoffee += 1
        if x + 10 <= coffeex <= x + 170:
            if coffeey > display_height - 140:
                eatCoffee = True
                if 0 <= iCoffee < 5:
                    speedup1(coffeex, display_height - 120)
                    if iCoffee == 1:
                        chaseSpeed += 1.5
                elif 5 <= iCoffee < 10:
                    speedup2(coffeex, display_height - 120)
                elif 10 <= iCoffee < 15:
                    speedup3(coffeex, display_height - 120)
                elif 15 <= iCoffee < 20:
                    speedup4(coffeex, display_height - 120)
                elif 20 <= iCoffee < 25:
                    speedup5(coffeex, display_height - 120)
                elif iCoffee >= 25:
                    eatCoffee = False
                    iCoffee = 0
                    coffeey = -200
                    coffeex = random.randrange(0, display_width - 100)
            elif eatCoffee is False:
                coffee(coffeex, coffeey)
        if iCoffee >= 25:
            eatCoffee = False
            iCoffee = 0
            coffeey = -200
            coffeex = random.randrange(0, display_width - 100)
        elif eatCoffee is False:
            coffee(coffeex, coffeey)

        if x + 30 <= cocax <= x + 150:
            if cocay > display_height - 120:
                eatCoca = True
                if 0 <= iCoca < 5:
                    warn1(cocax, display_height - 120)
                    if iCoca == 1:
                        cocaEaten += 1
                elif 5 <= iCoca < 10:
                    warn2(cocax, display_height - 120)
                elif 10 <= iCoca < 15:
                    warn3(cocax, display_height - 120)
                elif 15 <= iCoca < 20:
                    warn4(cocax, display_height - 120)
                elif 20 <= iCoca < 25:
                    warn5(cocax, display_height - 120)
                elif iCoca >= 25:
                    eatCoca = False
                    iCoca = 0
                    cocay = -94
                    cocax = random.randrange(0, display_width - 100)
            elif eatCatFood is False:
                coca(cocax, cocay)
        if iCoca >= 25:
            eatCoca = False
            iCoca = 0
            cocay = -94
            cocax = random.randrange(0, display_width - 100)
        elif eatCoca is False:
            coca(cocax, cocay)
        if cocaEaten == 3:
            too_much(catFoodEaten)

        if x + 30 <= catfoodx <= x + 150:
            if catfoody > display_height - 150:
                eatCatFood = True
                if 0 <= iCatFood < 5:
                    yum1(catfoodx, display_height - 100)
                    if iCatFood == 3:
                        catFoodEaten += 1
                        levelChange += 0.2
                elif 5 <= iCatFood < 10:
                    yum2(catfoodx, display_height - 100)
                elif 10 <= iCatFood < 15:
                    yum3(catfoodx, display_height - 100)
                elif 15 <= iCatFood < 20:
                    yum4(catfoodx, display_height - 100)
                elif iCatFood >= 20:
                    eatCatFood = False
                    catFoodEaten += 1
                    iCatFood = 0
                    catfoodx = random.randrange(0, display_width - 75)
                    catfoody = -42
            elif eatCatFood is False:
                catfood(catfoodx, catfoody)
        if iCatFood >= 20:
            eatCatFood = False
            iCatFood = 0
            catfoodx = random.randrange(0, display_width - 75)
            catfoody = -300
        elif eatCatFood is False:
            catfood(catfoodx, catfoody)
        score_board(catFoodEaten)
        stomach_ache(cocaEaten)
        pygame.display.update()
        clock.tick(60)


start_menu()
game_loop()
pygame.quit()
quit()
