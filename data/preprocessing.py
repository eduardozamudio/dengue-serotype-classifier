import re
datos=""
linea=""
l=[]
x=0
datos=open("/home/sergiolitwiniuk/Documentos/clasificador_dengue/dengue-serotype-classifier/data/all_den_proteinE.fasta","r")
salida = open("/home/sergiolitwiniuk/Documentos/clasificador_dengue/dengue-serotype-classifier/data/salida_proteinE.fasta","w")
headers= open("/home/sergiolitwiniuk/Documentos/clasificador_dengue/dengue-serotype-classifier/data/headers_proteinE.fasta","w")
for i in datos:
    if not re.match('>', i):
        i.replace("\n","")
        linea = linea + i
    else:
        print(linea+"\n")
        salida.write(linea + "\n")
        headers.write(i)
        linea = ""
