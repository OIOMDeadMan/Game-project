import pygame.image


class Interface:
    def __init__(self):
        self.is_visible = False

    def show(self):
        self.is_visible = True

    def hide(self):
        self.is_visible = False


class StatsWin(Interface):
    def __init__(self):
        super().__init__()
        self.stats_window = pygame.image.load("game_assets/UI/stats.png")


class InventoryWin(Interface):
    def __init__(self):
        super().__init__()
        self.inv_window = pygame.image.load("game_assets/UI/inventory.png")
