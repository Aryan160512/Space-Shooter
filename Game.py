import pgzrun, random

WIDTH = 1000
HEIGHT = 600
TITLE = 'Space Shooter'

isGameOver = False
score = 0

message = ''

playerBulletSpeed = 6
enemyBulletSpeed = 10

alienSpeed = 6

shooter = Actor('shooter')
shooter.pos = (500, 550)

enemies = []
bullets = []
enemyBullets = []

changeLevel = False
level = 1

def createEnemy():
    rand = random.randint(1, 3)
    enemy = Actor(f'enemy{rand}')
    enemy.pos = (random.randint(50, 950), 0)
    enemies.append(enemy)

def playerBullets():
    bullet = Actor('bullet')
    bullet.pos = (shooter.x, shooter.y + 20)
    bullets.append(bullet)

def checkCollison():
    global score
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 2

def on_key_down(key):
    if key == keys.SPACE:
        playerBullets()

def nextLevel():
    global enemies, bullets, level, changeLevel 
    level += 1
    enemies = []
    bullets = []

    changeLevel = True

def createEnemyBullets(alien):
    enemyBullet = Actor('enemybullet')
    enemyBullet.pos = (alien.x, alien.y + 20) 
    enemyBullets.append(enemyBullet)   


def update():
    global isGameOver, message, level, score
    if random.random() < 0.01:
        createEnemy()

    if keyboard.left and shooter.x > 50:
        shooter.x -= 5
    elif keyboard.right and shooter.x < 950:
        shooter.x += 5

    # if keyboard.space:
    #     playerBullets()

    for bullet in bullets:
        bullet.y -= playerBulletSpeed
        
        if bullet.y < 0:
            bullets.remove(bullet)

    for enemy in enemies:
        enemy.y += random.randint(1, 5)
        if enemy.colliderect(shooter):
            isGameOver = True
            message = 'YOU LOSE'
        
        if enemy.y > 650 and not isGameOver:
            # isGameOver = True
            # message = 'YOU LOSE'

            score -= 1

    if score == 10:
        if not changeLevel:
            nextLevel()

    if score == 20:
        isGameOver = True
        message = 'YOU WIN'

    if level == 2:
        if random.random() < 0.01:
            createEnemy()
        
        for enemy in enemies:
            if enemy.colliderect(shooter):
                isGameOver = True
                message = 'YOU LOST'
            
            if enemy.y > 650 and not isGameOver:
                #isGameOver = True
                #message = 'YOU LOST'
                score -= 1

            if random.random() < 0.01:
                createEnemyBullets(enemy)
                enemy.y += 1
            else:
                enemy.y += random.randint(1, 2)
        for enemyBullet in enemyBullets:
            enemyBullet.y += enemyBulletSpeed

            if enemyBullet.y > 1000:
                enemyBullets.remove(enemyBullet) 

def draw():
    screen.clear()
    screen.blit('background', (0, 0))

    checkCollison()

    screen.draw.text(f'Score: {score}', (50, 50))

    if isGameOver:
        screen.draw.text(message, (500, 300))

    if isGameOver == False:
        for bullet in bullets:
            bullet.draw()

        for enemyBullet in enemyBullets:
            enemyBullet.draw()

        shooter.draw()

        for enemy in enemies:
            enemy.draw()
pgzrun.go()