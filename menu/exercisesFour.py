from logic.exercisesFour import save_ganadores, search_fecha


def designFourList():
    ganadores = input("cuales son los numeros ganadores de la loteria? ")
    result = save_ganadores(ganadores)
    print (result)

def designFourDist():
    fecha = input("cuales es la fecha que quieres ingresar? ")
    prin (search_fecha(fecha))
    
