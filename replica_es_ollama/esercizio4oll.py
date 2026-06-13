import ollama
import json


dati_prodotto = {
    "prodotto": "Smartphone X100 Pro",
    "marca": "TechPhonix",
    "schermo": "6.7 pollici OLED 120Hz",
    "processore": "Snapdragon Gen 4",
    "batteria": "5000 mAh con ricarica rapida 80W",
    "fotocamera_principale": "108 Megapixel",
    "prezzo": "799 Euro"
}

print("Dati strutturati di partenza:")
print(json.dumps(dati_prodotto, indent=4, ensure_ascii=False))
print("\nTrasformazione dei dati in descrizione testuale in corso...")


response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "system",
            "content": (
                "Sei un copywriter e recensore esperto di tecnologia. "
                "Il tuo compito è prendere i dati strutturati (in formato JSON/Dizionario) forniti dall'utente "
                "e trasformarli in una descrizione testuale completa, fluida, leggibile e accattivante. "
                "Includi tutte le specifiche tecniche fornite nel testo, presentandole in modo naturale e professionale. "
                "Non inventare dati non presenti nel dizionario."
            )
        },
        {
            "role": "user",
            "content": json.dumps(dati_prodotto)  
        }
    ]
)

print("\n--- DESCRIZIONE TESTUALE COMPLETA ---")
print(response['message']['content'])