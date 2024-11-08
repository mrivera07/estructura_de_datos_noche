#ejemplo con tuplas
lista=[]#lista vacia
lista1=[1,"Hola",4.5,"8"]#lista con 4 elementos
print(lista1)
print(lista1[1][2])#elemtnos dentro del indice  1
#listas enlazadas

lista2=[0,1,2,3]
lista3=["A","B","C"]
lista4=[lista2,lista3]
print(lista4)
print(lista4[1][2])

#operaciones con listas
lista5=["A","B","C"]
lista6=[1,2,3,4]
lista7=lista5+lista6
print(lista7)

#repetir
lista8=[1,2,3,4,5]
lista9=lista8*4
print(lista9)

#comparar
lista10=["Juan"]
lista11=["Juan "]
print(lista10==lista11)

#determinar si un elemento se encuentra dentro de la lista
lista12=["cien","años","de","soledad"]
if "de" in lista12:
    print("si esta en la lista")
else:
    print("no esta en la lista")

# Interando en una lista

lista13=["Hola","estudiantes","programacion"]
for palabra in lista13:
    print(palabra)

