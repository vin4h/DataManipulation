from dotenv import load_dotenv
import requests
import os

class AwesomeApi:
    def __init__(self):
        load_dotenv()
        self.base_url = "https://economia.awesomeapi.com.br/json/last"
        self.usd_brl_coin = "USD-BRL"
        self.usd_eur_coin = "USD-EUR"
        self.eur_brl_coin = "EUR-BRL"
        self.eur_usd_coin = "EUR-USD"
        self.brl_usd_coin = "BRL-USD"
        self.brl_eur_coin = "BRL-EUR"
        self.converted_price_brl_usd = "Brasil to USA"
        self.converted_price_brl_eur = "Brasil to Europe"
        self.converted_price_usd_brl = "USA to Brasil"
        self.converted_price_usd_eur = "USA to Europe"
        self.converted_price_eur_usd = "Europe to USA"
        self.converted_price_eur_brl = "Europe to Brasil"
        self.api_key = os.getenv("AWESOME_API_KEY")
        
        
    
    def get_all_quote(self):
        coins = f"{self.usd_brl_coin},{self.usd_eur_coin},{self.eur_brl_coin},{self.eur_usd_coin},{self.brl_usd_coin},{self.brl_eur_coin}"
        
        headers = {
            "x-api-key": self.api_key
        }

        response = requests.get(f"{self.base_url}/{coins}", headers=headers)
        
        if response.status_code == 200:
           return response.json()
        else:
            print(f"Error get quote: {response}")
            
            return {}