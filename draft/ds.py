import nltk
from nltk.corpus import wordnet as wn
import random
import pandas as pd

# Baixar o recurso do WordNet (caso ainda não tenha sido baixado)
nltk.download('wordnet')

# Definir o número de iterações desejadas
num_iterations = 1000

# Criar uma lista para armazenar os dataframes
dataframes = []

# Iniciar a iteração
for iteration in range(num_iterations):
    # Obter uma synset aleatória
    synset = random.choice(list(wn.all_synsets()))
    
    # Obter todos os hiperônimos da synset
    hypernyms = synset.hypernyms()
    hypernyms_data = {
        'Definição Synset': [synset.definition() for _ in range(len(hypernyms))],
        'ID Synset': [synset.name() for _ in range(len(hypernyms))],
        'Definição Relacionada': [h.definition() for h in hypernyms],
        'ID Relacionada': [h.name() for h in hypernyms],
        'Relação': ['Hypernyms' for _ in range(len(hypernyms))]
    }
    hypernyms_df = pd.DataFrame(hypernyms_data)
    dataframes.append(hypernyms_df)
    
    # Obter todos os hipônimos da synset
    hyponyms = synset.hyponyms()
    hyponyms_data = {
        'Definição Synset': [synset.definition() for _ in range(len(hyponyms))],
        'ID Synset': [synset.name() for _ in range(len(hyponyms))],
        'Definição Relacionada': [h.definition() for h in hyponyms],
        'ID Relacionada': [h.name() for h in hyponyms],
        'Relação': ['Hyponyms' for _ in range(len(hyponyms))]
    }
    hyponyms_df = pd.DataFrame(hyponyms_data)
    dataframes.append(hyponyms_df)

# Concatenar todos os dataframes em um único dataframe
combined_df = pd.concat(dataframes)

# Salvar o dataframe em um arquivo CSV
combined_df.to_csv('synsets.csv', index=False)
