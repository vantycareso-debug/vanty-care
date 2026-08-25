# VANTY CARE — Análises e roadmap (guardado 2026-08-25)

## Visão de produto
**VANTY = Intelligence Layer for Products** (não “app de garantias”).
Missão: tornar transparente o que acontece aos produtos depois de serem vendidos.

Camadas: BUY · OWN · CARE · REPAIR · VALUE · TRADE · PASS ON · RECYCLE · LEARN

## Posicionamento de mercado
- Não competir com DPP oficial da UE → ser a **camada consumer** por cima.
- Moat: Product Graph real (compra → avaria → reparação → venda → fim de vida) + reviews verificadas por fatura.
- Concorrentes parciais: Omora, Certico, LoopOS (B2B), apps de warranty, OLX (sem histórico).
- Combinação consumer completa ainda rara.

## O que já existe (base v4.10)
- Carteira, OCR fatura, cartões loja
- Reviews verificadas + filtros geo
- RMA / assistência + contactos marca
- Passaporte, transferência, mercado + ofertas/chat
- Intelligence A (score, DNA, life curve, decision)
- Trust B (passport, verified, brand score, patterns, seller trust)
- Care Engine (confidence, EOL motivo, Ask Vanty, triagem problema)
- Watch / match com consentimento
- PWA + push local
- Identidade visual gunmetal + laranja

## Análises — o que falta para profissionalismo

### P0 — Parece produto, não demo
1. Onboarding curto (30s)
2. Empty states bons
3. Erros legíveis + loadings
4. Confidence + metodologia em scores públicos
5. Nav simplificada (Home · World · Market · Care · Perfil)
6. GDPR na UI (exportar / apagar conta)

### P1 — Fechar ciclos
7. Email RMA em produção (domínio próprio)
8. Sync cloud mercado / intents / matches
9. Push remoto (VAPID + Edge Function)

### P2 — Escala
10. Rankings só com N mínimo + metodologia
11. Brand Warranty Experience (tempos RMA)
12. Modularizar monolito HTML

### Evitar agora
- Feature explosion de AI
- Trade chains multi-user
- Números de escala fictícios
- Redesign de identidade do zero
- DPP concorrente à UE

## Princípios de dados
- Sempre mostrar **Data Confidence** (Alta / Média / Baixa / Insuficiente + N)
- “Padrão observado” ≠ “defeito de fabrico”
- Heurística de valuation ≠ cotação de mercado
- Reviews públicas só com compra verificada

## Brand / UI (referência)
- Fundo: #050608 · painéis #0D1116 · gunmetal #1A2026
- Laranja VANTY: #FF5A00 · luminoso #FF7A00 · profundo #C93400
- Logo = armadura; dashboard = interior da armadura
- Border-radius 8–12px; sem excesso de azul SaaS
- Verde = verificado; âmbar = atenção; violeta = Trade/Match

## Fases de inteligência (histórico de decisão)
- Update A: Health, DNA, Life curve, Keep/Sell/Repair
- Update B: Passport, Verified, Brand, Trust vendedor, long-term, patterns
- Update C (pendente): rankings, House Intelligence completa, Ask Vanty orquestrador total, Trade Engine cloud

## Push
- Local: ativo (SW + Notification API)
- Remoto: VAPID + supabase_push_subscriptions.sql + Edge Function

## Contacto sistema (dev)
- Email testes assistência: vantycareso@gmail.com (alterar quando produção)

---
Documento vivo: atualizar após cada release maior.


## Rebrand 2026-08-25 — VANTY (V.A.N.T.Y.)
- Nome: **VANTY** = Verified · Asset · Network · Trust · Yield
- Logo novo: V metálico + globo + arcos azul/laranja
- UI: Home / My World / Intelligence / Marketplace / Care
- Cores: laranja CTA + azul rede (moderado)
- v5.0
