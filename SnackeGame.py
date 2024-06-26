#import necessary labraries

import pygame
import random
import time

#initialize pygame
pygame.init()

#set size of screen , colors , snake size and ...
height = 500
length = 500
screen = (height , length)
screen_color = pygame.Color(10 , 0 , 10)
snake = pygame.Color(0 , 200 , 80)
apple = pygame.Color(250 , 0 , 0)
snake_speed = 15
snake_size =[
    [250 , 250],
    [260 , 250],
    [270 , 250],
    [280 , 250],
    [290 , 250]
]

#position of snake when game start
snake_position = [250 , 250]

fps =pygame.time.Clock()

#define the score in game
score = 0
def show_score(choice , color , font , size):
    score_font = pygame.font.SysFont(font , size )
    score_surface = score_font.render('Score : ' + str(score) , True , color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

#define what is game over
def game_over():
    my_font = pygame.font.SysFont('Times new roman' , 30)
    game_over_surface = my_font.render(' game over .. your score is : '  + str(score) , True , pygame.Color(255 , 0 , 0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (250 , 250)
    game_window.blit(game_over_surface , game_over_rect)
    pygame.display.flip()
    #time.sleep(3)
    #pygame.quit()
    #quit()

#random palce of screen for apple
apple_position = [random.randrange(1, (height//10)) * 10 ,
                  random.randrange(1, (length//10)) * 10]
apple_spwan = True

#which way to move when the game starts
direction = 'DOWN'
change_to = direction

pygame.display.set_caption(' Mar Bazi ')
game_window = pygame.display.set_mode(screen)

fps = pygame.time.Clock()


#define your game
while True:
    #for every key "UP , DOWN , LEFT , RIGHT " direction will change
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_UP:
                change_to = 'UP'
    #we have limit moves if snake's direction is UP , it can't go DOWN
    if change_to == "UP" and direction != 'DOWN':
        direction = 'UP'
    if change_to == "DOWN" and direction != 'UP':
        direction = 'DOWN'
    if change_to == "LEFT" and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == "RIGHT" and direction != 'LEFT':
        direction = 'RIGHT'
    #define how many pixels move in an event
    if direction == 'UP' :
        snake_position[1] -= 10
    if direction == 'DOWN' :
        snake_position[1] += 10
    if direction == 'LEFT' :
        snake_position[0] -= 10
    if direction == 'RIGHT' :
        snake_position[0] += 10
    #start to move , ifsnack's  head touch the apple , increase the score
    snake_size.insert(0 ,list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
        score += 1
        apple_spwan = False
    #this line is because the tail of snake remains fixed and its head moves and its length increases
    else :
        snake_size.pop()
    #put the apple in a random place on the screen
    if not apple_spwan:
        apple_position = [random.randrange(1, (height//10)) * 10 ,
                  random.randrange(1, (length//10)) * 10]
    apple_spwan = True
    game_window.fill(screen_color)

    for position in snake_size:
        pygame.draw.rect(game_window , snake , pygame.Rect(position[0] , position[1] , 10 , 10))
    pygame.draw.rect(game_window,apple,pygame.Rect(apple_position[0] , apple_position[1] , 10 ,10))

    #if its head touches the border of screen you will lose
    if snake_position[0] < 0 or snake_position[0] >= height or snake_position[0] >= length:
        game_over()
    if snake_position[1] < 0 or snake_position[1] >= height or snake_position[1] >= length:
        game_over()
    #if its head touches its body you will lose
    for block in snake_size[1:] :
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
            time.sleep(2)
            pygame.quit()
            quit()
    #show the score top of the screen
    show_score(1 , pygame.Color(255,255,255), 'times new roman' , 20)
    pygame.display.update()
    fps.tick(snake_speed)
if game_over():
    time.sleep(3)
    pygame.quit()
    quit()