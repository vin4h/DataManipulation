from database.connection import DatabaseConnection

class Operation:
    def __init__(self):
        self.db = DatabaseConnection()

    def createProductTable(self): 
        self.db.connect()
        query = "CREATE TABLE IF NOT EXISTS product (id SERIAL PRIMARY KEY, name VARCHAR(100), price FLOAT, country VARCHAR(30))"
        self.db.execute(query)
        print("Tabela criada com sucesso!")
        self.db.disconnect()
        
    def insertProductTable(self, name: str, price: float, country: str):
        try:
            self.db.connect()
            query = "INSERT INTO product (name, price, country) values (%s, %s, %s)"
            self.db.cursor.execute(query, (name, price, country))
            self.db.commit()
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
        finally:
            self.db.disconnect()