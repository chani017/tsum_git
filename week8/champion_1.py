class Champion:
    def __init__(self, name):
        self.name = name
        self.hp = 1000
        self.cure = 15
        self.speed = 300

class Mana_Champion(Champion):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 1000

    def cham_info(self):
        print(f"-----------------현재{self.name}정보-----------------")
        print(f"체력 : {self.hp}, 회복 : {self.cure}, 마나 : {self.mana}, 속도 : {self.speed}")

class Mana_none_Champion(Champion):
    def __init__(self, name):
        super().__init__(name)
        
    def cham_info(self):
        print(f"-----------------현재{self.name}정보-----------------")
        print(f"체력 : {self.hp}, 회복 : {self.cure}, 속도 : {self.speed}")
