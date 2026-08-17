# Vanty Care - Engine Backend, OCR & Supabase Integration
import json
import urllib.request
from datetime import datetime

SUPABASE_URL = "https://dhhqrjopwvtxzgfyjdrc.supabase.co"
SUPABASE_KEY = "sb_publishable_Hplq0WcOKp6kM_tN7Kx8Rw_b4lLqYFd"

class VantyCareEngine:
    def __init__(self, country_code="PT"):
        self.country_code = country_code
        self.warranty_rules = {
            "PT": 3,
            "ES": 3,
            "FR": 2,
            "US": 1
        }

    def calculate_warranty_expiration(self, purchase_date_str):
        purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
        years_to_add = self.warranty_rules.get(self.country_code, 2)
        try:
            expiration_date = purchase_date.replace(year=purchase_date.year + years_to_add)
        except ValueError:
            expiration_date = purchase_date + (datetime(purchase_date.year + years_to_add, 1, 1) - datetime(purchase_date.year, 1, 1))
        return expiration_date.strftime("%Y-%m-%d")

    def save_to_supabase(self, record):
        """Envia os dados diretamente para a tabela 'produtos_garantias' via REST API."""
        endpoint = f"{SUPABASE_URL}/rest/v1/produtos_garantias"
        payload = json.dumps([record]).encode('utf-8')
        
        req = urllib.request.Request(
            endpoint,
            data=payload,
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json",
                "Prefer": "return=minimal"
            },
            method="POST"
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                print(f"✅ Produto guardado com sucesso no Supabase! Status: {response.status}")
                return True
        except Exception as e:
            print(f"❌ Erro ao comunicar com o Supabase: {e}")
            return False

    def process_and_save_receipt(self, store_name, product_name, price, purchase_date_str, serial_number=None):
        fim_garantia = self.calculate_warranty_expiration(purchase_date_str)
        
        record = {
            "nome_produto": product_name,
            "loja": store_name,
            "data_compra": purchase_date_str,
            "fim_garantia": fim_garantia,
            "preco_com_iva": price,
            "numero_serie": serial_number or "N/A"
        }
        
        print("--------------------------------------------------")
        print("📄 Processando dados do talão:")
        print(json.dumps(record, indent=4, ensure_ascii=False))
        print("--------------------------------------------------")
        
        return self.save_to_supabase(record)

if __name__ == "__main__":
    engine = VantyCareEngine(country_code="PT")
    engine.process_and_save_receipt(
        store_name="Fnac",
        product_name="Auscultadores Bluetooth Sony",
        price=299.00,
        purchase_date_str="2026-08-17",
        serial_number="SN-SONY-9912"
    )
