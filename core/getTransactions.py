from re import findall
from core.utils import pageLimit
from core.requester import requester
from core.requester import request_txns
from core.requester import request_inner_txns
from DB import DB
from core.globalVars import ZERO_ADDRESS

def parseTxn(tx):
    db = DB()
    for attr in tx:
        db.set_attr(attr, tx[attr])
    return db


def getTransactions(address, processed, database: list, limit):
    addresses = []
    pages = pageLimit(limit)
    for i in range(pages):
        txn = request_txns(address, pages)
        inner_txn = request_inner_txns(address, pages)
        for arr in txn, inner_txn:
            for txn in arr["result"]:
                db = DB()
                for attr in txn:
                    db.set_attr(attr, txn[attr])
                if txn["from"] == "":
                    db.set_attr("from",ZERO_ADDRESS)
                if txn["to"] == "":
                    db.set_attr("to",ZERO_ADDRESS)
                    
                database.append(db)

        processed.add(address)

    return addresses
