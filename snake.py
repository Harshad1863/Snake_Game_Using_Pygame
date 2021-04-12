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

clock = pygame.time.Clock()

#Display Score On Screen
font = pygame.font.SysFont(None,55)


def text_screen(text,color,x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

#snake length increase
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

 
#Game loop
def gameloop():

    # Game specific Variable
    exit_game = False
    game_over = False
    snake_x=45
    snake_y=55
    init_velocity=5
    velocity_x=0
    velocity_y=0
    snake_size=20

    snk_list = []
    snk_length = 1

    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)

    score = 0

    fps=50  #frame per sec


    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over..!! Press Enter To Continue",red,100,200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()


        else:
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
                food_x = random.randint(20,screen_width/2)
                food_y = random.randint(20,screen_height/2)
                snk_length +=4


            gameWindow.fill(white)
            text_screen("Score: " + str(score * 10), red, 5, 5)
            #create food
            pygame.draw.rect(gameWindow,red, [food_x, food_y, snake_size , snake_size ])
            # Create Snake
            #pygame.draw.rect(gameWindow,black, [snake_x, snake_y, snake_size , snake_size ])  
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            #Collision Occure then Game over
            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

gameloop()
    