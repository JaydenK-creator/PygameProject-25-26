from gamelib import *
from random import randint
import time

game = Game(960, 640, "Dash World")
bk = Image("Images/gdbackg.png", game) 
game.setBackground(bk)

icon = Image("./images/cube_1.png", game)
icon.resizeBy(-60)
icon.moveTo(150, 450)
icon.dy = 0          
icon.gravity = 1.5   
icon.jump_power = -22
icon.grounded = True

game_speed = 5
current_level = 1
level_up_score = 20 

bar_bg = Shape("bar", game, 400, 20, gray)
bar_progress = Shape("bar", game, 0, 20, cyan)

obstacles = []
for i in range(6):
    a = Image("images/spike.png", game)
    a.resizeBy(-85)
    a.moveTo(1000 + (i * 500), 450)
    obstacles.append(a)

# START SCREEN
info = Image("images/info.png", game)
info.x = 450
info.y = 500
info.resizeBy(-40)

instructions = Image("images/instructions.png",game)
instructions.visible = False

play = Image("images/play.png", game)
play.resizeBy(-50)
play.x = 450
play.y = 375

title = Image("images/title.png", game)
title.y = 200
title.x = 450
title.resizeBy(-30)

cursor = Image("images/cursor.png", game)

mouse.visible = False

while not game.over:
    game.processInput()
    game.scrollBackground("left", 2) 
   
    info.draw()
    title.draw()
    play.draw()
    instructions.draw()

    cursor.moveTo(mouse.x, mouse.y)
    cursor.draw()

    if cursor.collidedWith(info, "rectangle") and mouse.LeftClick:
        instructions.visible = True

    if keys.Pressed[K_SPACE]:
        instructions.visible = False

    if cursor.collidedWith(play, "rectangle") and mouse.LeftClick:
        game.over = True

    game.update(60)

# RESET FOR LEVEL 1
game.over = False
game.score = 0

# LEVEL 1
while not game.over:
    game.processInput()
    game.scrollBackground("left", game_speed)

    if game.score >= level_up_score:
        game.drawText("LEVEL 1", 300, 300)
        game.update(30)
        time.sleep(2)
        game.over = True
#icon rotation/physics
    icon.dy += icon.gravity
    icon.y += icon.dy

    if icon.y >= 450:
        icon.y = 450
        icon.dy = 0
        if not icon.grounded: 
            icon.grounded = True
            icon.rotate = "still"
            
    else:
        icon.grounded = False
        icon.rotate = "right" 
        icon.rotate_angle -= 0.15 

    if keys.Pressed[K_SPACE] and icon.grounded:
        icon.dy = icon.jump_power
        icon.grounded = False

    icon.draw()

    for obs in obstacles:
        obs.x -= (game_speed + 3)
        obs.draw()

        if icon.collidedWith(obs):
            game.drawText("YOU LOSE", 350, 250)
            game.update(1)
            time.sleep(2)
            game.over = True
            game.quit()

        if obs.isOffScreen("left"):
            furthest_x = max(o.x for o in obstacles)
            gap = randint(300, 450)
            obs.x = furthest_x + gap
            game.score += 1


    
    bar_bg.moveTo(280, 50)
    bar_progress.moveTo(280, 50)
    progress_val = min(game.score / level_up_score, 1.0) 
    bar_progress.width = 400 * progress_val
    bar_bg.draw()
    bar_progress.draw()

    game.displayScore()
    game.update(60)

# LEVEL 2 START SCREEN
game.over = False
while not game.over:
    game.processInput()
    game.drawText("Press [F] to start Level 2", 300, 320)
    game.update(60)

    if keys.Pressed[K_f]:
        game.over = True

# LEVEL 2
game.over = False
game.score = 0  
game_speed = 7

for i in range(len(obstacles)):
    obstacles[i].moveTo(1000 + (i * 500), 450)

while not game.over:
    game.processInput()
    game.scrollBackground("left", game_speed)

    icon.dy += icon.gravity
    icon.y += icon.dy

    if icon.y >= 450:
        icon.y = 450
        icon.dy = 0
        if not icon.grounded: 
            icon.grounded = True
            icon.rotate = "still"
            icon.rotate_angle = round(icon.rotate_angle / (math.pi/2)) * (math.pi/2)
    else:
        icon.grounded = False
        icon.rotate = "right" 
        icon.rotate_angle -= 0.30 

    if keys.Pressed[K_SPACE] and icon.grounded:
        icon.dy = icon.jump_power
        icon.grounded = False

    icon.draw()

    for obs in obstacles:
        obs.x -= (game_speed + 5)
        obs.draw()

        if icon.collidedWith(obs):
            game.drawText("YOU LOSE", 350, 250)
            game.update(1)
            time.sleep(2)
            game.over = True
            game.quit()

        if obs.isOffScreen("left"):
            furthest_x = max(o.x for o in obstacles)
            gap = randint(300, 450)
            obs.x = furthest_x + gap
            game.score += 1

    bar_bg.moveTo(280, 50)
    bar_progress.moveTo(280, 50)
    progress_val = min(game.score / 20, 1.0) 
    bar_progress.width = 400 * progress_val
    bar_bg.draw()
    bar_progress.draw()

    if game.score >= 20:
        game.drawText("Level 2 completed", 300, 300)
        game.update(1)
        time.sleep(2)
        game.over = True

    game.displayScore()
    game.update(60)

# LEVEL 3 START SCREEN
game.over = False
while not game.over:
    game.processInput()
    game.drawText("Press [F] to start Level 3(Endless)", 300, 320)
    game.update(60)

    if keys.Pressed[K_f]:
        game.over = True

game.update(1)






game.over = False
game.score = 0  
for i in range(len(obstacles)):
    obstacles[i].moveTo(1000 + (i * 500), 450)
#final challenge
while not game.over:
    game.processInput()
    game.scrollBackground("left", game_speed)

   
    icon.dy += icon.gravity
    icon.y += icon.dy

    if icon.y >= 450:
        icon.y = 450
        icon.dy = 0
        if not icon.grounded: 
            icon.grounded = True
            icon.rotate = "still"
    else:
        icon.grounded = False
        icon.rotate = "right" 
        icon.rotate_angle -= 0.15 

    if keys.Pressed[K_SPACE] and icon.grounded:
        icon.dy = icon.jump_power
        icon.grounded = False

    icon.draw()

    for obs in obstacles:
        obs.x -= (game_speed + 3)
        obs.draw()

        if icon.collidedWith(obs):
            game.over = True

        if obs.isOffScreen("left"):
            furthest_x = max(o.x for o in obstacles)
            gap = randint(300, 450)
            obs.x = furthest_x + gap
            game.score += 1
            
            if game.score % 5 == 0:
                game_speed += 0.3

 

    game.displayScore()
    game.update(60)

game.drawText("GAME OVER", 350, 300)
game.update(30) 
game.quit()
