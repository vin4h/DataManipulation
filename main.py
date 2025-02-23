from database.operation import Operation
from product.product import Product

class Main:
    def __init__(self):
        self.operation = Operation()
        self.product = Product()
    
    def start(self):
        self.operation.create_product_table()
        self.operation.create_product_formatted_table()
        count = self.operation.get_all()
        
        if len(count) == 0: #restricted to creating new 100 rows in the database
            self.product.data_load()
        
    

main = Main()

main.start()