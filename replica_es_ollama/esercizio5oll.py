import ollama


input_testo = input("Inserisci il breve testo su cui vuoi generare le domande di comprensione:\n> ")

print("\nGenerazione delle domande di comprensione in corso con Llama 3...")

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "system",
            "content": (
                "Sei un assistente didattico esperto nella creazione di materiali educativi. "
                "Il tuo compito è leggere il testo fornito dall'utente e generare esattamente 3 domande di comprensione. "
                "Le domande devono basarsi esclusivamente sulle informazioni presenti nel testo e servono a verificare "
                "se lo studente ha capito bene i punti chiave. "
                "Fornisci una formattazione pulita, numerata (1, 2, 3) e non aggiungere risposte o commenti extra."
            )
        },
        {
            "role": "user",
            "content": input_testo
        }
    ]
)

print("\n--- DOMANDE DI COMPRENSIONE GENERATE ---")
print(response['message']['content'])