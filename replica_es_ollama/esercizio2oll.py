import ollama

input_biografia = input("Inserisci un testo descrittivo su una persona:\n> ")

print("\nEstrazione dei dettagli chiave in corso con Llama 3...")


response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "system",
            "content": (
                "Sei un assistente specializzato nell'analisi del testo e nell'estrazione di informazioni. "
                "Il tuo compito è leggere il testo fornito dall'utente ed estrarre ESCLUSIVAMENTE questi tre dettagli: "
                "Nome, Età e Professione. "
                "Formatta la risposta esattamente in questo modo, usando un elenco puntato:\n"
                "- Nome: [Nome estratto]\n"
                "- Età: [Età estratta o 'Non specificata']\n"
                "- Professione: [Professione estratta o 'Non specificata']\n"
                "Non aggiungere introduzioni, saluti o commenti extra. Rispondi solo con l'elenco dei dati."
            )
        },
        {
            "role": "user",
            "content": input_biografia
        }
    ]
)


print("\n--- DETTAGLI CHIAVE ESTRATTI ---")
print(response['message']['content'])