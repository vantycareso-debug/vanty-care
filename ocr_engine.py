# Vanty Care - Engine Backend & Leitor de Talões (OCR)
import json
from datetime import datetime

class VantyCareEngine:
    def __init__(self, country_code="PT"):
        self.country_code = country_code
        # Regras de Garantia por Legislação (Anos)
        self.warranty_rules = {
            "PT": 3,  # União Europeia (3 anos)
            "ES": 3,
            "FR": 2,
            "US": 1
        }

    def calculate_warranty_expiration(self, purchase_date_str):
        """Calcula automaticamente o fim da garantia com base no país do utilizador."""
        purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
        years_to_add = self.warranty_rules.get(self.country_code, 2)
        
        try:
            expiration_date = purchase_date.replace(year=purchase_date.year + years_to_add)
        except ValueError:
            expiration_date = purchase_date + (datetime(purchase_date.year + years_to_add, 1, 1) - datetime(purchase_date.year, 1, 1))
            
        return expiration_date.strftime("%Y-%m-%d")

    def process_receipt_data(self, store_name, product_name, price, purchase_date_str, serial_number=None):
        """
        Estrutura os dados extraídos do talão para inserção no Supabase.
        """
        fim_garantia = self.calculate_warranty_expiration(purchase_date_str)
        
        record = {
            "nome_produto": product_name,
            "loja": store_name,
            "data_compra": purchase_date_str,
            "fim_garantia": fim_garantia,
            "preco_com_iva": price,
            "numero_serie": serial_number or "N/A",
            "jurisdicao": self.country_code
        }
        
        print("--------------------------------------------------")
        print("✅ Talão Processado com Sucesso no Vanty Care Engine:")
        print(json.dumps(record, indent=4, ensure_ascii=False))
        print("--------------------------------------------------")
        return record

if __name__ == "__main__":
    # Teste local do motor do Vanty Care
    engine = VantyCareEngine(country_code="PT")
    engine.process_receipt_data(
        store_name="Worten",
        product_name="Máquina de Café Espresso",
        price=149.99,
        purchase_date_str="2026-08-17",
        serial_number="SN-WORTEN-9921"
    )
