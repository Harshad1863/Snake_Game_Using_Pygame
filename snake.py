import pygame
import random

pygame.init()

#colors
white =(255,255,255)
red = (255,0,0)
black =(0,0,0)

#creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((1000,500)) 

#Game title
pygame.display.set_caption("Snake With Harshad")


# Game specific Variable
exit_game = False
game_over = False
snake_x=45
snake_y=55
init_velocity=5
velocity_x=0
velocity_y=0
snake_size=20

food_x = random.randint(20,screen_width/2)
food_y = random.randint(20,screen_height/2)

score = 0

fps=50  #frame per sec

clock = pygame.time.Clock()
 
  
#Game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        
        if event.type == pygame.KEYDOWN:
            #for Right arrow key
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            #for Left arrow key
            if event.key == pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0
            
            #for UP arrow key
            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0

            #for Down arrow key
            if event.key == pygame.K_DOWN:
                velocity_y =  init_velocity
                velocity_x = 0

            

            

    snake_x += velocity_x
    snake_y += velocity_y

    #Replotting food and adding score
    if abs(snake_x - food_x)<4 and (snake_y - food_y)<4:
        score += 1
        print("Score: ",score*10)
        food_x = random.randint(20,screen_width/2)
        food_y = random.randint(20,screen_height/2)


    gameWindow.fill(white)
     #create food
    pygame.draw.rect(gameWindow,red, [food_x, food_y, snake_size , snake_size ])
    # Create Snake
    pygame.draw.rect(gameWindow,black, [snake_x, snake_y, snake_size , snake_size ])  
    
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()
    