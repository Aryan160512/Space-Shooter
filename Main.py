import os

x = 100
y = 100

os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x}, {y}'

import pygame
from pygame.locals import *

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
isRunning = True

border = pygame.Rect(WIDTH // 2 - 5, 0, 20, HEIGHT)
speed = 5
bulletSpeed = 10
maxBullets = 5

keysS1 = [False, False, False, False]
keysS2 = [False, False, False, False]

shipWidth = 100
shipHeight = 100

bg = pygame.image.load('Images/background.jpg')
spaceship1 = pygame.image.load('Images/spaceship.png')
spaceship2 = pygame.image.load('Images/spaceship2.png')

spaceship1 = pygame.transform.scale(spaceship1, (shipWidth, shipHeight))
spaceship2 = pygame.transform.scale(spaceship2, (shipWidth, shipHeight))

def movementRed(keysPressed, redShip):
    if keysPressed[pygame.K_a] and redShip.x - speed > 0:
        redShip.x -= speed
    elif keysPressed[pygame.K_d] and redShip.x + speed < (WIDTH // 2 - 100):
        redShip.x += speed
    elif keysPressed[pygame.K_w] and redShip.y + speed > 0:
        redShip.y -= speed
    elif keysPressed[pygame.K_s] and redShip.y - speed < HEIGHT - 100:
        redShip.y += speed


def movementBlue(keysPressed, blueShip):
    if keysPressed[pygame.K_LEFT] and blueShip.x - speed > WIDTH // 2 + 10:
        blueShip.x -= speed
    elif keysPressed[pygame.K_RIGHT] and blueShip.x + speed < (WIDTH - 100):
        blueShip.x += speed
    elif keysPressed[pygame.K_UP] and blueShip.y + speed > 0:
        blueShip.y -= speed
    elif keysPressed[pygame.K_DOWN] and blueShip.y - speed < HEIGHT - 100:
        blueShip.y += speed

def moveBullets(redBullets, blueBullets, redShip, blueShip):
    for rbullet in redBullets:
        rbullet.x += bulletSpeed

        if rbullet.colliderect(blueShip):
            redBullets.remove(rbullet)
        elif rbullet.x > WIDTH:
            redBullets.remove(rbullet)
    
    for bbullet in blueBullets:
        bbullet.x -= bulletSpeed

        if bbullet.colliderect(redShip):
            blueBullets.remove(bbullet)

        elif bbullet.x < 0:
            blueBullets.remove(bbullet)



def display(redShip, blueShip, redHealth, blueHealth, redBullets, blueBullets):
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, 'black', border)
    screen.blit(spaceship1, (redShip.x, redShip.y))
    screen.blit(spaceship2, (blueShip.x, blueShip.y))

    font = pygame.font.SysFont('Verdana', 30)
    redHealthText = font.render(f'Health: {redHealth}', True, ("#FF0000"))
    screen.blit(redHealthText, (50, 50))

    blueHealthText = font.render(f'Health: {blueHealth}', True, ("#00F0FF"))
    screen.blit(blueHealthText, (800, 50))
    pygame.display.update()

    for rBullet in redBullets:
        pygame.draw.rect(screen, 'red', rBullet)
    
    for bBullet in blueBullets:
        pygame.draw.rect(screen, 'blue', bBullet)

    pygame.display.update()


def main():

    redShip = pygame.Rect(30, 300, shipWidth, shipHeight)
    blueShip = pygame.Rect(850, 300, shipWidth, shipHeight)
    redHealth = 10
    blueHealth = 10
    redBullets = []
    blueBullets = []
    
    global isRunning
    while isRunning:
    
        keyPressed = pygame.key.get_pressed()
        movementRed(keyPressed, redShip)
        movementBlue(keyPressed, blueShip)
        moveBullets(redBullets, blueBullets, redShip, blueShip)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(redBullets) < maxBullets:
                    bullet = pygame.Rect(redShip.x + redShip.width, redShip.y + redShip.height // 2, 10, 5)
                    redBullets.append(bullet)
                
                if event.key == pygame.K_RCTRL and len(blueBullets) < maxBullets:
                    bullet = pygame.Rect(blueShip.x, blueShip.y + blueShip.height // 2, 10, 5)
                    redBullets.append(bullet)

        display(redShip, blueShip, redHealth, blueHealth, redBullets, blueBullets)

main()
pygame.quit()