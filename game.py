import pygame

#setup
pygame.init()
screen_width = 720
screen_height = 576
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Make Your Character!')
running = True

#add bg
bg_image = pygame.image.load('PFDA Final Images/bg.png')
bg_image_rect = bg_image.get_rect()
bg_image_rect.topleft = (0,0)

#testing adding images
skin01 = pygame.image.load('PFDA Final Images/skin01.png').convert_alpha() 
skin01_rect = skin01.get_rect()
skin01_rect.topleft = (0,0)

show_image = True

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_image = not show_image

    #adding bg to screen
    screen.blit(bg_image, bg_image_rect)
    #screen.blit(skin01, skin01_rect)

    if show_image:
        screen.blit(skin01, skin01_rect)

    pygame.display.flip() 


pygame.quit() 