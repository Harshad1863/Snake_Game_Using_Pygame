import pygame
x = pygame.init()

#Windows
gameWindow = pygame.display.set_mode((1000,500)) 
#Set Title  
pygame.display.set_caption("Flippy Bird")        

# Game specific Variable
exit_game = False
game_over = False

#Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have passed Right arrow key")



pygame.quit()
quit()

