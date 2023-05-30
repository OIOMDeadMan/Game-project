import pygame
import os
from game_assets.locations import image
import Enemies

class Board:
    # atrybuty planszy
    C = 32
    grid = []

    def __init__(self, location, hero_screen_position):
        self.board_image = pygame.image.load(os.path.join("game_assets/locations", location + ".png"))
        self.board_image = pygame.transform.scale(self.board_image, (3328, 2432))
        self.board_dim_x, self.board_dim_y = self.board_image.get_width(), self.board_image.get_height()

        for index_col, cell_x in enumerate(range(0, self.board_dim_x, self.C)):
            col = []
            for index_row, cell_y in enumerate(range(0, self.board_dim_y, self.C)):
                if 0 < index_row < (self.board_dim_y / 32 - 1) and 0 < index_col < (self.board_dim_x / 32 - 1):
                    col.append(Cell(cell_x, cell_y, index_col, index_row, True))
                else:
                    col.append(Cell(cell_x, cell_y, index_col, index_row, False))
            self.grid.append(col)

        for coords in image.closed_cells:
            self.grid[coords[0]][coords[1]].open = False

        self.hero_spawn_position = self.grid[20][20]
        self.starting_view_position_x = hero_screen_position[0] - self.hero_spawn_position.x
        self.starting_view_position_y = hero_screen_position[1] - self.hero_spawn_position.y

        self.map_position_x = self.starting_view_position_x
        self.map_position_y = self.starting_view_position_y


        self.spawn_objects()

    def spawn_objects(self):
        Enemies.Enemy(self.grid[20][20])



class Cell:
    def __init__(self, x, y, col, row, state):
        self.col = col
        self.row = row
        self.x = x
        self.y = y
        self.open = state
        self.content = None
