from Pest import Pest
from Resource import Resource
from Stock import Stock
from StockConsoleView import StockConsoleView

s = Stock()
s.products = [Resource(),Resource()]


sc = StockConsoleView()
sc.consoleController()

# p.destroyResource()
