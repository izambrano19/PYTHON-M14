import Bio
from Bio.Seq import Seq
from Bio import SeqIO

def trencaid(identificador): #Definir funciones en python - def + nombredelafunción
    ##gi | 2765658 | emb | Z78533.1 | CIZ78533
    resultado = identificador.split("|")
    return resultado[3]


diccionari = {}
diccionari["hola"] = "salutació"

for i in SeqIO.parse("ls_orchid.fasta","fasta"):
    #print("id " + i.id)
    valor = trencaid(i.id) #en valor solo quiero una parte del id
    #print(valor)
    diccionari[valor] = i.seq[:200] #Si pones : antes de 200, pilla las primeras 200 letras
    #print("descripcio " + i.description)
    #print("nom " + i.name)
    #print(i.seq)
    #print(len(i))
    #print("---------------")

#print(diccionari.keys())
#print(diccionari.values())
#print(diccionari["hola"])
#print(diccionari["Z78533.1"])

def alinea(cadena1,cadena2):

    return

claus = diccionari.keys()

for i in range(len(claus)):#Desde i hasta la longitud del vector de claus
    for j in range(i+1,len(claus)):#Hacemos un segundo bucle que comienza uno más a la derecha, que va contando de 1 en 1 según la longitud de i.
        alinea(claus[i],claus[j])
