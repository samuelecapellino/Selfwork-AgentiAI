import ollama

input_articolo = input("Incolla qui l'articolo di giornale da riassumere:\n> ")

print("\nGenerazione del riassunto lampo in corso...")


response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "system",
            "content": (
                "Sei un giornalista esperto di breaking news. "
                "Il tuo compito è riassumere l'articolo fornito dall'utente in un singolo paragrafo. "
                "ATTENZIONE: Il riassunto deve contenere tassativamente al massimo 255 caratteri (spazi inclusi). "
                "Sii estremamente conciso, elimina i dettagli superflui e vai dritto al punto. "
                "Non aggiungere saluti, introduzioni o commenti: rispondi solo con il riassunto."
            )
        },
        {
            "role": "user",
            "content": input_articolo
        }
    ]
)


riassunto = response['message']['content'].strip()
lunghezza = len(riassunto)

print("\n--- RIASSUNTO GENERATO (Llama 3) ---")
print(riassunto)
print(f"\nLunghezza effettiva: {lunghezza} caratteri (Limite massimo: 255)")