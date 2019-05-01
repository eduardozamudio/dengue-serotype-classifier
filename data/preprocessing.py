import re
datos=""
linea=""
l=[]
x=0
datos=open("all_den_proteinE.fasta","r")
salida = open("salida_proteinE.fasta","w")
headers= open("headers_proteinE.fasta","w")
for i in datos:
    if not re.match('>', i):
        i.replace("\n","")
        linea = linea + i
    else:
        print(linea+"\n")
        salida.write(linea + "\n")
        headers.write(i)
        linea = ""
