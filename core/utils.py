import random

from DB import DB

from core.globalVars import FROM
from core.colors import red, info


def pageLimit(n):
    return int((round(n, 49) / 49) + 1)


def round(n, m):
    r = n % m
    return n + m - r if r + r >= m else n - r


def ranker(database, top):
    newDatabase = []
    sizes = []
    tx: DB
    for tx in database:
        tx.size = getSize(database, getattr(tx, FROM), FROM)
        sizes.append(tx.size)
    index = 0
    while max(sizes) != -1 and index != top:
        maximum = sizes.index(max(sizes))
        sizes[maximum] = -1
        newDatabase.append(database[maximum])
        index += 1
    cmp = len(database) - len(newDatabase)
    print("%sConnections Ignored: %s" % (red if cmp else info + " ", cmp))
    return newDatabase

def genLocation():
    x, y = random.randint(1, 800), random.randint(1, 500)
    x, y = random.choice([x, x * -1]), random.choice([y, y * -1])
    return x, y


def getSize(database, attr, attr_name):
    tx: DB
    for tx in database:
        size = 10
        if getattr(tx, attr_name) == attr:
            size += 1
        tx.size = size
    return size


def getNewAddresses(database: list, processed):
    new = []
    tx: DB
    for tx in database:
        if getattr(tx, FROM) not in processed:
            new.append(getattr(tx, FROM))

    return new
