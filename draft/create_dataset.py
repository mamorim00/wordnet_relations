import csv
from nltk.corpus import wordnet as wn
import random

# Randomly select synsets
all_synsets = list(wn.all_synsets())
random_synsets = random.sample(all_synsets, 10)

# Obtain the synset names
synset_names = [synset.name() for synset in random_synsets]

# List of possible relationships
relationships = ['hyponyms', 'hypernyms', 'related']

# Generate synset pairs with random relationships
synset_pairs = []
for synset1 in synset_names:
    for synset2 in synset_names:
        if synset1 != synset2:
            relationship = random.choice(relationships)
            synset_pairs.append((synset1, synset2, relationship))

# Open a CSV file for writing
with open('wordnet_dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Synset 1', 'Synset 2', 'Relationship'])

    # Write synset pairs and relationships to the CSV file
    for synset1, synset2, relationship in synset_pairs:
        synset1_definition = wn.synset(synset1).definition()
        synset2_definition = wn.synset(synset2).definition()
        writer.writerow([synset1_definition, synset2_definition, relationship])
