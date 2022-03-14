import json
from web3 import Web3

def database(submit_id,email,cro_address,ip_address):
    # Load JSON file
    filename = 'db.json'
    with open(filename,"r") as db:
        data=json.load(db)

    #Check if record exists
    if email in data.__str__() or cro_address in data.__str__() or ip_address in data.__str__():
        print('exists')
        return False

    #Check if Web3 address is valid
    elif Web3.isAddress(cro_address):
        print('valid address')

        #Update JSON File
        data.append({
            "id":submit_id,
            "email":email,
            "cro_address":cro_address,
            "ip_address":ip_address
            })

        with open(filename,mode="w") as db:
            json.dump(data,db)
        return True

    else:
        print('invalid address')
        return False