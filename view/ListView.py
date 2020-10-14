import tkinter as tk


# суперкласс для отображения списков
class ListView:
    name = str()

    def __init__(self, root, elements):
        self.elements = elements
        self.myFrame = tk.LabelFrame(root, text = self.name)
        self.update()

    def update(self):
        for item in self.myFrame.winfo_children():
            item.destroy()

        for element in self.elements:
            pestLabel = tk.Label(self.myFrame, text = element.name)
            pestLabel.pack(side = tk.BOTTOM)

        self.myFrame.pack(side = tk.RIGHT)

class PestsView(ListView):
    name = "Вредители"


class ResourceView(ListView):
    name = "Ресурсы"

