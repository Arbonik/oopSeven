class Resource:

    def __init__(self):
        self.name = ""
        # Стоимость размещения на складе
        self.cost = 10
    #     Количество треуемого места
        self.capacity = 10

    def __str__(self) -> str:
        return " - " + self.name + "(Доход: " + str(self.cost) + " занимаемое место: " + str(self.capacity) + ")"

    @staticmethod
    def instance():
        print("Какой продукт хотите разместить на складе?")
        print("1: " + str(Shaurma()))
        print("2: " + str(Meat()))
        print("3: " + str(Car()))
        p = int(input())
        if p == 1:
            return Shaurma()
        elif p == 2:
            return Meat()
        elif p == 3:
            return Car()

class Shaurma(Resource):

    def __init__(self):
        self.name = "Шаурма"
        self.cost = 5
        self.capacity = 5

class Car(Resource):

    def __init__(self):
        self.name = "Машина"
        self.cost = 120
        self.capacity = 50

class Meat(Resource):

    def __init__(self):
        self.name = "Мясо"
        self.cost = 30
        self.capacity = 10

