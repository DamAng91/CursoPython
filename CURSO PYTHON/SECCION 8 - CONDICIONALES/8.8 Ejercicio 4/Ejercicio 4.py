voto = input("Ingrese su voto: ")

if voto.upper() == "A":
    print("Ud. ha votado al candidato {} del partido rojo".format(voto.upper()))
elif voto.upper() == "B":
    print("Ud. ha votado al candidato {} del partido verde".format(voto.upper()))
elif voto.upper() == "C":
    print("Ud. ha votado al candidato {} del partido azul".format(voto.upper()))
else:
    print("Opcion erronea")




    