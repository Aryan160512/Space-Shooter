import pgzrun, random

WIDTH = 1000
HEIGHT = 600
TITLE = 'Space Shooter'

isGameOver = False

playerBulletSpeed = 6
enemyBulletSpeed = 6

alienSpeed = 7

shooter = Actor('shooter')
shooter.pos = (500, 550)

enemies = []
bullets = []

def createEnemy():
    rand = random.randint(1, 3)
    enemy = Actor(f'enemy{rand}')
    enemy.pos = (random.randint(50, 950), 50)
    enemies.append(enemy)

def playerBullets():
    bullet = Actor('bullet')
    bullet.pos = (shooter.x, shooter.y + 20)
    bullets.append(bullet)

def update():
    if random.random() < 0.01:
        createEnemy()

    if keyboard.left and shooter.x > 50:
        shooter.x -= 5
    elif keyboard.right and shooter.x < 950:
        shooter.x += 5

    if keyboard.space:
        playerBullets()

    for bullet in bullets:
        bullet.y -= playerBulletSpeed
        
        if bullet.y < 0:
            bullets.remove(bullet)

    for enemy in enemies:
        enemy.y += random.randint(1, 5)
        
        if enemy.y > 1000:
            isGameOver = True
            gameOver('YOU LOST')

def gameOver(message):
    screen.draw.text(message, (500, 300))

def draw():
    screen.clear()
    screen.blit('background', (0, 0))

    if isGameOver == False:
        for bullet in bullets:
            bullet.draw()

        shooter.draw()

        for enemy in enemies:
            enemy.draw()
pgzrun.go()