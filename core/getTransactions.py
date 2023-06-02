from core.requester import request_txns
from core.requester import request_inner_txns
from core.config import DB
from core.config import ZERO_ADDRESS


def parseTxn(tx):
    db = DB()
    for attr in tx:
        db.set_attr(attr, tx[attr])
    return db


def getTransactions(address, processed, database, limit):
    addresses = []
    # pages = pageLimit(limit)
    txn = request_txns(address, limit)
    inner_txn = request_inner_txns(address, limit)
    for arr in txn, inner_txn:
        for txn in arr["result"]:
            addresses.append(txn["from"])
            addresses.append(txn["to"])
            db = DB()
            for attr in txn:
                db.set_attr(attr, txn[attr])
            if txn["from"] == "":
                db.set_attr("from", ZERO_ADDRESS)
            if txn["to"] == "":
                db.set_attr("to", ZERO_ADDRESS)

            database.append(db)

        processed.add(address)
    addresses = list(dict.fromkeys(addresses))
    return addresses
