from database.operation import Operation
from product.product import Product

class Main:
    def __init__(self):
        self.operation = Operation()
        self.product = Product()
    
    def start(self):
        self.operation.createProductTable()
        self.product.data_load()
        
    

main = Main()

main.start()