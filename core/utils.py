import random

from DB import DB


#COUNT = "count"
SIZE = "size"
FROM = "from"
TO = "to"

def pageLimit(n):
    return int((round(n, 49) / 49) + 1)


def round(n, m):
    r = n % m
    return n + m - r if r + r >= m else n - r


def ranker(database, top):  # db {from : {to : addr, count:n}} # BROKEN, FIX LATER
    newDatabase = []
    print("oldDB: ", database)
    for node in database:
        print("node: ", node)
        newDatabase.append(node)
        #newDatabase[node] = {"x": 0}
        topSize = [0 for i in range(top)]
        topAdd = ["" for i in range(top)]
        
        if node[SIZE] > minimum:
            index = topSize.index(minimum)
            # ...
        for to in list(database[node].keys()):
            minimum = min(topSize)
            print("a: ", to)
            if database[node][to] > minimum:
                index = topSize.index(minimum)
                topSize[index] = database[node]
                topAdd[index] = to
        for size, address in zip(topSize, topAdd):
            newDatabase[node][address] = size
        print("newDB: ", newDatabase)

    return newDatabase


def genLocation():
    x, y = random.randint(1, 800), random.randint(1, 500)
    x, y = random.choice([x, x * -1]), random.choice([y, y * -1])
    return x, y


def getNewAddresses(database: list, processed):
    new = []
    
    txn:DB 
    for txn in database:
        if txn.from_ not in processed:
            
            print("newAddr: ", txn.from_)
            new.append(txn.from_)
        
    return new # no need to check for null 
    #return set(filter(None, new))
