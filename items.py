import os
import random
import pygame.image


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

    def __init__(self, item_type, item_icon=pygame.image.load("game_assets/items/no_item.png")):
        self.iname = None
        self.itype = item_type
        self.icon = item_icon
        self.irarity = None
        self.ilvl = None
        self.draw_position = EqItem.eq_slots[item_type]
        self.iclasses = None
        self.istats = {"ARMOR": 0, "STR": 0, "DEX": 0, "INT": 0, "LUC": 0}

    def equip_item(self, selected_hero):
        if selected_hero.hero_class in self.iclasses and selected_hero.lvl == self.ilvl:
            selected_hero.eq[f"{self.itype}"] = self

    @staticmethod
    def unequip_item(item, selected_hero):
        selected_hero.eq[item.type] = item.__class__


no_item = EqItem("no_item", None)

wooden_helmet = EqItem("helmet",
                       pygame.image.load("game_assets/items/helmet_test.png"))
helmet_names = ['Drewniany hełm', 'Skórzany hełm', 'Stalowy hełm', 'Smoczy hełm']
rarity_types = ['common', 'rare', 'epic', 'legendary']
class_types = ['warrior', 'wizard', 'rogue']
def random_item(obj, name_list, rarity_list, class_list):
    obj.iname = random.choice(name_list)
    obj.irarity = random.choice(rarity_list)
    obj.iclasses = random.choice(class_list)
    obj.ilvl = random.randint(1,100)
    obj.istats['ARMOR'] = int(obj.ilvl * 2)
    obj.istats['STR'] = int(obj.ilvl * 1)
    obj.istats['DEX'] = int(obj.ilvl * 1)
    obj.istats['INT'] = int(obj.ilvl * 1)
    obj.istats['LUC'] = int(obj.ilvl * 1)
    match obj.iname:
        case 'Drewniany hełm':
            obj.istats['ARMOR'] += 10
        case 'Skórzany hełm':
            obj.istats['ARMOR'] += 20
        case 'Stalowy hełm':
            obj.istats['ARMOR'] += 40
        case 'Smoczy hełm':
            obj.istats['ARMOR'] += 50
    match obj.irarity:
        case 'common':
            obj.istats['ARMOR'] += 10
            obj.istats['STR'] += 2
            obj.istats['DEX'] += 2
            obj.istats['INT'] += 2
            obj.istats['LUC'] += 2
        case 'rare':
            obj.istats['ARMOR'] += 20
            obj.istats['STR'] += 4
            obj.istats['DEX'] += 4
            obj.istats['INT'] += 4
            obj.istats['LUC'] += 4
        case 'epic':
            obj.istats['ARMOR'] += 40
            obj.istats['STR'] += 6
            obj.istats['DEX'] += 6
            obj.istats['INT'] += 6
            obj.istats['LUC'] += 6
        case 'legendary':
            obj.istats['ARMOR'] += 80
            obj.istats['STR'] += 10
            obj.istats['DEX'] += 10
            obj.istats['INT'] += 10
            obj.istats['LUC'] += 10
    match obj.iclasses:
        case 'warrior':
            obj.istats['STR'] += 5
        case 'wizard':
            obj.istats['INT'] += 5
        case 'rogue':
            obj.istats['DEX'] += 5


helm = EqItem("helmet",
                       pygame.image.load("game_assets/items/helmet_test.png"))

random_item(helm, helmet_names, rarity_types,class_types)
print(vars(helm))