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

class Head:
    def __init__(self):
        self.pos = (0,0)
        image_paths = ['PFDA Final Images/head01.png', 'PFDA Final Images/head02.png', 'PFDA Final Images/head03.png']
        self.images = [pygame.image.load(path).convert_alpha() for path in image_paths]
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect(topleft = (self.pos))
        
        #for image in range(len(self.images)):
            #self.images.append(pygame.image.load(self.image_files).convert_alpha)
            #images_rect = self.images.get_rect()
        #self.surface = self.update_surface()

    def surface(self):
        #adding a surface
        surf = pygame.Surface((720, 576))
        return surf
            

    def draw(self, surface):
        #draw images onto screen
        #toggle image visibility when selected
        #for image in self.images:
            #surf.draw(self.images, self.pos)
        surface.blit(self.image, self.rect)

    def set_image_by_index(self, index):
        if 0 <= index < len(self.images):
            self.current_image_index = index
            self.image = self.images[self.current_image_index]
            self. rect = self.image.get_rect(topleft = (self.pos))
    

while running:
    #instancing objects
    head = Head()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        
        #changing image with key press
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_index = (head.current_image_index + 1) % len(head.images)
                head.set_image_by_index(next_index)
            elif event.key == pygame.K_LEFT:
                prev_index = (head.current_image_index - 1 + len(head.images)) % len(head.images)
                head.set_image_by_index(prev_index)
            
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

    head.draw(screen)

    #if show_image:
        #screen.blit(skin01, skin01_rect)

    pygame.display.flip() 
    pygame.display.update()


pygame.quit() 