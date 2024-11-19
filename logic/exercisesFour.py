#Escribir un programa que pregunte una fecha en formato `dd/mm/aaaa`
#  y muestre por pantalla la misma fecha en formato `dd de <mes> de aaaa`
#  donde `<mes>` es el nombre del mes.
import json
def read_file():
    with open ("databases/exercisesFourList.Json", "r") as file:
       data = file.read()
       convertirList = json.loads(data)
       return convertirList

def write_file(data):
    with open("databases/exercisesFourList.json", "wb+") as file:
        convertirJson = json.dumps(data, indent=3).encode(utf-6)
        file.write(convertirJson)
        file.close()




