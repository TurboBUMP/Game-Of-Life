import pygame
import pygame.locals
import sys

pygame.init()

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 900

FPS = 60

GREY = pygame.Color(128,128,128)
WHITE = pygame.Color(255,255,255)


DISPLAY = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
DISPLAY.fill(GREY)


FramePerSec = pygame.time.Clock()
FramePerSec.tick(FPS)


class button():
    def __init__(self,image,pos,base_color,hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.base_color, self.hovering_color = base_color, hovering_color
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))

    def update(self,screen):
        screen.blit(self.image,self.rect)

    def check_for_input(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.bottom, self.rect.top):
            print('button press')

button_surface = pygame.image.load('glider.png')
button_surface = pygame.transform.scale(button_surface,(164,164))

button = button(button_surface,(400,500),WHITE,GREY)





while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.check_for_input(pygame.mouse.get_pos())

        DISPLAY.fill(WHITE)
        button.update(DISPLAY)

        pygame.display.update()
