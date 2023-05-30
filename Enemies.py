class Enemy:
    def interact(self):
        print("Zaatakowano przeciwnika")

    def spawn(self, cell):
        cell.content = self
        cell.open = False
