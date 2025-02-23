from database.connection import DatabaseConnection

class Operation:
    def __init__(self):
        self.db = DatabaseConnection()

    def create_product_table(self): 
        self.db.connect()
        query = "CREATE TABLE IF NOT EXISTS product (id SERIAL PRIMARY KEY, name VARCHAR(100), price FLOAT, country VARCHAR(30))"
        self.db.execute(query)
        self.db.commit()
        print("Product table created with success!")
        self.db.disconnect()
        
    def create_product_formatted_table(self):
        self.db.connect()
        query = "CREATE TABLE IF NOT EXISTS product_formatted (id SERIAL PRIMARY KEY, id_product int, converted_price_brl float, converted_price_usd float, converted_price_eur float, quote_brl float, quote_usd float, quote_eur float, created_at timestamp DEFAULT now(), CONSTRAINT fk_product FOREIGN KEY (id_product) REFERENCES product(id) ON DELETE CASCADE)"
        self.db.execute(query)
        self.db.commit()
        print("Product Formmated table created with success!")
        self.db.disconnect()
        
        
    def insert_product_table(self, name: str, price: float, country: str):
        try:
            self.db.connect()
            query = "INSERT INTO product (name, price, country) values (%s, %s, %s)"
            self.db.cursor.execute(query, (name, price, country))
            self.db.commit()
        except Exception as e:
            print(f"Error to insert product: {e}")
        finally:
            self.db.disconnect()
            
            
    def insert_product_formatted_table(self, id_product: int, converted_price_brl: float, converted_price_usd: float, converted_price_eur: float, quote_usd: float, quote_eur: float, quote_brl: float):
        try:
            self.db.connect()
            query = "INSERT INTO product_formatted (id_product, converted_price_brl, converted_price_usd, converted_price_eur, quote_usd, quote_eur, quote_brl) values (%s, %s, %s, %s, %s, %s, %s)"
            self.db.cursor.execute(query, (id_product, converted_price_brl, converted_price_usd, converted_price_eur, quote_usd, quote_eur, quote_brl))
            self.db.commit()
        except Exception as e:
            print(f"Error to insert product formatted: {e}")
        finally:
            self.db.disconnect()
            
    def get_all(self):
        try:
            self.db.connect()
            query = "SELECT * FROM product"
            self.db.execute(query)
            return self.db.fetch_all()
        except Exception as e:
            print(f"Error to find all product: {e}")
        finally:
            self.db.disconnect()