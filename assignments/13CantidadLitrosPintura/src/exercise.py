def main():
    #escribe tu código abajo de esta línea
    a = (float(input("Area a pintar en metros: ")))
    r = (float(input("Rendimiento (m2/l): ")))
    c = (round(a/r))
    print("Litros a comprar:",c)

if __name__ == '__main__':
    main()
