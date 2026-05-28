import multiprocessing
import collections
import re
import os
import time

def clean_and_count(text_chunk):

    
    words = re.findall(r'\w+', text_chunk.lower())
    return collections.Counter(words)

def get_chunks(file_path, chunk_size=1024*1024):


    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            extra = f.readline()
            yield chunk + extra

def parallel_word_count(file_path):

    num_processes = multiprocessing.cpu_count()
    print(f"Utilizăm {num_processes} nuclee pentru procesare...")


    pool = multiprocessing.Pool(processes=num_processes)
    

    chunks = get_chunks(file_path)

    start_time = time.time()


    results = pool.map(clean_and_count, chunks)


    final_counter = collections.Counter()
    for partial_counter in results:
        final_counter.update(partial_counter)

  
    pool.close()
    pool.join()

    end_time = time.time()
    return final_counter, end_time - start_time

if __name__ == "__main__":
 
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_to_process = os.path.join(base_dir, "../../data/large_text.txt")

  
    if os.path.exists(file_to_process):
        final_counts, duration = parallel_word_count(file_to_process)
        
        print(f"Procesare finalizată în {duration:.4f} secunde.")
        print("Top 10 cele mai frecvente cuvinte:")
        for word, count in final_counts.most_common(10):
            print(f"{word}: {count}")
    else:
        print(f"Eroare: Fișierul '{file_to_process}' nu a fost găsit.")