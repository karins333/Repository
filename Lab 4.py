#Вариант4 Задание 1
from Bio import SeqIO


file1 = "Brassica_oleracea.gb"
file2 = "Solanum_lycopersicum.gb"
output_file = "combined_genbank.gb"


records = []
for file in [file1, file2]:
    with open(file, "r") as f:
        records.extend(list(SeqIO.parse(f, "genbank")))


with open(output_file, "w") as f:
    SeqIO.write(records, f, "genbank")

print(f"Файл {output_file} успешно создан, содержит {len(records)} записей.")
from Bio import SeqIO
for record in SeqIO.parse("combined_genbank.gb", "genbank"):
    print(f"ID: {record.id}, Описание: {record.description}")