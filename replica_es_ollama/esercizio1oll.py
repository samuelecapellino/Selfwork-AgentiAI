import ollama

# 1. Chiediamo all'utente la frase in italiano da tradurre
input_text = input("Inserisci la frase in italiano da tradurre in inglese: ")

# 2. Utilizziamo il metodo nativo ollama.chat con Llama 3
response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "system",
            "content": (
                "Sei un traduttore automatico professionale. "
                "Il tuo compito è tradurre la frase dell'utente dall'italiano all'inglese. "
                "Fornisci come risposta ESCLUSIVAMENTE la traduzione in inglese, "
                "senza aggiungere commenti, spiegazioni o saluti."
            )
        },
        {
            "role": "user",
            "content": input_text
        }
    ]
)

# 3. Estraiamo e stampiamo il contenuto della risposta dal dizionario di Ollama
print("\n--- TRADUZIONE DA OLLAMA (Llama 3) ---")
print(response['message']['content'])