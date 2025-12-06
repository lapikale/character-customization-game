import pygame

#setup
pygame.init()
screen_width = 720
screen_height = 576
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Make Your Character!')
running = True

#add bg
bg_image = pygame.image.load('bg.png ')
bg_image_rect = bg_image.get_rect()
bg_image_rect.topleft(0,0)

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    #adding bg to screen
    display_surface.blit(bg_image, bg_image_rect)

    pygame.display.flip() 


pygame.quit() 