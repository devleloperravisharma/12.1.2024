import pgzrun
import random

WIDTH = 1700
HEIGHT = 1300
TITLE = "give love <3"
PINK = (249,83,127)
tears = []
hearts = []
score = 0
direction = 1

for x in range(10):
    for y in range(5):
        tear = Actor("teardrop")
        tears.append(tear)
        tears[-1].x = 400 + 100*x
        tears[-1].y = 150 + 50*y

player = Actor("star")
player.pos = (WIDTH//2, HEIGHT - 100)

def draw():
    screen.clear()
    screen.fill(PINK)
    player.draw()
    for tear in tears:
        tear.draw()
    for heart in hearts:
        heart.draw()
    if len(tears) == 0:
        happiness_mission_over()
    
    display_happiness()


def update():
    global score, direction, tears
    down = False
    if keyboard.a:
        if player.x <= 50:
            player.x = 50
        player.x -=5
    if keyboard.d:
        if player.x >= WIDTH-5:
            player.x = WIDTH-5
        player.x += 5
    if keyboard.w:
        if player.y >= HEIGHT-5:
            player.y = HEIGHT-5
        player.y -= 5
    if keyboard.s:
        if player.y <= 50:
            player.y = 50
        player.y +=5
    for heart in hearts:
        if heart.y < 0:
            hearts.remove(heart)
        else:
            heart.y -=50
    if len(tears) > 0 and (tears[0].x < 200 or tears[-1].x > WIDTH - 200):
        down = True
        direction = direction*-1
    for tear in tears:
        tear.x += 2*direction
        if down:
            tear.y += 150
        if tear.y > HEIGHT:
            tears.remove(tear)
        for heart in hearts:
            if tear.colliderect(heart):
                score += 1
                tears.remove(tear)
                hearts.remove(heart)
                if len(tears) == 0:
                    happiness_mission_over()
        if tear.colliderect(player):
            tears = []
            happiness_mission_over()

def on_mouse_down():
    global hearts
    heart = Actor("heart")
    hearts.append(heart)
    hearts[-1].x = player.x
    hearts[-1].y = player.y-50


def display_happiness():
    screen.draw.text("happiness given:" + str(score), (50, 50), fontsize = 50)

def happiness_mission_over():
    if score == 50:
        screen.draw.text("happiness spread to everyone! you spread happiness to:"+ str(score) + "teardrops!", (100, HEIGHT//2), fontsize = 50)
    else:
        screen.draw.text("you missed a teardrop and lost :( your score was:"+ str(score) + "teardrops!", (100, HEIGHT//2), fontsize = 50)
pgzrun.go()