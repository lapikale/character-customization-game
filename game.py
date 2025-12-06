import pygame

#setup
pygame.init()
screen_width = 720
screen_height = 576
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Make Your Character!')
running = True

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    screen.fill('pink')

    pygame.display.flip() 


pygame.quit() 