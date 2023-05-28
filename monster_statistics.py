import pygame
import os


class Monster_main:
    monster_height = 0
    monster_width = 0    
    
    def __(self, monster_name, STR, DEX, INT, VIT, LUCK):
        self.monster_name = monster_name
        self.STR = STR
        self.DEX = DEX
        self.INT = INT
        self.VIT = VIT
        self.LUCK = LUCK
        self.attack = self.STR*10
        self.mana = self.INT*10
        self.dodge_chance = self.DEX*10
        self.ranged_DMG= self.DEX*5
        self.tenacity = self.VIT*5
        self.hit_points = self.VIT*10
        self.physical_crit_chance = self.LUCK*10
        self.magical_crit_chance = self.LUCK*10
        self.block = self.STR*5
        self.armor: 0
        self.lifesteal = 0
        self.piercing_armor = 0
        
#example of class inheretance        
class Dziki_pies(Monster_main):
    def __init__(self, monster_name, STR, DEX, INT, VIT, LUCK):
        super().__init__(monster_name,  STR, DEX, INT, VIT, LUCK)
        
    

pies = Dziki_pies('Dziki pies', 20,10,10,10,10)

print(pies.mana)
