import pygame.image
import random as rd


class Inventory:
    inv_pos = 632, 48

    def __init__(self):
        self.slots = []
        slot_count_per_row = 640 // InvSlot.size[0]

        for row in range(Inventory.inv_pos[1] + 8, 544 // InvSlot.size[1]):
            for col in range(slot_count_per_row):
                x = Inventory.inv_pos[0] + 8 + col * InvSlot.size[0]
                y = Inventory.inv_pos[1] + 8 + row * InvSlot.size[1]
                self.slots.append(InvSlot((x, y)))


class InvSlot:
    size = 64, 64

    def __init__(self, position):
        self.content = None
        self.image = pygame.image.load("game_assets/items/no_item.png")
        self.position = position


class EqItem:
    eq_slots = {"helmet": (337, 99),
                "armor": (337, 168),
                "trousers": (337, 237),
                "boots": (337, 306),
                "hand1": (268, 168),
                "hand2": (406, 168),
                "bracers": (268, 237),
                "gloves": (406, 237),
                "bracelet": (520, 99),
                "necklace": (520, 168),
                "amulet": (520, 237),
                "no_item": (-1, -1)}

    item_type_list = [key for key, value in eq_slots.items()]
    item_name_list = {}

    def __init__(self, item_name, item_type, item_rarity, required_lvl,
                 item_armor, item_str, item_dex, item_int, item_luc,
                 item_class, item_icon=pygame.image.load("game_assets/items/sword.png")):
        self.iname = item_name
        self.itype = item_type
        self.icon = item_icon
        self.irarity = item_rarity
        self.ilvl = required_lvl
        self.draw_position = EqItem.eq_slots[item_type]
        self.iclasses = item_class
        self.istats = {"ARMOR": item_armor, "STR": item_str, "DEX": item_dex, "INT": item_int, "LUC": item_luc}

    def equip_item(self, selected_hero):
        if selected_hero.hero_class in self.iclasses and selected_hero.lvl == self.ilvl:
            selected_hero.eq[f"{self.itype}"] = self

    @staticmethod
    def unequip_item(item, selected_hero):
        selected_hero.eq[item.type] = item.__class__

    def interact(self, hero):
        hero.inventory.append(self)
        hero.position_cell.content = None


no_item = EqItem(None, "no_item", None, None, None, None, None, None, None, None)


def generate_item(minlvl, maxlvl):
    rarity_list = {"common": 1, "uncommon": 1.2, "epic": 1.5, "legendary": 2}
    classes_coefficient = {"warrior": {"ARMOR": 4, "STR": 3, "INT": 0.5, "DEX": 1, "LUC": 2},
                           "wizard": {"ARMOR": 2, "STR": 0.5, "INT": 3, "DEX": 0.5, "LUC": 2},
                           "rogue": {"ARMOR": 3, "STR": 1, "INT": 0.5, "DEX": 3, "LUC": 2}}
    rarity_drop_chance = [50, 40, 8, 2]

    itype = rd.choice([key for key, value in EqItem.eq_slots.items()])

    with open(f"game_assets/items/{itype}_names.txt", "r") as file:
        content = file.read()
        names = content.split(", ")
        iname = rd.choice(names)

    irarity = rd.choices(list(rarity_list.keys()), weights=rarity_drop_chance)[0]

    ilvl = rd.randint(int(minlvl), int(maxlvl))

    iclass = rd.choice(list(classes_coefficient.keys()))

    item_modificator = ilvl * rarity_list[irarity]

    iarmor = rd.randint(int(item_modificator * classes_coefficient[iclass]["ARMOR"] * 10),
                        int(item_modificator * classes_coefficient[iclass]["ARMOR"] * 12))

    istr = rd.randint(int(item_modificator * classes_coefficient[iclass]["STR"] * 1),
                      int(item_modificator * classes_coefficient[iclass]["STR"] * 1.2))

    iint = rd.randint(int(item_modificator * classes_coefficient[iclass]["INT"] * 1),
                      int(item_modificator * classes_coefficient[iclass]["INT"] * 1.2))

    idex = rd.randint(int(item_modificator * classes_coefficient[iclass]["DEX"] * 1),
                      int(item_modificator * classes_coefficient[iclass]["DEX"] * 1.2))

    iluc = rd.randint(int(item_modificator * classes_coefficient[iclass]["LUC"] * 1),
                      int(item_modificator * classes_coefficient[iclass]["LUC"] * 1.2))

    item = EqItem(iname, itype, irarity, ilvl, iarmor, istr, idex, iint, iluc, iclass)

    return item


def spawn_item(item, cell):
    cell.content = item

# min_lvl = input("min lvl: ")
# max_lvl = input("max lvl: ")
#
# it = generate_item(min_lvl, max_lvl)
# print(f"Nazwa: {it.iname}, typ: {it.itype}, lvl: {it.ilvl}, klasa: {it.iclasses}, rzedkość: {it.irarity},"
#       f"Siła: {it.istats['STR']}, Zręka: {it.istats['DEX']}, INT: {it.istats['INT']}, Luck: {it.istats['LUC']}")
