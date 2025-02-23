import csv
import os

from database.operation import Operation
from third_party_api.awesome import AwesomeApi

class Product:
     
        
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.csv = os.path.join(base_path, 'product.csv')
        self.operation = Operation()
        self.awesome_api = AwesomeApi()
        self.usd_brl_response = "USDBRL"
        self.usd_eur_response = "USDEUR"
        self.eur_brl_response = "EURBRL"
        self.eur_usd_response = "EURUSD"
        self.brl_usd_response = "BRLUSD"
        self.brl_eur_response = "BRLEUR"
        self.br_country = "Brazil"
        self.eu_country = "Europe"
        self.usa_country = "EUA"
    
    def data_load(self):
        with open(self.csv, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            next(reader)
            
            for row in reader:
                try:
                    name: str = row['name']
                    price: float = float(row['price'])
                    country: str = row['country']
                    
                    self.operation.insert_product_table(name, float(price), country)
                except Exception as e:
                    print(f"Error listing row: {e}")
            
            print("List of product has inserted with success sucesso!")
            

    def formatted_product(self): 
        products = self.get_all_product()
        current_quotes = self.awesome_api.get_all_quote()
        for product in products:
            match product['country']:
                case self.br_country:
                    #todo get and processos values
                    price = product['price']
                    quote_brl = 1
                    quote_usd = current_quotes
                    print()
                case self.eu_country:
                    print()
                case self.usa_country:
                    print()
                case _:
                    print(f'Country notfound {product['country']}')
        
    def insert_product_formatted(self, product_formatted):
        id_product: int = product_formatted['id_product']
        converted_price_brl: float = product_formatted['converted_price_brl']
        converted_price_usd: float = product_formatted['converted_price_usd']
        converted_price_eur: float = product_formatted['converted_price_eur']
        quote_usd: float = product_formatted['quote_usd']
        quote_eur: float = product_formatted['quote_eur']
        quote_brl: float = product_formatted['quote_brl']
        
        self.operation.insert_product_formatted_table(id_product, converted_price_brl, converted_price_usd, converted_price_eur, quote_usd, quote_eur, quote_brl)
        
        
    
    def get_all_product(self):
        return self.operation.get_all()
    