from random import Random

from Pest import Pest
from Resource import Resource


class Stock:

    def __init__(self):

        self.products = list()
        # Вредители
        self.pests = list()
        # отрава
        self.poison = 0
        # вместимость склада
        self.capacity = 100
        self.money = 0

    def addResource(self, resource: Resource):
        if resource.capacity <= self.capacity:
            self.capacity -= resource.capacity
            self.products.append(resource)
        else:
            print("Недостаточно места на складе")

    # Подсчет прибыли за аренду склада
    def rent(self):
        sum = 0
        for i in self.products:
            sum += i.cost
        return sum

    def buyPoison(self):
        print("Сколько направить на борьбу с вредителями?")
        print("Доступно средств: " + str(self.money))
        buy = int(input())
        if buy <= self.money:
            self.money -= buy
            self.poison += buy
            for pets in self.pests:
                if pets.death(self.poison):
                    self.poison -= pets.health
                    self.pests.remove(pets)

    def update(self):
        # Расчет прибыли, порчи имущества,
        self.money += self.rent()
        self.pestUpdate()

    def pestUpdate(self):
        for product in self.products:
            for pets in self.pests:
                if pets.destroy(product):
                    self.capacity += product.capacity
                    self.products.remove(product)
                    break

        # шанс появления вредителей увеличивается с увеличением хранимых ресурсов
        if Random().randint(0, 100) > self.capacity:
            self.pests.append(Pest.instance())