#!/usr/bin/env python

# pip install requests

import requests
import json
import configparser
import pathlib
from pathlib import Path

def getConfig(file=None):
    if (file == None):
        file = str(pathlib.Path.home() / ".bitcoin" / "bitcoin.conf")

    fd = open(file,"r")
    data = fd.read()
    fd.close()

    config=configparser.ConfigParser()
    config.read_string(f"""
    [default]
    {data}
    """)

    return config['default']

config=getConfig()

testnet=int(config.get('testnet',0))
user=str(config.get('rpcuser',''))
password=str(config.get('rpcpassword',''))
port=int(config.get('port',8332 if not testnet else 18332))

url = f"http://localhost:{port}/"

# The below is the default transaction id that information will be gathered for
# This id comes from my initial recieved testcoin from a faucet
txid = "26a242fc975aae9ad07941a9c4cb3edd6d1c91f1a7ba5e6a297cf68c8e8b60a1"

# Any id may be used here so long as the transaction invloved my wallet
# Not all transaction id's are stored on my blockchain: only those that
# pertain to me
txidIn = input("Enter desired transaction id. Leave blank to use default id:")

#Checks to see if the user input was left blank
if (txidIn!=""):
    txid = txidIn

payload = {
    "version" : "1.1",
    "method": "gettransaction",
    "params": [txid],
    "id": 0,
}

response = requests.post(url, json=payload, auth=(user,password))
print(response.json())
