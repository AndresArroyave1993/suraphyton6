#los diccionarios son variables especiales
#que me permiten almacenar multiples datos de difente tipo en una sola variable

empleado={
    'nombre':"juan",
    'cedula':101782828,
    'cargo':"Analista de datos",
    'salario':5700000,
    'horasTrabajadas':40,
    'aplicaSubsidioTransporte':False,
    'deuda':[1500000,80000]
}
#print(empleado)
#print(empleado['deuda'][1])

#recorriendo un diccionario:

for observadorAtributo,observadorValor in empleado.items():
    print(observadorAtributo)
    print(observadorValor)