from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import os
def calculate_gc_content(record):
    try:
        return gc_fraction(record.seq)
    except Exception as e:
        print(f"Ошибка при расчете GC для {record.id}: {str(e)}")
        return 0.0
def main(input_file):
    if not os.path.exists(input_file):
        print(f"Файл {input_file} не найден!")
        return
    try:
        records = list(SeqIO.parse(input_file, "genbank"))
    except Exception as e:
        print(f"Ошибка при чтении файла: {str(e)}")
        return
    for record in records:
        record.gc_content = calculate_gc_content(record)
    sorted_records = sorted(records, key=lambda x: x.gc_content)
    for record in sorted_records:
        print(f"{record.id}: {record.description}, GC = {record.gc_content:.4f}")
if __name__ == "__main__":
    input_file = "combined_genbank.gb"
    main(input_file)


