import pygame

import os

class Game:
    WIDTH, HEIGHT = 1280, 640
    
    FPS = 60
    hero_height = 24
    hero_width = 16
    WHITE = (255,255,255)
    vel = 32# velocity of hero model
    keys_pressed = pygame.key.get_pressed()
    def __init__(self):
       self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) 




model_front_image = pygame.image.load(os.path.join('game_assets', 'model_front.png'))
model_back_image = 
model_left_image = 
model_right_image =






def draw_window(main_model):
    WIN.fill((WHITE))
    WIN.blit(model_front_image, (main_model.x, main_model.y))
    pygame.display.update()
#def Hero_model():
    #main_model = pygame.Rect(100, 100, hero_width, hero_height)

    def Hero_movement(keys_pressed, main_model):
        if keys_pressed[pygame.K_w] and main_model.y - vel > 0:#up movement
            main_model.y -= vel
        if keys_pressed[pygame.K_s] and main_model.y + vel < HEIGHT:#down movement
            main_model.y += vel
        if keys_pressed[pygame.K_a] and main_model.x - vel > 0:# left movement
            main_model.x -= vel
        if keys_pressed[pygame.K_d] and main_model.x + vel < WIDTH:
            main_model.x += vel




#class main_Hero:
    #def __init__(self):
        
        #self.image = ''
        #self.model = main_model
        #self.movement = Hero_movement(keys_pressed, main_model)
    


    def module(self):#main module
    
        main_model = pygame.Rect(100, 100, hero_width, hero_height)
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                    draw_window(main_model)       
                    Hero_movement(keys_pressed, main_model)        
                
                
                
    pygame.quit()
    
    
