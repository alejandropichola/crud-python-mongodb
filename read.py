from pymongo import MongoClient

client = MongoClient('localhost:27017')
myDb = client['test']
db = myDb.workers

def read():
  try:
    colData = db.find()
    print('\n all data from workers database \n')
    for col in colData:
      print(col)

  except ImportError:
    platform_specific_module = None
    # print str(e)