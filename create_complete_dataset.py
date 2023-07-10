import nltk
from nltk.corpus import wordnet as wn
import random
import pandas as pd
import tqdm

# Baixar o recurso do WordNet (caso ainda não tenha sido baixado)
#nltk.download('wordnet')

# Obter todas as synsets em WordNet
all_synsets = list(wn.all_synsets())

# Definir o número de iterações desejadas
num_iterations = len(all_synsets)

# Criar uma lista para armazenar os dataframes
dataframes = []

# Iniciar a iteração
for iteration in tqdm.tqdm(range(num_iterations), desc='Progress'):
    # Obter uma synset aleatória
    synset = all_synsets[iteration]

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
    
    # Obter todos os sinônimos da synset
    synonyms = synset.lemmas()
    synonyms_data = {
        'Definição Synset': [synset.definition() for _ in range(len(synonyms))],
        'ID Synset': [synset.name() for _ in range(len(synonyms))],
        'Definição Relacionada': [s.synset().definition() for s in synonyms],
        'ID Relacionada': [s.synset().name() for s in synonyms],
        'Relação': ['Synonyms' for _ in range(len(synonyms))]
    }
    synonyms_df = pd.DataFrame(synonyms_data)
    dataframes.append(synonyms_df)

# Concatenar todos os dataframes em um único dataframe
combined_df = pd.concat(dataframes)

# Salvar o dataframe em um arquivo CSV
combined_df.to_csv('all_synsets.csv', index=False)
