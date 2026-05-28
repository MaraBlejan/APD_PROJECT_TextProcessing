
nume_fisier = "date_mari.txt"
continut = "Acesta este un proiect de procesare paralela a textului folosind framework-ul Dask in Python.\n"

print(f"Se genereaza fisierul {nume_fisier}...")

with open(nume_fisier, "w", encoding="utf-8") as f:

    for i in range(1000000):
        f.write(f"{i} {continut}")

print(f"Gata! Fisierul {nume_fisier} a fost creat cu succes.")