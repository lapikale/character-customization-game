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
#skin01 = pygame.image.load('PFDA Final Images/skin01.png').convert_alpha() 
#skin01_rect = skin01.get_rect()
#skin01_rect.topleft = (0,0)

#show_image = True

class Skin:
    def __init__(self):
        #load images in a list
        self.images = []
        self.image_files = ['PFDA Final Images/skin01.png', 'PFDA Final Images/skin02.png', 'PFDA Final Images/skin03.png']
        for image in range(len(self.images)):
            self.images.append(pygame.image.load(self.image_files).convert_alpha)
            images_rect = self.images.get_rect()
            images_rect.topleft = (0,0)
        self.surface = self.update_surface()

    def update_surface(self):
        #adding a surface
        surf = pygame.Surface((720, 576))
        return surf
            

    def draw(self, screen):
        #draw images onto screen
        #toggle image visibility when selected
        for image in self.images:
            screen.blit(self.images, (0,0))


while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            
    #image visibility toggle
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_SPACE:
                #show_image = not show_image

    #replace image with new image?
        #if event.type == pygame.KEYDOWN and event.skin01 == 1:
            #skin_1 = new_skin_1


    #adding bg to screen
    screen.blit(bg_image, bg_image_rect)
    #screen.blit(skin01, skin01_rect)

    #instancing object
    skin = Skin()

    #if show_image:
        #screen.blit(skin01, skin01_rect)

    pygame.display.flip() 
    pygame.display.update()


pygame.quit() 