import dask.bag as db
from dask.distributed import Client
import string
import time
import os

def curata_text(linie):
    
   
    if not linie or linie.isspace():
        return ""
    linie = linie.lower()
    tabel_punctuatie = str.maketrans('', '', string.punctuation)
    return linie.translate(tabel_punctuatie)

def proceseaza_cuvinte(cale_fisier):
    if not os.path.exists(cale_fisier):
        print(f"\n[EROARE] Fișierul nu a fost găsit la calea: {os.path.abspath(cale_fisier)}")
        print(f"[INFO] Folderul curent de lucru este: {os.getcwd()}")
        print(f"[INFO] Te rog verifică dacă fișierul este în folderul 'data'.")
        return

    
    client = Client(n_workers=4, threads_per_worker=2, memory_limit='2GB')
    print(f"\n>>> Dask este ACTIV.")
    print(f">>> Monitorizare Dashboard la: {client.dashboard_link}")

    print(f">>> Se analizează fișierul: {cale_fisier}...")
    
    start_time = time.time()

    try:
       
        bag = db.read_text(cale_fisier, blocksize="32MB", encoding='utf-8')

        
        frecvente = (
            bag.map(curata_text)       
                .str.split()           
                .flatten()              
                .frequencies()         
        )

        rezultat = frecvente.topk(20, key=1).compute()

        end_time = time.time()
        durata_totala = end_time - start_time

        print("\n" + "="*45)
        print(f"{'POZ':<4} | {'CUVÂNT':<20} | {'APARIȚII':<10}")
        print("-" * 45)
        for i, (cuvant, numar) in enumerate(rezultat, 1):
            print(f"{i:<4} | {cuvant:<20} | {numar:<10}")
        print("="*45)
        
        print(f"\n[SUCCES] Procesare terminată în {durata_totala:.4f} secunde.")

    except Exception as e:
        print(f"\n[EROARE CRITICĂ] A apărut o problemă: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":

    cale_reala = os.path.join("data", "date_mari.txt")
    
    
    proceseaza_cuvinte(cale_reala)