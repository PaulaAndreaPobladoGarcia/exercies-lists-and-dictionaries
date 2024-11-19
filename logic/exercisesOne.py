#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.
import json
def read_file():
    with open("databases/exercisesOneList.json", "r") as file:
        data = file.read()
        convertirList = json.loads(data)
        return convertirList

def write_file(data):
    with open("databases/exercisesOneList.json", "wb+") as file:
     convertirJson = json.dumps(data, indent=4).encode("utf-8")
     file.write(convertirJson)
     file.close()


def save_course(course):
    data = read_file()
    data.append(course)
    write_file(data)
    return data

#Escribir un programa que guarde en una variable el diccionario
#  `{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}`, pregunte al usuario 
# por una divisa y muestre su símbolo o un mensaje de aviso si 
# la divisa no está en el diccionario.
       
def search_currency(currency):
    data = read_file("exercisesOneDict.json")        
    if (data.get(currency)):
        return data.get(currency)
    else:
        return "Currency not found"