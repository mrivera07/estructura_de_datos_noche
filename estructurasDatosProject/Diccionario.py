#ejemplo con diccionario

diccionario ={}#diccionario vacio
puertos={
    22:"SSH",
    23:"TELNET",
    80:"HTTPS",
    3301:"MySQL",
    1526:"ORACLE",

}
print(puertos[22])
puertos1={
    22:"SSH",
    80:"Http"
}

puertos2={
    53:"DNS",
    443:"Https",
}
print(puertos1)
puertos1.update(puertos2)#actualizar el diccionario
print(puertos1)
#eliminar un elemento de direccionamiento
calificaciones={
    "Alumno1":5,
    "Alumno2":4,
    "Alumno3":3,
    "Alumno4":2,
}
print(calificaciones)
del calificaciones["Alumno3"]
print(calificaciones)
#interar en un diccionario
dicPuerto={
    22:"ssh",
    23:"telnet",
    80:"http",
}
for x,y in dicPuerto.items():
    print(x,"->",y )