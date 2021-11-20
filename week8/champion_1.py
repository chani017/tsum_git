class Champion:
    def __init__(self, name):
        self.name = name

class Mana_Champion(Champion):
    def __init__(self, name, hp, heal, mana, speed):
        self.name = name
        self.hp = hp
        self.heal = heal
        self.mana = mana
        self.speed = speed

    def cham_info(self):
        print(f"-----------------현재{self.name}정보-----------------")
        print(f"체력 : {self.hp}, 회복 : {self.heal}, 마나 : {self.mana}, 속도 : {self.speed}")

class Mana_none_Champion(Champion):
    def __init__(self, name, hp, heal, speed):
        self.name = name
        self.hp = hp
        self.heal = heal
        self.speed = speed
        
    def cham_info(self):
        print(f"-----------------현재{self.name}정보-----------------")
        print(f"체력 : {self.hp}, 회복 : {self.heal}, 속도 : {self.speed}")