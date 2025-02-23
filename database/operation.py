from database.connection import DatabaseConnection

class Operation:
    def __init__(self):
        self.db = DatabaseConnection()

    def create_product_table(self): 
        self.db.connect()
        query = "CREATE TABLE IF NOT EXISTS product (id SERIAL PRIMARY KEY, name VARCHAR(100), price FLOAT, country VARCHAR(30))"
        self.db.execute(query)
        print("Tabela product criada com sucesso!")
        self.db.disconnect()
        
    def create_product_formatted_table(self):
        self.db.connect()
        query = "CREATE TABLE IF NOT EXISTS product_formatted (id SERIAL PRIMARY KEY, id_product int, converted_price_brl float, converted_price_usd float, converted_price_eur float, quote_brl float, quote_usd float, quote_eur float)"
        self.db.execute(query)
        print("Tabela product_formatted criada com sucesso!")
        self.db.disconnect()
        
        
    def insert_product_table(self, name: str, price: float, country: str):
        try:
            self.db.connect()
            query = "INSERT INTO product (name, price, country) values (%s, %s, %s)"
            self.db.cursor.execute(query, (name, price, country))
            self.db.commit()
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
        finally:
            self.db.disconnect()
            
    def get_all(self):
        try:
            self.db.connect()
            query= "SELECT * FROM product"
            self.db.execute(query)
            self.db.disconnect()
        except Exception as e:
            print(f"Erro ao buscar todos os produtos: {e}")
        finally:
            self.db.disconnect()