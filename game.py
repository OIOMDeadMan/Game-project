import pygame
import hero_file
import board
import interface
import items


class Game:
    WIDTH, HEIGHT = 1280, 640
    FPS = 60
    hsp = [WIDTH / 2, HEIGHT / 2]  # hero screen position

    # clicks = []

    def __init__(self):
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.stats_win, self.inv_win = self.create_interface()
        self.heroes = self.create_heroes()
        self.board = self.create_map()

        self.hero_index = 0
        self.selected_hero = self.heroes[self.hero_index]
        self.selected_hero_frame = None

        items.spawn_item(items.generate_item(1, 1), self.board.grid[20][20])

        self.running = True
        self.run()

    def run(self):

        hero_model = hero_file.HeroModel(self.board.hero_spawn_position)
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(self.FPS)

            self.handle_keyboard_events(hero_model)

            self.draw_window(hero_model, self.board)

        pygame.quit()

    def draw_window(self, engine, bg):
        self.WIN.blit(bg.board_image, (self.board.map_position_x, self.board.map_position_y))

        self.draw_map_objects()

        self.WIN.blit(engine.current_image, (self.hsp[0], self.hsp[1] - bg.C / 2))

        self.draw_interface()
        self.draw_hero_icons()


        # for v in self.clicks:
        #     pygame.draw.rect(self.WIN, (255, 0, 0),
        #                      (v[0] * bg.C + bg.map_position_x, v[1] * bg.C + bg.map_position_y, bg.C, bg.C))

        pygame.display.update()

    # @staticmethod
    # def get_cell(pos, bg):
    #     cell_col = int(pos[0] // 32 - bg.map_position_x // 32)
    #     cell_row = int(pos[1] // 32 - bg.map_position_y // 32)
    #     clicked_cell = board.Board.grid[cell_col][cell_row]
    #
    #     return clicked_cell

    def handle_keyboard_events(self, engine):
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    engine.interact_cell(engine.orientation, self.board.grid)

                if event.key == pygame.K_c:
                    if self.stats_win.is_visible:
                        self.stats_win.is_visible = False
                    else:
                        self.stats_win.is_visible = True

                if event.key == pygame.K_i:
                    if self.inv_win.is_visible:
                        self.inv_win.is_visible = False
                    else:
                        self.inv_win.is_visible = True

                if event.key == pygame.K_TAB:
                    self.select_next_hero()

            # pos = pygame.mouse.get_pos()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     print(pos)
            #     cell = self.get_cell(pos, self.board)
            #     col = cell.col
            #     row = cell.row
            #     if [col, row] not in self.clicks:
            #         self.clicks.append([col, row])
            #     else:
            #         self.clicks.remove([col, row])
            #
            #     print(self.clicks)

        if any(keys_pressed[key] for key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]) \
                or engine.is_moving:
            engine.move(board.Board.grid, self.board, self.hsp, keys_pressed, engine.orientation)

    @staticmethod
    def create_interface():
        stats_win = interface.StatsWin()
        inv_win = interface.InventoryWin()
        return stats_win, inv_win

    @staticmethod
    def create_heroes():
        hero_1 = hero_file.Wizard("Maciej")
        hero_2 = hero_file.Warrior("Kuba")
        hero_3 = hero_file.Wizard("Stasiak")
        hero_4 = hero_file.Warrior("Jercha")
        return hero_1, hero_2, hero_3, hero_4

    def create_map(self):
        map = board.Board("image", self.hsp)
        return map

    def draw_interface(self):
        if self.stats_win.is_visible:
            self.WIN.blit(self.stats_win.stats_window, (128, 48))
            for item_type, item in self.selected_hero.eq.items():
                self.WIN.blit(item.icon, (item.draw_position[0], item.draw_position[1]))

        if self.inv_win.is_visible:
            self.WIN.blit(self.inv_win.inv_window, (632, 48))

    def draw_hero_icons(self):
        self.WIN.blit(self.heroes[0].hero_icon, (0, 64))
        self.WIN.blit(self.heroes[1].hero_icon, (0, 192))
        self.WIN.blit(self.heroes[0].hero_icon, (0, 320))
        self.WIN.blit(self.heroes[1].hero_icon, (0, 448))

        frame_pos = int(self.hero_index % len(self.heroes)) * 128 + 64
        self.selected_hero_frame = pygame.draw.rect(self.WIN, "green", (0, frame_pos, 100, 100), width=2)

    def select_next_hero(self):
        self.hero_index += 1
        self.selected_hero = self.heroes[self.hero_index % len(self.heroes)]

        print(self.selected_hero)

    @staticmethod
    def refresh(hero):
        for key, value in hero.eq.items():
            try:
                for stat, number in value.stats.items():
                    try:
                        hero.stats[stat] = hero.stats.get(stat, 0) + value.stats.get(stat, 0)
                    except AttributeError:
                        pass
            except AttributeError:
                pass
        print(hero.stats['STR'])

    def draw_map_objects(self):
        for row in self.board.grid:
            for cell in row:
                if cell.content is not None:
                    self.WIN.blit(pygame.transform.scale(cell.content.icon, (32, 32)),
                                  ((cell.col * self.board.C + self.board.map_position_x),
                                  (cell.row * self.board.C + self.board.map_position_y)))


g = Game()
