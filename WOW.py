Diccionario = {"XD":"es una forma de expresar algo grasioso",
    "bro":"es una forma la cual se expresan entre amigos ",
    "lol":"es una forma de expresar algo grasioso pero casi siempre lo ocupan los de America",
    "papu":"es una manera de llamar a una persona de parte de la grasa xd",
    "mamu":"es la contra parte de papu osea en femenino"
}

while True:
    palabra = input("que escogeras xd")
    if palabra in diccionario.keys():
        print(diccionario[palabra])
    else:
        print("wacho eso no esta deja le chambeo y la pongo xd")
