import pygame
import os
import items


class HeroModel:

    # inicjalizacja parametrów bohatera, parametr spawn_position zaczytuje się zależnie od aktualnie wczytanej mapy
    def __init__(self, position_cell):
        self.height = 48
        self.width = 32
        self.position_cell = position_cell
        self.position_x = position_cell.x
        self.position_y = position_cell.y
        self.VEL = 4
        self.orientation = "S"
        self.is_moving = False

        self.inventory = []

        self.images = {}
        self.load_hero_images()
        self.current_image = self.images["N0.png"]

    def load_hero_images(self):
        sc = pygame.transform.scale
        ld = pygame.image.load
        jn = os.path.join
        self.images = {file_name: sc(ld(jn("game_assets/sprite", file_name)).convert_alpha(), (32, 48))
                       for file_name in os.listdir("game_assets/sprite") if file_name != "__init__.py"}

    def move(self, grid, current_map, hsp, keys_pressed, orientation):
        col = self.position_cell.col
        row = self.position_cell.row
        default_hsp = 640, 320

        def up():
            self.orientation = "N"
            self.current_image = self.images["N0.png"]
            self.is_moving = True
            destination_cell = grid[col][row - 1]
            if not destination_cell.open:
                self.is_moving = False
                return False

            self.position_y -= self.VEL

            if self.position_y % 32 < 16:
                self.current_image = self.images["N1.png"]
            else:
                self.current_image = self.images["N2.png"]

            if hsp[1] != default_hsp[1]:
                hsp[1] -= self.VEL

            elif current_map.board_dim_y - hsp[1] > destination_cell.y >= hsp[1]:
                current_map.map_position_y += self.VEL

            else:
                hsp[1] -= self.VEL

            if self.position_y <= destination_cell.y:
                self.position_cell = destination_cell
                self.position_y = self.position_cell.y
                self.is_moving = False
                self.current_image = self.images["N0.png"]
                print(self.position_x, self.position_y)

        def left():
            self.orientation = "W"
            self.current_image = self.images["W0.png"]
            self.is_moving = True
            destination_cell = grid[col - 1][row]
            if not destination_cell.open:
                self.is_moving = False
                return False

            self.position_x -= self.VEL

            if self.position_x % 32 < 16:
                self.current_image = self.images["W1.png"]
            else:
                self.current_image = self.images["W2.png"]

            if hsp[0] != default_hsp[0]:
                hsp[0] -= self.VEL

            elif current_map.board_dim_x - hsp[0] > destination_cell.x >= hsp[0]:
                current_map.map_position_x += self.VEL

            else:
                hsp[0] -= self.VEL

            if self.position_x <= destination_cell.x:
                self.position_cell = destination_cell
                self.position_x = self.position_cell.x
                self.is_moving = False
                self.current_image = self.images["W0.png"]
                print(self.position_cell.col, self.position_cell.row)

        def down():
            self.orientation = "S"
            self.current_image = self.images["S0.png"]
            self.is_moving = True
            destination_cell = grid[col][row + 1]
            if not destination_cell.open:
                self.is_moving = False
                return False

            self.position_y += self.VEL

            if self.position_y % 32 < 16:
                self.current_image = self.images["S1.png"]
            else:
                self.current_image = self.images["S2.png"]

            if hsp[1] != default_hsp[1]:
                hsp[1] += self.VEL

            elif current_map.board_dim_y - hsp[1] >= destination_cell.y > hsp[1]:
                current_map.map_position_y -= self.VEL

            else:
                hsp[1] += self.VEL

            if self.position_y >= destination_cell.y:
                self.position_cell = destination_cell
                self.position_y = self.position_cell.y
                self.is_moving = False
                self.current_image = self.images["S0.png"]
                print(self.position_cell.col, self.position_cell.row)

        def right():
            self.orientation = "E"
            self.current_image = self.images["E0.png"]
            destination_cell = grid[col + 1][row]

            self.is_moving = True
            if not destination_cell.open:
                self.is_moving = False
                return False

            self.position_x += self.VEL

            if self.position_x % 32 < 16:
                self.current_image = self.images["E1.png"]
            else:
                self.current_image = self.images["E2.png"]

            if hsp[0] != default_hsp[0]:
                hsp[0] += self.VEL

            elif current_map.board_dim_x - hsp[0] >= destination_cell.x > hsp[0]:
                current_map.map_position_x -= self.VEL

            else:
                hsp[0] += self.VEL

            if self.position_x >= destination_cell.x:
                self.position_cell = destination_cell
                self.position_x = self.position_cell.x
                self.is_moving = False
                self.current_image = self.images["E0.png"]
                print(self.position_cell.col, self.position_cell.row)

        if not self.is_moving and keys_pressed[pygame.K_w]:
            up()

        elif not self.is_moving and keys_pressed[pygame.K_a]:
            left()

        elif not self.is_moving and keys_pressed[pygame.K_s]:
            down()

        elif not self.is_moving and keys_pressed[pygame.K_d]:
            right()

        elif self.is_moving and orientation == "N":
            up()

        elif self.is_moving and orientation == "W":
            left()

        elif self.is_moving and orientation == "S":
            down()

        elif self.is_moving and orientation == "E":
            right()

    def interact_cell(self, orientation, grid):
        # interaction with a cell that hero s standing on
        if self.position_cell.content is not None:
            self.position_cell.content.interact(self)

        else:
        # interaction with a cell that hero is looking at
            try:
                if orientation == "N":
                    interacted_cell = grid[self.position_cell.col][self.position_cell.row - 1]
                    interacted_cell.content.interact()

                elif orientation == "W":
                    interacted_cell = grid[self.position_cell.col - 1][self.position_cell.row]
                    interacted_cell.content.interact()

                elif orientation == "S":
                    interacted_cell = grid[self.position_cell.col][self.position_cell.row + 1]
                    interacted_cell.content.interact()

                elif orientation == "E":
                    interacted_cell = grid[self.position_cell.col + 1][self.position_cell.row]
                    interacted_cell.content.interact()
            except AttributeError:
                print("Nic tu nie ma")


class Hero:
    def __init__(self, name):
        self.name = name
        self.eq = dict(helmet=items.no_item, armor=items.no_item, trousers=items.no_item,
                       boots=items.no_item, hand1=items.no_item, hand2=items.no_item, bracers=items.no_item,
                       gloves=items.no_item, bracelet=items.no_item, necklace=items.no_item,
                       amulet=items.no_item)

    def attack(self, enemy):
        pass

    def cast_spell(self, spell):
        pass

    def step(self, fighting_row):
        pass

    def lvl_up(self, current_lvl):
        pass

    def add_stat(self, stat):
        pass

    def upgrade_spell(self, spell):
        pass

    def upgrade_skill(self, skill):
        pass

    def use_item(self, item):
        pass

    def upgrade_class(self, new_class):
        pass


class Wizard(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.hero_class = "wizard"
        self.hero_icon = pygame.image.load("game_assets/UI/wizard_icon.png")
        self.STR = 4
        self.DEX = 4
        self.INT = 8
        self.LUC = 6


class Priest(Wizard):
    def __init__(self, name):
        super().__init__(name)
        self.STR += 4
        self.DEX += 4
        self.INT += 10
        self.LUC += 4


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.hero_icon = pygame.image.load("game_assets/UI/warrior_icon.png")
        self.STR = 4
        self.DEX = 4
        self.INT = 8
        self.LUC = 6

