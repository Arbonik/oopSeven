from Resource import Resource
from Stock import Stock


class StockConsoleView:
    def __init__(self):
        self.stock = Stock()

    def consoleController(self):
        while True:
            self.stock.update()
            self.show()
            print("Какие действия предпринять?")
            print("1: добавить продуктов на склад")
            print("2: протравить вредителей")
            print("3: выйти")
            playerInput = input()
            if "1" == playerInput:
                self.stock.addResource(Resource.instance())
            elif "2" == playerInput:
                self.stock.buyPoison()
            elif "3" == playerInput:
                break

    def show(self):

        self.showProduct()
        self.showPets()

    def showProduct(self):
        print("Продукты на складе: ")
        for p in self.stock.products:
            print(p)
        print("Свободного места: " + str(self.stock.capacity))

    def showPets(self):
        if len(self.stock.pests) == 0:
            print("Вредителей нет")
        else:
            print("Вредителей на складе: " + str(len(self.stock.pests)))
            for pets in self.stock.pests:
                print(" - " + pets.name)
