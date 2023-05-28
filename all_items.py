class melle_weapon:
    def __init__(self, name, upgrade):
        self.name = name
        self.upgrade = upgrade
        self.DMG = 0
        self.Is_twohanded = True
        self.armor_penetration = 0
        self.physical_crit_chance = 0
        self.price = 0
        self.additional_effect = ''
        self.weapon_type()
        self.weapon_upgrade()
    def weapon_type(self):
        match self.name:
            case 'Dagger':
                self.DMG = 5
                self.armor_penetration = 5
                self.physical_crit_chance = 30
                self.price = 100
            case 'Sword':
                self.DMG = 8
                self.armor_penetration = 3
                self.physical_crit_chance = 10
                self.price = 200
            case 'Long sword':
                self.DMG = 10
                self.armor_penetration = 8
                self.physical_crit_chance = 15
                self.price = 300
            case 'Two-handed sword':
                self.DMG = 20
                self.armor_penetration = 15
                self.physical_crit_chance = 30
                self.price = 400
                self.Is_twohanded = False
            #case 'Short bow':
    def weapon_upgrade(self):
        if self.upgrade > 0:
            self.name = self.name, '+', self.upgrade
            self.DMG += self.upgrade
            self.armor_penetration += self.upgrade
            self.physical_crit_chance = 0
            self.price += self.price + self.upgrade*100

#sekcja broni melle
dagger_0 = melle_weapon('Dagger', 0)
dagger_1 = melle_weapon('Dagger', 1)
dagger_2 = melle_weapon('Dagger', 2)
dagger_3 = melle_weapon('Dagger', 3)
dagger_4 = melle_weapon('Dagger', 4)
dagger_5 = melle_weapon('Dagger', 5)
dagger_6 = melle_weapon('Dagger', 6)
dagger_7 = melle_weapon('Dagger', 7)
dagger_8 = melle_weapon('Dagger', 8)
dagger_9 = melle_weapon('Dagger', 9)

sword_0 = melle_weapon('Sword', 0)
sword_1 = melle_weapon('Sword', 1)
sword_2 = melle_weapon('Sword', 2)
sword_3 = melle_weapon('Sword', 3)
sword_4 = melle_weapon('Sword', 4)
sword_5 = melle_weapon('Sword', 5)
sword_6 = melle_weapon('Sword', 6)
sword_7 = melle_weapon('Sword', 7)
sword_8 = melle_weapon('Sword', 8)
sword_9 = melle_weapon('Sword', 9)


class ranged_weapon:
    def __int__(self, name, upgrade):
        self.name = name
        self.upgrade = upgrade
        self.DMG = 0
        self.armor_penetration = 0
        self.physical_crit_chance = 0
        self.price = 0
        self.additional_effect = ''
        self.weapon_type()
        self.weapon_upgrade()