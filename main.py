from database.operation import Operation
from product.product import Product

class Main:
    def __init__(self):
        self.operation = Operation()
        self.product = Product()
    
    def start(self):
        self.operation.create_product_table()
        self.operation.create_product_formatted_table()
        self.product.data_load()
        
    

main = Main()

main.start()