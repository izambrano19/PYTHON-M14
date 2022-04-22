import Bio
from Bio.Seq import Seq
from Bio import SeqIO

for i in SeqIO.parse("ls_orchid.fasta","fasta"):
    print("id " + i.id)
    print("descripcio " + i.description)
    print("nom " + i.name)
    print(i.seq)
    print(len(i))
    print("---------------")

