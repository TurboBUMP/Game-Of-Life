try:
    import pygame
    import pygame.locals
except ModuleNotFoundError as err:
    print('Error: ', err)

import sys

pygame.init()

BOARD_WIDTH = 900
BOARD_HEIGHT = 900

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

NUMBER_OF_CELLS_X = 50
NUMBER_OF_CELLS_Y = 50

X_CELL_DIMENSION = int(BOARD_WIDTH/NUMBER_OF_CELLS_X)
Y_CELL_DIMENSION = int(BOARD_HEIGHT/NUMBER_OF_CELLS_Y)

FPS = 60
TITLE = 'Game Of Life'

BLACK = pygame.Color(0, 0, 0)         # Black
WHITE = pygame.Color(255, 255, 255)   # White
GREY = pygame.Color(128, 128, 128)   # Grey
RED = pygame.Color(255, 0, 0)       # Red

DISPLAY = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
DISPLAY.fill(WHITE)
pygame.display.set_caption(TITLE)

FramePerSec = pygame.time.Clock()
FramePerSec.tick(FPS)

###############################################################################

def draw_grid(display,display_width,x_cell_dimension,y_cell_dimension,display_height,color):

    for x in range(0,display_width+1,x_cell_dimension):
        pygame.draw.line(display,color,(x,0),(x,display_height))

    for y in range(0,display_height+1,y_cell_dimension):
        pygame.draw.line(display,color,(0,y),(display_width,y))

###############################################################################

###############################################################################
################################## class ######################################
class button_glider():
    def __init__(self,image,pos):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.pressed = False

    def update(self,screen):
        screen.blit(self.image,self.rect)

    def check_for_input(self,position):
        if (position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)):
            self.pressed = True

    def draw_glider(self,position,pressed):
        if self.pressed==True:
            if event.type == pygame.MOUSEBUTTONUP:
                if (position[0]<BOARD_WIDTH and position[1]<BOARD_HEIGHT):
                    placing_position = pygame.mouse.get_pos()
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+2,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+2,placing_position[1]//Y_CELL_DIMENSION-1)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION-2)).draw(DISPLAY))
                    self.pressed=False

class button_rumble():
    def __init__(self,image,pos):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.pressed = False

    def update(self,screen):
        screen.blit(self.image,self.rect)

    def check_for_input(self,position):
        if (position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)):
            self.pressed = True

    def draw_rumble(self,position,pressed):
        if self.pressed==True:
            if event.type == pygame.MOUSEBUTTONUP:
                if (position[0]<BOARD_WIDTH and position[1]<BOARD_HEIGHT):
                    placing_position = pygame.mouse.get_pos()
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+2,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION+1)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION+2)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION,placing_position[1]//Y_CELL_DIMENSION+3)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION+3)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+2,placing_position[1]//Y_CELL_DIMENSION+3)).draw(DISPLAY))

                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION,placing_position[1]//Y_CELL_DIMENSION+5)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION+5)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+2,placing_position[1]//Y_CELL_DIMENSION+5)).draw(DISPLAY))

                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION,placing_position[1]//Y_CELL_DIMENSION+6)).draw(DISPLAY))   
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION+6)).draw(DISPLAY)) 
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+2,placing_position[1]//Y_CELL_DIMENSION+6)).draw(DISPLAY)) 

                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION,placing_position[1]//Y_CELL_DIMENSION+8)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION+8)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+2,placing_position[1]//Y_CELL_DIMENSION+8)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION+9)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION+10)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION,placing_position[1]//Y_CELL_DIMENSION+11)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION+11)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+2,placing_position[1]//Y_CELL_DIMENSION+11)).draw(DISPLAY))

                    self.pressed = False
 

