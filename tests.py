import pandas as pd
from nltk.corpus import wordnet as wn

def check_hyponyms():
    csv_file = 'all_synsets.csv'
    combined_df = pd.read_csv(csv_file)

    # Get all unique system names
    unique_synset = set(combined_df['ID Synset'])

    # Check if all synset with hyponyms are included
    all_hyponym_synset = set(wn.synset(sys.name()).name() for sys in wn.all_synsets() if sys.hyponyms())
    missing_synset = all_hyponym_synset - unique_synset

    if missing_synset:
        print("The following synset are missing from the CSV:")
        for sys in missing_synset:
            print(sys)
    else:
        print("All synsets with hyponyms are included in the CSV.")

def check_hypernyms():
    csv_file = 'all_synsets.csv'
    combined_df = pd.read_csv(csv_file)

    # Get all unique system names
    unique_synset = set(combined_df['ID Synset'])

    # Check if all synset with hypernyms are included
    all_hypernym_synset = set(wn.synset(sys.name()).name() for sys in wn.all_synsets() if sys.hypernyms())
    missing_synset = all_hypernym_synset - unique_synset

    if missing_synset:
        print("The following synset are missing from the CSV:")
        for sys in missing_synset:
            print(sys)
    else:
        print("All synsets with hypernyms are included in the CSV.")

def check_synonyms():
    csv_file = 'all_synsets.csv'
    combined_df = pd.read_csv(csv_file)

    # Get all unique system names
    unique_synset = set(combined_df['ID Synset'])

    # Check if all synset with synonyms are included
    all_synonym_synset = set(wn.synset(sys.name()).name() for sys in wn.all_synsets() if sys.lemmas())
    missing_synset = all_synonym_synset - unique_synset

    if missing_synset:
        print("The following synset are missing from the CSV:")
        for sys in missing_synset:
            print(sys)
    else:
        print("All synsets with synonyms are included in the CSV.")

if __name__ == '__main__':
    check_hyponyms()
    check_hypernyms()
    check_synonyms()
