calificacion = int(input("Porporciona un valor entre 1 y 10: "))

if 0 < calificacion <= 6:
    print("F")
elif 6 < calificacion <= 7:
    print("D")
elif 7 < calificacion <= 8:
    print("C")
elif 8 < calificacion <= 9:
    print("B")
elif 9 < calificacion <= 10:
    print("A")
else:
    print("Calificación errónea")
