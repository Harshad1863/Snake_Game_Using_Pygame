import pygame
pygame.init()

#colors
white =(255,255,255)
red = (255,0,0)
black =()

screen_width = 900
screen_height = 600

#creating window
gameWindow = pygame.display.set_mode((1000,500)) 
pygame.display.set_caption("Snake WIth Harshad")


# Game specific Variable
exit_game = False
game_over = False

#Game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            exit_game=True



    gameWindow.fill(white)   
    pygame.display.update()


pygame.quit()
quit()
    