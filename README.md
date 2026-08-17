# 🛡️ Vanty Care - Global Warranty Management System

O **Vanty Care** é uma plataforma inteligente concebida para centralizar, gerir e automatizar garantias de produtos e pedidos de assistência técnica (RMA) à escala global.

---

## 🚀 Arquitetura do Projeto

* **Frontend (`index.html`):** Interface do utilizador em HTML5 e Tailwind CSS com visão da "Casa do Cliente", painel de controlo de garantias e formulário de registo.
* **Backend Engine (`ocr_engine.py`):** Motor em Python para cálculo automático de caducidade de garantia com base na legislação do país (ex: 3 anos UE) e estruturação de dados de faturas.
* **Base de Dados (Supabase / PostgreSQL):** Estrutura relacional separada entre catálogo global (marcas e centros de assistência técnica/CATs) e inventário individual do cliente.

---

## 🛠️ Como Executar
1. **Ver a Aplicação Web:** Acede ao link disponibilizado via GitHub Pages.
2. **Executar o Backend Python:**
   ```bash
   python ocr_engine.py
