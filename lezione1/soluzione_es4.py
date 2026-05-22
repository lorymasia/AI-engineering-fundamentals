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

def chiedi_claude(domanda, temperature=0.7, system=None, max_tokens=300):
    """Invia una domanda a Claude e restituisce la risposta testuale."""
    params = {
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [{"role": "user", "content": domanda}]
    }
    if system:
        params["system"] = system

    response = client.messages.create(**params)
    return response.content[0].text

# 1. Chiedi il nome
nome = input("Come ti chiami? ")

# 2. TODO: crea il messaggio usando il nome
messaggio = f"Ciao {nome}"  # ← usa f-string con la variabile nome

# 3. TODO: chiama l'API
domanda_test = 'Ciao chi sei?'
system_prompt= 'Sei un assistente python esperto'
risposta = chiedi_claude(domanda_test, system=system_prompt)

# 4. TODO: stampa la risposta in modo carino
print(messaggio)
print(risposta)


