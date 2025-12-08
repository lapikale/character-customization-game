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

#load button images
right_arrow = pygame.image.load('PFDA Final Images/arrow_right.png').convert_alpha()
left_arrow = pygame.image.load('PFDA Final Images/arrow_left.png').convert_alpha()

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        #mouse logic
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

#button instances
#skin
right_button_skin = Button(580, 50, right_arrow)
left_button_skin = Button(100, 50, left_arrow)
#head
right_button_head = Button(580, 100, right_arrow)
left_button_head = Button(100, 100, left_arrow)


class Head:
    def __init__(self):
        self.pos = (0,0)
        image_paths = ['PFDA Final Images/head01.png', 'PFDA Final Images/head02.png', 'PFDA Final Images/head03.png']
        self.images = [pygame.image.load(path).convert_alpha() for path in image_paths]
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect(topleft = (self.pos))

    def surface(self):
        #adding a surface
        surf = pygame.Surface((720, 576))
        return surf
            

    def draw(self, surface):
        #draw images onto screen
        surface.blit(self.image, self.rect)

    def set_image_by_index(self, index):
        if 0 <= index < len(self.images):
            self.current_image_index = index
            self.image = self.images[self.current_image_index]
            self.rect = self.image.get_rect(topleft = (self.pos))

class Top:
    def __init__(self):
        self.pos = (0,0)
        image_paths = ['PFDA Final Images/top01.png', 'PFDA Final Images/top02.png', 'PFDA Final Images/top03.png']
        self.images = [pygame.image.load(path).convert_alpha() for path in image_paths]
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect(topleft = (self.pos))

    def surface(self):
        #adding a surface
        surf = pygame.Surface((720, 576))
        return surf
        
    def draw(self, surface):
        #draw images onto screen
        surface.blit(self.image, self.rect)

    def set_image_by_index(self, index):
        if 0 <= index < len(self.images):
            self.current_image_index = index
            self.image = self.images[self.current_image_index]
            self.rect = self.image.get_rect(topleft = (self.pos))

class Legs:
    def __init__(self):
        self.pos = (0,0)
        image_paths = ['PFDA Final Images/legs01.png', 'PFDA Final Images/legs02.png', 'PFDA Final Images/legs03.png']
        self.images = [pygame.image.load(path).convert_alpha() for path in image_paths]
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect(topleft = (self.pos))

    def surface(self):
        #adding a surface
        surf = pygame.Surface((720, 576))
        return surf
        
    def draw(self, surface):
        #draw images onto screen
        surface.blit(self.image, self.rect)

    def set_image_by_index(self, index):
        if 0 <= index < len(self.images):
            self.current_image_index = index
            self.image = self.images[self.current_image_index]
            self.rect = self.image.get_rect(topleft = (self.pos))

class Skin:
    def __init__(self):
        self.pos = (0,0)
        image_paths = ['PFDA Final Images/skin01.png', 'PFDA Final Images/skin02.png', 'PFDA Final Images/skin03.png']
        self.images = [pygame.image.load(path).convert_alpha() for path in image_paths]
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect(topleft = (self.pos))

    def surface(self):
        #adding a surface
        surf = pygame.Surface((720, 576))
        return surf
        
    def draw(self, surface):
        #draw images onto screen
        surface.blit(self.image, self.rect)

    def set_image_by_index(self, index):
        if 0 <= index < len(self.images):
            self.current_image_index = index
            self.image = self.images[self.current_image_index]
            self.rect = self.image.get_rect(topleft = (self.pos))
    
    
#instancing objects
skin = Skin()
head = Head()
top = Top()
legs = Legs()


while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        
        #changing image with key press
        #head
        if right_button_head.draw():
            next_index = (head.current_image_index + 1) % len(head.images)
            head.set_image_by_index(next_index)
        if left_button_head.draw():
            prev_index = (head.current_image_index - 1 + len(head.images)) % len(head.images)
            head.set_image_by_index(prev_index)
        #top
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_index = (top.current_image_index + 1) % len(top.images)
                top.set_image_by_index(next_index)
            elif event.key == pygame.K_LEFT:
                prev_index = (top.current_image_index - 1 + len(top.images)) % len(top.images)
                top.set_image_by_index(prev_index)
        #skin
        if right_button_skin.draw():
            next_index = (skin.current_image_index + 1) % len(skin.images)
            skin.set_image_by_index(next_index)
        if left_button_skin.draw():
                prev_index = (skin.current_image_index - 1 + len(skin.images)) % len(skin.images)
                skin.set_image_by_index(prev_index)
        #legs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_index = (legs.current_image_index + 1) % len(legs.images)
                legs.set_image_by_index(next_index)
            elif event.key == pygame.K_LEFT:
                prev_index = (legs.current_image_index - 1 + len(legs.images)) % len(legs.images)
                legs.set_image_by_index(prev_index)


    #adding bg to screen
    screen.blit(bg_image, bg_image_rect)

    #drawing body parts to screen
    skin.draw(screen)
    head.draw(screen)
    legs.draw(screen)
    top.draw(screen)

    #drawing buttons to screen
    right_button_skin.draw()
    left_button_skin.draw()
    right_button_head.draw()
    left_button_head.draw()

    pygame.display.flip() 
    pygame.display.update()


pygame.quit() 