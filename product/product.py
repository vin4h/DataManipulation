import csv
import os

from database.operation import Operation

class Product:
     
        
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.csv = os.path.join(base_path, 'product.csv')
        self.operation = Operation()
    
    def data_load(self):
        with open(self.csv, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            next(reader)
            
            for row in reader:
                try:
                    name: str = row['name']
                    price: float = float(row['price'])
                    country: str = row['country']
                    
                    self.operation.insertProductTable(name, float(price), country)
                except Exception as e:
                    print(f"Erro listagem da row: {e}")
            
            print("Lista de produto inserido com sucesso!")