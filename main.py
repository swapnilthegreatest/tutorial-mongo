import pymongo
from Database.Celebs import CelebDB

#main file.
#play around with me in your brain cells.

if __name__ == '__main__':
    mongo_db = pymongo.MongoClient("mongodb://localhost:27017/")
    celeb_db = CelebDB(mongo_db)

    try:
        celeb_db.insertMultipleActors()
        celeb_db.createActor(6, 'Bajirao')
    except Exception as err:
        print(err)

    try:
        celeb_db.createActor(7, 'Ganpati')
    except Exception as err:
        print(err)

    print("----------------------------------------------------")
    celeb_db.getActor(6)

