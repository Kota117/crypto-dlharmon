#!/usr/bin/env python

from bitcoin.rpc import RawProxy

url = None
port = 18332 # testnet, use None for main net client
conf = "/home/dlharmon/.bitcoin/bitcoin.conf"

proxy = RawProxy(url,port,conf)

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

info = proxy.gettransaction(txid)

print(info)
