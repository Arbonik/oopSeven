import tkinter as tk

from model.Resource import Car, ResourceDepository
from model.Stock import Stock
from view.ListView import PestsView, ResourceView, ListView


class StockView:

    # freeSpace
    # income
    # interface
    def __init__(self):
        self.stock = Stock.instance()

        self.mainView = tk.Tk()

        self.fillContrellerFrame(self.mainView)
        self.petstList = PestsView(self.mainView, self.stock.pests)
        self.resourceList = ResourceView(self.mainView, self.stock.products)

        self.mainView.mainloop()

    def addProduct(self):
        index = self.listBoxResource.index(self.listBoxResource.curselection())

        quantity = int(self.quantity.get())

        for i in range(int(quantity)):
            self.stock.addResource(ResourceDepository.get(index))

        self.updateUI()

        self.freeSpaceLabel.config(text = "Свободное место на складе: " + str(self.stock.capacity))

    def fillContrellerFrame(self, root):

        self.controller = tk.LabelFrame(root, text="Управление")

        # настраивает панель расположения товаров
        self.marketView()

        # настраивает чистку
        self.clearPanel()

        for view in self.controller.winfo_children():
            view.pack()

        self.controller.pack(side = tk.LEFT)

    def clear(self):
        money = int(self.poisonQantity.get())
        self.stock.buyPoison(money)
        self.updateUI()


    def clearPanel(self):
        self.moneyLabel = tk.Label(self.controller, text="Доступные средства: ")
        # self.resourceList
        microFrame = tk.Frame(self.controller)
        self.buyPoison = tk.Button(microFrame, text="Протравить вредителей")
        self.buyPoison.config(command = self.clear)
        self.buyPoison.pack(side = tk.LEFT)
        self.poisonQantity = tk.Entry(microFrame, width = 5)
        self.poisonQantity.pack(side = tk.RIGHT)

    def marketView(self):
        self.freeSpaceLabel = tk.Label(self.controller, text="Свободное место на складе: ")
        self.rentFrame = tk.Frame(self.controller)

        self.listBoxResource = tk.Listbox(self.controller, width=45)
        for res in ResourceDepository.__reversed__():
            self.listBoxResource.insert(0, str(res))

        self.resourceButton = tk.Button(self.rentFrame, text="Разместить ресурс")
        self.resourceButton.pack(side=tk.LEFT)
        self.resourceButton.config(command = self.addProduct)
        # Количество товара
        self.quantity = tk.Entry(self.rentFrame, width=5)
        self.quantity.pack(side=tk.RIGHT)

    def updateUI(self):
        self.moneyLabel.config(text = "Доступные средства: " + str(self.stock.money))
        self.stock.update()
        self.resourceList.update()
        self.petstList.update()


StockView()
