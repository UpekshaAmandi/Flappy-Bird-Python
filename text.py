import pygame
import neat
import time
import os
import random
import pygame

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("images","bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images","pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images","base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images","bg.png")))

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

# moment and animation
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

            #bird jump moment
    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

            #bird move
    def move(self):
        #lust jump how meny moment   
        self.tick_count == 1

        #how meny pixel up and down 
        d = self.vel*self.tick_count + 1.5*self.tick_count**2 #tick_out astimate to 1  [-10.5 + 1.5 = -9]
        #limt the pixel    
        if d>= 16: 
            d = 16
        if d < 0:
            d -= 2

        self.y = self.y = d
        
        #tracking bird rotation
        if d < 0 or self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90: #fell down 90 degree to down
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0] 
        elif self.img_count < self.ANIMATION_tIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_tIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_tIME*4:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_tIME*2 + 1:
            self.img = self.IMGS[0]
        self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center) 
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
    
def draw_window(win, bird):
    win.blit(BG_IMG, (0,0))
    bird.draw(win)
    pygame.display.update()

def main():
    WIN_HEIGHT = 800  # Define WIN_HEIGHT variable
    bird = Bird(200, 200)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    run = True
    while run:
        for event in pygame.event.get(): #tracking mouse moment something
            if event.type == pygame.QUIT:
                run = False
        
        draw_window(win, bird)
                
    pygame.quit()
    quit()

main()