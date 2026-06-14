import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
from chromadb.utils import embedding_functions


load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    print("Errore: OPENAI_API_KEY non trovata nel file .env!")
    exit()


client = OpenAI(api_key=openai_key)


def estrai_info_con_openai(testo):
    prompt = f"""Estrai le seguenti informazioni dal testo:
- nome completo
- email
- numero di telefono

Restituisci solo un dizionario JSON nel formato:
{{"nome": "...", "email": "...", "phone": "..."}}

Testo: {testo}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content


documents_dir = "resumes"
documents = []
metadatas = []
ids = []
id_counter = 0

print("Fase 1: Lettura dei curricula ed estrazione dei metadati...")

for filename in os.listdir(documents_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(documents_dir, filename), 'r', encoding='utf-8') as file:
            
            chunks = file.read().replace('\n', '.').split('### ')
            
            info_candidato = estrai_info_con_openai(chunks[1])
            
            for chunk in chunks:
                if chunk.strip() != "":
                    documents.append(chunk)
                    metadatas.append({"source": filename, "info": info_candidato})
                    ids.append(str(id_counter))
                    id_counter += 1


print("\nFase 2: Creazione del Database Vettoriale su ChromaDB...")

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=openai_key,
    model_name="text-embedding-3-small"
)

chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(
    name="CVs",
    embedding_function=openai_ef
)


collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)


print("\nFase 3: Esecuzione della query semantica...")
user_question = "mi serve qualcuno per promuovere il mio prodotto"

results = collection.query(
    query_texts=[user_question],
    n_results=1
)


doc_recuperato = results['documents'][0][0]
source_recuperata = results['metadatas'][0][0]['source']
info_recuperata = results['metadatas'][0][0]['info']

context = f"CONTESTO: nome file {source_recuperata} ecco il paragrafo piu' significativo: {doc_recuperato} ricorda sempre di menzionare il candidato all'inizio e i dati personali alla fine per il contatto, ti lascio tutto qui: {info_recuperata}"

prompt = f"""Dato il seguente contesto {context} rispondi alla domanda dell'utente {user_question} 
spiegando che nel file individuato c'e' il profilo piu' adatto. 
Argomenta la scelta utilizzando il contenuto del testo individuato nel contesto
"""


print("\nFase 4: Generazione della risposta finale con OpenAI...")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Sei un assistente HR, specializzato nella ricerca di profili professionali"
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n--- RISPOSTA FINALE GENERATA ---")
print(completion.choices[0].message.content)