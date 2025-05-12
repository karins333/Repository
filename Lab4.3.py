from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import os
def translate_cds(feature, parent_record):
    try:
        nt_seq = feature.extract(parent_record.seq)
        if feature.location.strand == -1:
            nt_seq = nt_seq.reverse_complement()
        protein_seq = nt_seq.translate(to_stop=True, cds=True)
        return str(protein_seq)
    except Exception as e:
        print(f"Ошибка при трансляции {parent_record.id}: {str(e)}")
        return None
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
        print(f"\n{record.id}: {record.description}")
        cds_features = [f for f in record.features if f.type == "CDS"]
        if not cds_features:
            print("Не найдено кодирующих последовательностей (CDS)")
            continue
        for feature in cds_features:
            location = feature.location
            strand = "+" if location.strand >= 0 else "-"
            print(f"Coding sequence location = [{location.start}:{location.end}]({strand})")
            protein_seq = translate_cds(feature, record)
            if protein_seq:
                print("Translation =")
                for i in range(0, len(protein_seq), 60):
                    print(protein_seq[i:i + 60])
            else:
                print("Ошибка трансляции")
if __name__ == "__main__":
    input_file = "combined_genbank.gb"
    main(input_file)
