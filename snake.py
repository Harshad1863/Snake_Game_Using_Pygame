import pygame
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
pygame.display.set_caption("Snake WIth Harshad")


# Game specific Variable
exit_game = False
game_over = False
snake_x=45
snake_y=55
snake_size=10
fps=30  #frame per sec

clock = pygame.time.Clock()



#Game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        
        if event.type == pygame.KEYDOWN:
            #for Right arrow key
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10

            #for Left arrow key
            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 10
            
            #for UP arrow key
            if event.key == pygame.K_UP:
                snake_y = snake_y - 10

            #for Down arrow key
            if event.key == pygame.K_DOWN:
                snake_y = snake_y + 10

            

            




    gameWindow.fill(white) 
    pygame.draw.rect(gameWindow,black, [snake_x, snake_y, snake_size , snake_size ])  
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()
    