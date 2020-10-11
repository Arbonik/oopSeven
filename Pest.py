from random import Random

from Resource import Resource, Shaurma, Meat, Car


class Pest:
    def __init__(self):
        self.name = str()
        self.lovelyResource = [Resource()]
        # живучесть вредителя
        self.health = 30

    def death(self, damage: int):
        return self.health < damage

    def destroy(self, p: Resource):
        for i in self.lovelyResource:
            if type(p) == type(i):
                return True
        return False

    @staticmethod
    def instance():
        rand = Random().randint(0, 2)
        if (rand == 0):
            return Rat()
        elif rand == 1:
            return Fixick()
        elif rand == 2:
            return TrueEvil()


class Rat(Pest):
    def __init__(self):
        self.name = "Крыса (любит мясо и шаурму)"
        self.health = 30
        self.lovelyResource = [Shaurma(), Meat()]


class Fixick(Pest):
    def __init__(self):
        self.name = "Фиксик (любит машину и шаурму)"
        self.health = 100
        self.lovelyResource = [Car(), Meat()]


class TrueEvil(Pest):
    def __init__(self):
        self.name = "Чистое зло (любит все)"
        self.health = 200
        self.lovelyResource = [Car(), Meat(), Shaurma()]
