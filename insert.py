import pymongo

client = pymongo.MongoClient('localhost:27017')
mydb = client['test']
db = mydb['workers']

def insert():
    try:
        firstName = input('Ingresa nombre')
        lastName = input('Ingresa apellido')
        age = int(input('Ingrese edad'))
        db.insert_one({
            'firstName': firstName,
            'lastName': lastName,
            'age': age
        })
        print('dato insertado correctamente')

    except ImportError:
        platform_specific_module = None
        # print str(e)
