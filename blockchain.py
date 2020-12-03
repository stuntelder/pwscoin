from time import time
import json
import hashlib

class Blockchain (object):
    def __init__(self):
        self.chain = [];

class Block (object):
    def __init__(self, transactions, time, index):
        self.index = index; #'naam' van het block
        self.transactions = transactions; 
        self.time = time;
        self.prev = ''; #hash van het vorige block
        self.hash = self.calculateHash(); #hash van het block

    def calculateHash(self):
        hashTransactions = "";
        for transaction in self.transactions:
            hashTransactions += transaction.hash;

        hashString = str(self.time) + hashTransactions + self.prev + str(self.index);
        return hashlib.sha256(hashEncoded).hexdigest();

class Transaction (object):
    def __init__(self, sender, reciever, amt):
        self.sender = sender;
        self.reciever = reciever
        self.amt = amt;
        self.hash = self.calculateHash();

    def calculateHash(self):
        hashString = self.sender + self.reciever + str(self.amt) + str(self.time);