class Champion:
    def __init__(self, name):
        self.name = name

class Mana_Champion(Champion):
    def __init__(self, name):
        self.name = name
        self.hp = 1000
        self.heal = 15
        self.mana = 1000
        self.speed = 300

    def cham_info(self):
        print(f"-----------------현재{self.name}정보-----------------")
        print(f"체력 : {self.hp}, 회복 : {self.heal}, 마나 : {self.mana}, 속도 : {self.speed}")

class Mana_none_Champion(Champion):
    def __init__(self, name):
        self.name = name
        self.hp = 1000
        self.heal = 15
        self.speed = 300
        
    def cham_info(self):
        print(f"-----------------현재{self.name}정보-----------------")
        print(f"체력 : {self.hp}, 회복 : {self.heal}, 속도 : {self.speed}")
