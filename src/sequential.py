import string #ne da o lista cu toate semnele de punctuatie
import time #ne ajuta la masurarea timpului
from collections import Counter #este o unealta pentru  contorizare
import os #ne ajuta sa comunica cu sitemul de operare

def count_words_sequential(file_path):
    # Contor pentru cuvinte
    word_counts = Counter()
    
    # Verificare daca fisierul exista
    if not os.path.exists(file_path):
        print(f"Error: The file :{file_path} does not exist.")
        return None

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Eliminarea semnelor de punctuatie si scrierea  cu litere mici
            line = line.lower().translate(str.maketrans('', '', string.punctuation))
            #Taie randul in bucati oriunde gaseste spatiu.Rezultatul este o lista
            words = line.split()
            # Adaugarea cuvintelor in contor
            word_counts.update(words)
            
    return word_counts

if __name__ == "__main__":
    file_name = "../data/large_text.txt" 
    
    print(f"The sequential process will start for the file: {file_name}")
    
    start_time = time.time()
    counts = count_words_sequential(file_name)
    end_time = time.time()
    
    if counts:
        print(f"\nThe sequential process finished in {end_time - start_time:.4f} seconds.")
        print(f"The total number of distinct words found: {len(counts)}")
        print("\nThe 10 most common words are:")
        for word, freq in counts.most_common(10):
            print(f"{word}: {freq}")