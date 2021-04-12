import pygame
x = pygame.init()

#Windows
gameWindow = pygame.display.set_mode((1200,500)) 
#Set Title  
pygame.display.set_caption("Flippy Bird")        

# Game specific Variable
exit_game = False
game_over = False

#Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)



pygame.quit()
quit()

