import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = 'Maze Runner'

walls = [
    Rect(0, 0, 800, 10),
    Rect(0, 0, 10, 600),
    Rect(0, 590, 800, 10),
    Rect(790, 0, 10, 600),
    Rect(100, 100, 200, 10),
    Rect(300, 100, 10, 200),
    Rect(300, 300, 200, 10),
    Rect(500, 200, 10, 200),
    Rect(200, 400, 300, 10),
    Rect(100, 500, 10, 100),
    Rect(400, 500, 100, 10),
    Rect(600, 100, 10, 200),
    Rect(600, 300, 100, 10),
    Rect(700, 200, 10, 300),
    Rect(200, 200, 10, 200),
    Rect(100, 300, 100, 10),
    Rect(200, 500, 200, 10),
    Rect(150, 150, 100, 10),
    Rect(250, 150, 10, 100),
    Rect(150, 250, 100, 10),
    Rect(500, 150, 200, 10),
    Rect(550, 250, 10, 100),
    Rect(450, 350, 150, 10),
    Rect(350, 250, 10, 100),
    Rect(250, 350, 100, 10),
    Rect(350, 450, 200, 10),
    Rect(100, 200, 10, 100),
    Rect(700, 400, 10, 100),
    Rect(650, 450, 50, 10),
    Rect(400, 150, 10, 100),
    Rect(300, 450, 10, 100),
]

def draw():
    screen.clear()
    for wall in walls:
        screen.draw.filled_rect(wall, 'grey')

pgzrun.go()
