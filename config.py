from pymongo import MongoClient
import certifi




MONGO_URI = 'mongodb+srv://freshmania:freshmania123@cluster0.z4t3nel.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()


def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile = ca)
        db = client["db_produtos_app"]
    except ConnectionError:
        print('Erro de conexão com base de dados.')
    return db
