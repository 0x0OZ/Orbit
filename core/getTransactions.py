from re import findall
from core.utils import pageLimit
from core.requester import requester

from DB import DB

def getTransactions(address, processed, database: list, limit):
    addresses = []
    pages = pageLimit(limit)
    for i in range(pages):
        response = requester(address, pages)
        # matches = response['result'][0]['hash']
        for txn in response["result"]:
            db = DB()
            for attr in txn:
                #setattr(db,attr,txn[attr])
                db.set_attr(attr,txn[attr])
            database.append(db)
        processed.add(address)
    return addresses

