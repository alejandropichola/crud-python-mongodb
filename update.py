from pymongo import MongoClient

client = MongoClient('localhost:27017')
myDb = client['test']
db = myDb.workers

def update():
    try:
        dataId = input("Ingrese id: ")
        firstName = input('Ingresar nombre: ')
        lastName = input('Ingresar apellido: ')
        age = int(input('Ingresar edad: '))

        db.update({"lastName": dataId},
                      {
                        "$set": {
                            "firstName": firstName,
                            "lastName": lastName,
                            "age": age
                        }
                      })
        print('\nActualizado correctamente\n')

    except ImportError:
        platform_specific_module = None
