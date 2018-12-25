from pymongo import MongoClient

client = MongoClient('localhost:27017')
myDb = client['test']
db = myDb.workers

def delete():
    try:
        idDelete = input("ingrese id del objeto a eliminar: ")
        db.delete_many({'firstName': idDelete})
        print('\nEliminado correctamente\n')

    except ImportError:
        platform_specific_module = None
        # print str(e)
