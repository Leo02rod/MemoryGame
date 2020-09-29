import pygame
import random

pygame.init()

#screen/title setup
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("SDD Game")

#font for characters
largeText = pygame.font.Font("ChalkboardSE.ttc",60)
mediumText = pygame.font.Font("ChalkboardSE.ttc",40)
smallText = pygame.font.Font("ChalkboardSE.ttc",20)

#Colours
white = (255, 255,255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0,200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
dark_gray = (50, 50, 50)
sky_blue = (0,255,255)
light_gray = (200,200,200)
moon_glow = (235,245,255)

#In game Variables
clock = pygame.time.Clock()
fps = 60
x_center = 800/2
y_center = 600/2
center = x_center, y_center
button_width = 120
button_height = 50
character_set = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm-=#%%$#^"
word = ""
guessed = []


#score system
score1 = 0

# answer
answer = ""

text = ''

#Input box/Window
def game():

    game = True
    global text
    input_box_selected = False
    text = ""

    while game:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 600 > mouse_position[0] > 200 and 325 > mouse_position[1] > 275:
                    input_box_selected = True
                else:
                    input_box_selected = False
            if event.type == pygame.KEYDOWN:
                if input_box_selected:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key == pygame.K_RETURN:
                        confirm()
                    else:
                        text += event.unicode

        screen.fill(green)

        mediumText = pygame.font.Font("ChalkboardSE.ttc",40)
        smallText = pygame.font.Font("ChalkboardSE.ttc",20)
        TextSurf, TextRect = text_objects("ANSWER!", mediumText)
        TextRect.center = (400, 100)
        screen.blit(TextSurf, TextRect)
#input boxes
        if input_box_selected:
            pygame.draw.rect(screen, black, (200,275, 400, 50))
            pygame.draw.rect(screen, white, (200,275, 400, 50))

            TextSurf, TextRect = text_objects(text, smallText)
            TextRect.center = (400, 300)
            screen.blit(TextSurf, TextRect)
        else:
            pygame.draw.rect(screen, black, (200,275, 400, 50))
            pygame.draw.rect(screen, white, (200,275, 400, 50))

        #input box text
            TextSurf, TextRect = text_objects(text, smallText)
            TextRect.center = (400, 300)
            screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(60)

#checking function
def confirm():

    confirm = True

    while confirm:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(moon_glow)

        largeText = pygame.font.SysFont('ChalkboardSE.ttc', 100)

        if answer == text:
            TextSurf, TextRect = text_objects("CORRECT", largeText)
            TextRect.center = (400, 100)
            screen.blit(TextSurf, TextRect)
            # Exit to menu screen or quit button
            button("MENU", 100, 450, 100, 50, red, bright_red, level)
            button("Continue", 300, 450, 100, 50, green, bright_green, easy)
            button("QUIT", 600, 450, 100, 50, red, bright_red, quitgame)
        else:
            TextSurf, TextRect = text_objects("WRONG", largeText)
            TextRect.center = (400, 100)
            screen.blit(TextSurf, TextRect)
            # Exit to menu screen or quit button
            button("MENU", 100, 450, 100, 50, red, bright_red, menu)
            button("QUIT", 600, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(60)

#random character generator
def random_word():

    global answer
    global character_set

    answer = ""

    for i in range(6):
        answer += random.choice(character_set)



#In game Timer
#timer
def timer(time):
    pygame.time.wait(time * 1000)


# Text renderer
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Button renderer
def button(button_text, button_x, button_y, button_width, button_height, inactive_colour, active_colour, action=None):

    # Mouse position
    mouse_position = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    # Button
    if button_x + button_width > mouse_position[0] > button_x and button_y + button_height > mouse_position[1] > button_y:
        pygame.draw.rect(screen, active_colour, (button_x, button_y, button_width, button_height))

        # Mouse click
        if mouse_click[0] == 1 and action is not None:
            action()

    else:
        pygame.draw.rect(screen, inactive_colour, (button_x, button_y, button_width, button_height))

    # Button text
    smallText = pygame.font.SysFont("ChalkboardSE.ttc", 20)
    TextSurf, TextRect = text_objects(button_text, smallText)
    TextRect.center = (button_x + (button_width / 2), button_y + (button_height / 2))
    screen.blit(TextSurf, TextRect)

def score(score):
    text = smallfont.render("Score: "+string(score), True, black)
    screen.blit(text, [0,0])

#______________________________Main game________________________________

#Splashscreen
def splashscreen():

    splashscreen = True

    while splashscreen:
        # If exit button pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Background
        screen.fill(sky_blue)

        # Text
        TextSurf, TextRect = text_objects("2020 Memory Game", largeText)
        TextRect.center = (center)
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(60)

        # Timer
        timer(2)

        # Show menu
        menu()

#Main Menu
def menu():

    menu = True

    while menu:
        #To exit by pressing exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(sky_blue)

        #In text Menu
        TextSurf, TextRect = text_objects("Mind_(@)-(@)_Game", largeText)
        TextRect.center = (center)
        screen.blit(TextSurf, TextRect)

        #Three main buttons for (start, instructions, quit)
        #Start buttons
        button("Begin", x_center - 250, y_center + 100, button_width, button_height, green, bright_green, level)
        button("Instructions", x_center - button_width/2, y_center + 100, button_width, button_height, light_gray, moon_glow, instruction)
        button("Quit", x_center + 150, y_center + 100, button_width, button_height, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(fps)

# Instruction
def instruction():

    instruction = True

    while instruction:
        for event in pygame.event.get():
            # If quit button pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(sky_blue)
        largeText = pygame.font.SysFont('ChalkboardSE.ttc', 110)
        TextSurf, TextRect = text_objects("Instructions", largeText)
        TextRect.center = ((800/2), (600/2 - 150))
        screen.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont('ChalkboardSE.ttc', 30)
        TextSurf, TextRect = text_objects("The goal of this game is to write down", smallText)
        TextRect.center = ((800/2), (600/2 - 80))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("the 6 random characters that appear on the screen.", smallText)
        TextRect.center = ((800/2), (600/2 - 50))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("There is a time limit for each level difficulty.", smallText)
        TextRect.center = ((800/2), (600/2 - 20))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("EASY = 15 secs", smallText)
        TextRect.center = ((800/2), (600/2 + 40))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("NORMAL = 8 secs", smallText)
        TextRect.center = ((800/2), (600/2 + 80))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("HARD = 3 secs", smallText)
        TextRect.center = ((800/2), (600/2 + 120))
        screen.blit(TextSurf, TextRect)

        # Back Button
        button("Back", 50, 450, 100, 50, red, bright_red, menu)

        pygame.display.update()
        clock.tick(60)

#Begin button
def level():

    level = True

    while level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Background
        screen.fill(dark_gray)
        largeText = pygame.font.SysFont('ChalkboardSE.ttc', 100)
        TextSurf, TextRect = text_objects("Select difficulty", largeText)
        TextRect.center = (400, 100)
        screen.blit(TextSurf, TextRect)
        button("Back", 50, 450, 100, 50 ,red, bright_red, menu)

        # Easy button
        button("Easy", 150, 250, 100, 50, green, bright_green, easy)

        button("Medium", 350, 250, 100, 50, green, bright_green, medium)

        button("Hard", 550, 250, 100, 50, green, bright_green, tough)


        pygame.display.update()
        clock.tick(60)

#Easy difficulty
def easy():

    random_word()

    countdown = 15

    easy = True

    while easy:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Background
        screen.fill(dark_gray)

        largeText = pygame.font.SysFont('ChalkboardSE.ttc', 80)

        # Display word
        TextSurf, TextRect = text_objects(f"Word is {answer}", largeText)
        TextRect.center = (center)
        screen.blit(TextSurf, TextRect)

        # Display countdown
        TextSurf, TextRect = text_objects(f"Starting in {countdown}...", mediumText)
        TextRect.center = (x_center, y_center + 50)
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(1)
        countdown -= 1

        if countdown == 0:
            game()

#Normal Level
def medium():

    global answer

    random_word()

    countdown = 8

    medium = True

    while medium:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Background
        screen.fill(dark_gray)

        # Display word
        largeText = pygame.font.SysFont('ChalkboardSE.ttc', 80)
        TextSurf, TextRect = text_objects(f"Word is {answer}", largeText)
        TextRect.center = (center)
        screen.blit(TextSurf, TextRect)

        # Display countdown
        TextSurf, TextRect = text_objects(f"Starting in {countdown}...", mediumText)
        TextRect.center = (x_center, y_center + 50)
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(1)
        countdown -= 1

        if countdown == 0:
            game()

# hard difficulty
def tough():

    global answer
    global text

    random_word()

    countdown = 3

    tough = True

    while tough:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Background
        screen.fill(dark_gray)

        # Display word
        largeText = pygame.font.SysFont('ChalkboardSE.ttc', 80)
        TextSurf, TextRect = text_objects(f"Word is {answer}", largeText)
        TextRect.center = (400, 100)
        screen.blit(TextSurf, TextRect)

        # Display countdown
        TextSurf, TextRect = text_objects(f"Starting in {countdown}...", mediumText)
        TextRect.center = (x_center, y_center + 50)
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(1)
        countdown -= 1

        if countdown == 0:
            game()

# answer game
def game():

    game = True
    global text
    input_box_selected = False
    text = ""

    while game:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 600 > mouse_position[0] > 200 and 325 > mouse_position[1] > 275:
                    input_box_selected = True
                else:
                    input_box_selected = False
            if event.type == pygame.KEYDOWN:
                if input_box_selected:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key == pygame.K_RETURN:
                        confirm()
                    else:
                        text += event.unicode

        screen.fill(light_gray)

        #text
        mediumText = pygame.font.Font("ChalkboardSE.ttc",40)
        smallText = pygame.font.Font("ChalkboardSE.ttc",20)
        TextSurf, TextRect = text_objects("Input ANSWER!", mediumText)
        TextRect.center = (400, 100)
        screen.blit(TextSurf, TextRect)
        #input boxes
        if input_box_selected:
            pygame.draw.rect(screen, black, (200,275, 400, 50))
            pygame.draw.rect(screen, white, (205,285, 390, 40))

            TextSurf, TextRect = text_objects(text, smallText)
            TextRect.center = (400, 300)
            screen.blit(TextSurf, TextRect)
        else:
            pygame.draw.rect(screen, black, (200,275, 400, 50))
            pygame.draw.rect(screen, red, (205,280, 390, 40))

        #input box text
            TextSurf, TextRect = text_objects(text, smallText)
            TextRect.center = (400, 300)
            screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(60)

#checking function
def confirm():

    confirm = True

    while confirm:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(green)

        #display scores

        largeText = pygame.font.SysFont('ChalkboardSE.ttc', 100)

        if answer == text:
            TextSurf, TextRect = text_objects("CORRECT", largeText)
            TextRect.center = (400, 100)
            screen.blit(TextSurf, TextRect)
            # Exit to menu screen or quit button
            button("MENU", 100, 450, 100, 50, red, bright_red, level)
            button("continue", 300, 450, 100, 50, red, bright_red, tough)
            button("QUIT", 600, 450, 100, 50, red, bright_red, quitgame)
        else:
            TextSurf, TextRect = text_objects("WRONG", largeText)
            TextRect.center = (400, 100)
            screen.blit(TextSurf, TextRect)
            # Exit to menu screen or quit button
            button("MENU", 100, 450, 100, 50, red, bright_red, menu)
            button("QUIT", 600, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(60)


#quitgame
def quitgame():
    pygame.quit()

splashscreen()

menu()

pygame.quit()
