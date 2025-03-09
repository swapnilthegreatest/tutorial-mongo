DB_NAME = 'celebs'
COLLECTIONS = ['actors', 'movies']

ROWS = dict()
ROWS['actors'] = [
    { "_id": 1, 'actor_id': 1, 'name': "John Wick"},
    { "_id": 2, 'actor_id': 2, 'name': "Naruto"},
    { "_id": 3, 'actor_id': 3, 'name': "Sabrina"},
    { "_id": 4, 'actor_id': 4, 'name': "Mamta B."},
]

class CelebDB:
    def __init__(self, db_client):
        self.db_name = 'celebs'
        self.mongodb = db_client[self.db_name]
        self.actors = self.mongodb['actors']

    def createActor(self, actor_id, name):
        try:
            row = {'_id': actor_id, 'actor_id': actor_id, 'name': name}
            self.actors.insert_one(row)
        except Exception as err:
            print(err)

    def getActor(self, actor_id):
        myquery = {"actor_id": actor_id}
        try:
            rows = self.actors.find(myquery)
            for r in rows:
                print(r)
        except Exception as err:
            print(err)

    def insertMultipleActors(self):
        try:
            self.actors.insert_many(ROWS['actors'])
        except Exception as err:
            print(err)