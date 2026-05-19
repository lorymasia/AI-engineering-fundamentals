"""
AI Engineering Fundamentals — Lezione 1
Esercizio 4 (Deliverable) — Chatbot personalizzato

TODO: Completa questo script in modo che:
1. Chieda il nome utente con input()
2. Usi il nome nel messaggio a Claude
3. Stampi la risposta in modo formattato

Poi pusha questo file su GitHub!
"""

import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

# 1. Chiedi il nome
nome = input("Come ti chiami? ")

# 2. TODO: crea il messaggio usando il nome
messaggio = f"Ciao {nome}"

# 3. TODO: chiama l'API
risposta = chiedi_claude(domanda_test, system=system_rima)

# 4. TODO: stampa la risposta in modo carino
print(messaggio)
print(risposta)
