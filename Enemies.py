class Enemy:
    def __init__(self, cell):
        self.hit_count = 0
        self.cell = cell
        cell.content = self
        cell.open = False


    def interact(self):
        print("Zaatakowano przeciwnika")
        self.hit_count += 1
        if self.hit_count >= 5:
            self.cell.open = True
            self.cell.content = None
            print('Pokonano przeciwnika')





    def spawn(self, cell):
        cell.content = self
        cell.open = False