class button_spaceship():
    def __init__(self,image,pos):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.pressed = False

    def update(self,screen):
        screen.blit(self.image,self.rect)

    def check_for_input(self,position):
        if (position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)):
            self.pressed = True

    def draw_spaceship(self,position,pressed):
        if self.pressed==True:
            if event.type == pygame.MOUSEBUTTONUP:
                if (position[0]<BOARD_WIDTH and position[1]<BOARD_HEIGHT):
                    placing_position = pygame.mouse.get_pos()
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+1,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+2,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+3,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+4,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+5,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+6,placing_position[1]//Y_CELL_DIMENSION)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+6,placing_position[1]//Y_CELL_DIMENSION+1)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+6,placing_position[1]//Y_CELL_DIMENSION+2)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+5,placing_position[1]//Y_CELL_DIMENSION+3)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+3,placing_position[1]//Y_CELL_DIMENSION+4)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION+2,placing_position[1]//Y_CELL_DIMENSION+4)).draw(DISPLAY))
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION,placing_position[1]//Y_CELL_DIMENSION+3)).draw(DISPLAY))   
                    cells_set.add_living_cell(cell((placing_position[0]//X_CELL_DIMENSION,placing_position[1]//Y_CELL_DIMENSION+1)).draw(DISPLAY)) 

                    self.pressed = False


class cell(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        self.position = pos
        self.color = BLACK
        self.numbers_of_neighbors = 0
        self.square = pygame.rect

    def __eq__(self,other):
        if not isinstance(other,cell):
            return False
        else:
            return self.position == other.position and self.color == other.color

    def __hash__(self):
        return hash(self.position)

    def draw(self,surface):
        self.square = pygame.draw.rect(surface,self.color,(self.position[0]*X_CELL_DIMENSION,
                                        self.position[1]*Y_CELL_DIMENSION,
                                        X_CELL_DIMENSION,
                                        Y_CELL_DIMENSION))
        return self

    def get_pos_x(self):
        return self.position[0]

    def get_pos_y(self):
        return self.position[1]

    def get_numbers_of_neighbors(self):
        return self.numbers_of_neighbors

    def increment_number_of_neighbors(self,inn):
        self.numbers_of_neighbors = self.get_numbers_of_neighbors()+inn

    def reset_number_of_neighbors(self):
        self.numbers_of_neighbors = 0


class cells_set():

    def __init__(self):
        self.living_cells = set()
        self.dead_cells = set()
        self.set_of_cells_to_delete_at_next_era = set()
        self.set_of_cells_to_add_at_next_era = set()

    def add_living_cell(self,cell):
        self.living_cells.add(cell)

    def remove_living_cell(self,cell):
        del cell.square
        self.living_cells.discard(cell)

    def add_dead_cell(self,cell):
        self.dead_cells.add(cell)

    def remove_dead_cell(self,cell):
        self.dead_cells.discard(cell)

    def reset_dead_cell(self):
        self.dead_cells = set()

    def reset_cells_to_add(self):
        self.set_of_cells_to_add_at_next_era = set()

    def reset_cells_to_delete(self):
        self.set_of_cells_to_delete_at_next_era = set()

    def get_set_of_cells_to_delete_at_next_era(self):
        return self.set_of_cells_to_delete_at_next_era

    def get_set_of_cells_to_add_at_next_era(self):
        return self.set_of_cells_to_add_at_next_era

    def get_living_cells(self):
        return self.living_cells

    def get_dead_cells(self):
        return self.dead_cells

    def get_all_position(self):
        return [(c.get_pos_x(),c.get_pos_y()) for c in self.get_living_cells()]

    def get_all_neighbors(self):
        return [(c.numbers_of_neighbors) for c in self.get_living_cells()]

    def check_neighborhood(self):
        for c in self.get_living_cells():
            if ((c.get_pos_x()+1,c.get_pos_y()) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x(),c.get_pos_y()+1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x()-1,c.get_pos_y()) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x(),c.get_pos_y()-1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x()+1,c.get_pos_y()-1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x()+1,c.get_pos_y()+1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x()-1,c.get_pos_y()-1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x()-1,c.get_pos_y()+1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)

            if(c.get_numbers_of_neighbors()<2):
                self.set_of_cells_to_delete_at_next_era.add(c)
            if(c.get_numbers_of_neighbors()==2 or c.get_numbers_of_neighbors() ==3):
                pass
            if(c.get_numbers_of_neighbors()>=4):
                self.set_of_cells_to_delete_at_next_era.add(c)

    def find_dead_cells(self):
        for c in self.get_living_cells():
            self.add_dead_cell(cell((c.get_pos_x()+1,c.get_pos_y())))
            self.add_dead_cell(cell((c.get_pos_x()-1,c.get_pos_y())))
            self.add_dead_cell(cell((c.get_pos_x(),c.get_pos_y()+1)))
            self.add_dead_cell(cell((c.get_pos_x(),c.get_pos_y()-1)))
            self.add_dead_cell(cell((c.get_pos_x()+1,c.get_pos_y()+1))) 
            self.add_dead_cell(cell((c.get_pos_x()-1,c.get_pos_y()+1))) 
            self.add_dead_cell(cell((c.get_pos_x()+1,c.get_pos_y()-1))) 
            self.add_dead_cell(cell((c.get_pos_x()-1,c.get_pos_y()-1))) 

    def check_dead_cells(self):
        for c in self.get_dead_cells():
            if((c.get_pos_x()+1,c.get_pos_y()) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x(),c.get_pos_y()+1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x()-1,c.get_pos_y()) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x(),c.get_pos_y()-1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x()+1,c.get_pos_y()+1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x()+1,c.get_pos_y()-1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x()-1,c.get_pos_y()+1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)
            if((c.get_pos_x()-1,c.get_pos_y()-1) in self.get_all_position()):
                c.increment_number_of_neighbors(1)

            if c.get_numbers_of_neighbors() == 3:
                c.reset_number_of_neighbors()
                self.set_of_cells_to_add_at_next_era.add(c)

    def update_cells(self):
        for c in self.get_set_of_cells_to_delete_at_next_era():
            self.remove_living_cell(c)
        for c in self.get_living_cells():
            if ((c.get_pos_x() > NUMBER_OF_CELLS_X-1 or c.get_pos_x() < 0) or (c.get_pos_y() > NUMBER_OF_CELLS_Y-1 or c.get_pos_y() < 0)):
                c.color = WHITE
            c.reset_number_of_neighbors()
        for c in self.get_set_of_cells_to_add_at_next_era(): 
            if ((c.get_pos_x() > NUMBER_OF_CELLS_X-1 or c.get_pos_x() < 0) or (c.get_pos_y() > NUMBER_OF_CELLS_Y-1 or c.get_pos_y() < 0)):
                c.color = WHITE
            self.add_living_cell(c)

        self.reset_cells_to_add()
        self.reset_cells_to_delete()
        self.reset_dead_cell()

################################################################################

if __name__ == '__main__':
    
    cells_set = cells_set()
    set_flag = True

    button_glider_surface = pygame.image.load('images/glider.png')
    button_glider_surface = pygame.transform.scale(button_glider_surface,(150,150))
    button_glider = button_glider(button_glider_surface,(1036,100))

    button_rumble_surface = pygame.image.load('images/rumble.png')                         
    button_rumble_surface = pygame.transform.scale(button_rumble_surface,(200,80)) 
    button_rumble = button_rumble(button_rumble_surface,(1036,250))      

    button_spaceship_surface = pygame.image.load('images/spaceship.png')                          
    button_spaceship_surface = pygame.transform.scale(button_spaceship_surface,(150,150))   
    button_spaceship = button_spaceship(button_spaceship_surface,(1036,400))       

    # SETUP of the game initial state -----------------------------------------
    draw_grid(DISPLAY,BOARD_WIDTH,X_CELL_DIMENSION,Y_CELL_DIMENSION,BOARD_HEIGHT,GREY)
    print('Game Of Life: select your cells and press any key to start the game!')
    while set_flag:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                button_glider.check_for_input(mouse_pos)
                button_rumble.check_for_input(mouse_pos)
                button_spaceship.check_for_input(mouse_pos)
                if (not button_glider.pressed and not button_rumble.pressed and not button_spaceship.pressed and mouse_pos[0]<BOARD_WIDTH and mouse_pos[1]<BOARD_HEIGHT):
                    cells_set.add_living_cell(cell((mouse_pos[0]//X_CELL_DIMENSION,
                                            mouse_pos[1]//Y_CELL_DIMENSION)
                                            ).draw(DISPLAY))

                else:
                    button_glider.draw_glider(mouse_pos,button_glider.pressed)
                    button_rumble.draw_rumble(mouse_pos,button_rumble.pressed)
                    button_spaceship.draw_spaceship(mouse_pos,button_spaceship.pressed)

            elif event.type == pygame.KEYUP:
                set_flag = False
        button_glider.update(DISPLAY)
        button_rumble.update(DISPLAY)
        button_spaceship.update(DISPLAY)
        pygame.display.update()

    # LOOP of the game --------------------------------------------------------
    counter = 0
    era = 0
    while True:
        counter += 1
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

        if (counter == 10):
            counter = 0
            era += 1
            DISPLAY.fill(WHITE)
            draw_grid(DISPLAY,BOARD_WIDTH,X_CELL_DIMENSION,Y_CELL_DIMENSION,BOARD_HEIGHT,GREY)

            if len(cells_set.get_living_cells()) == 0:
                print(f'All cells died in {era} eras. LIFE ENDED')
                pygame.quit()
                sys.exit()

            cells_set.check_neighborhood()
            cells_set.find_dead_cells()
            cells_set.check_dead_cells()
            for c in cells_set.get_living_cells():
                c.draw(DISPLAY)
            cells_set.update_cells()
        button_glider.update(DISPLAY)
        button_rumble.update(DISPLAY)
        button_spaceship.update(DISPLAY)
        cells_set.get_living_cells()
        pygame.display.flip()
