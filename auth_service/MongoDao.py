from pymongo import MongoClient
import hashlib, random
import os

class MongoDao:

    def __init__(self, connectString=None):
        self._connectionstring = connectString or os.environ['MONGODB']
        self._client = None

    def get_connection(self):
        if self._client != None:
            return self
        self._client = self.__connect(self._connectionstring);
        self._auth_db = self._client.auth;
        self._users = self._auth_db.users;
        self._tokens = self._auth_db.tokens;
        return self

    def __connect(self, connectString):
        try:
            print("connecting...");
            conn = MongoClient(connectString, connectTimeoutMS=5000);
            print("connected...");
            return conn;
        except:
            print("Could not connect to database.");
            raise

    def authenticateClient(self, key, secret):
        try:
            user = self._users.find_one({'key': key, 'secret': secret});
            return self.__createToken(user) if user else False;
        except:
            print("Failed to get accounts.");
            raise

    def __createToken(self, user):
        token = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest();
        print(token)
        id = self._tokens.insert_one({"userid": user['_id'], "token": token});
        if id:
            return token;
        else:
            raise Exception("Gah. Couldnt create the record!");
