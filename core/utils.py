import random
from core.config import DB
from core.config import FROM
from core.colors import red, info
from math import log, floor
from core.config import ZERO_ADDRESS
import json


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
        tx.size_from = getSize(database, getattr(tx, FROM), FROM)
        tx.size_to = getSize(database, getattr(tx, "to"), "to")
        sizes.append(tx.size_from + tx.size_to)
    index = 0
    # max(sizes) >= 0 and index < top
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


# need some optimization, this is a bottleneck for large address sets (1000+)
def getSize(database, attr, attr_name):
    base = 10
    tx: DB
    size = 4
    for tx in database:
        if getattr(tx, attr_name) == attr:
            size += 1
    return size if size <= base else base


def getNewAddresses(database: list, processed):
    new = []
    tx: DB
    for tx in database:
        if getattr(tx, FROM) not in processed:
            new.append(getattr(tx, FROM))

    return new


def getNodeName(name):
    labels = json.loads(open("labels/labels.json").read())
    try:
        return labels[name]
    except:
        return name
