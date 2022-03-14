import pymongo
from pymongo import MongoClient
import certifi
from web3 import Web3
from dotenv import load_dotenv
load_dotenv()
import os

# Connect to MongoDB
database_password = os.environ.get('DBPW')
print(database_password)
def upload_to_db(id,email,address,ip):

    # Connection info
    cluster = MongoClient(f"mongodb+srv://titanmaker:{database_password}@cluster0.fdym1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=certifi.where())
    db = cluster['titanmaker']
    collection = db['ticket_users']

    # Search for record
    search_email = collection.find_one({"email":email})
    search_ip = collection.find_one({"ip":ip})
    search_cro = collection.find_one({"cro_address":address})

    if search_email != None or search_cro!= None or search_ip != None:
        print('Already exists!')
        return False

    elif Web3.isAddress(address) == False:
        print('Not a web3 address')
        return False

    else:
        post = {
            "_id":id,
            "email":email,
            "cro_address":address,
            "ip":ip
        }
        collection.insert_one(post)

        print('record added!')
        return True
