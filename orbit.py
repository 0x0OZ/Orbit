#!/usr/bin/env python3

import os
import json
import random
import argparse
import webbrowser
import concurrent.futures

from core.utils import getNewAddresses
from core.utils import ranker
from core.utils import genLocation
from core.getQuark import getQuark
from core.exporter import exporter
from core.prepareGraph import prepareGraph
from core.getTransactions import getTransactions
from core.colors import green, white, red, info, run, end
from core.utils import getSize
from core.globalVars import SIZE
from core.globalVars import FROM
from core.globalVars import TO
from DB import DB

parse = argparse.ArgumentParser()
parse.add_argument("-s", "--seeds", help="target blockchain address(es)", dest="seeds")
parse.add_argument(
    "-o", "--output", help="output file to save raw JSON data", dest="output"
)
parse.add_argument(
    "-d", "--depth", help="depth of crawling", dest="depth", type=int, default=3
)
parse.add_argument(
    "-t",
    "--top",
    help="number of addresses to crawl from results",
    dest="top",
    type=int,
    default=20,
)
parse.add_argument(
    "-l",
    "--limit",
    help="maximum number of addresses to fetch from one address",
    dest="limit",
    type=int,
    default=100,
)
args = parse.parse_args()

top = args.top
seeds = args.seeds
depth = args.depth
limit = args.limit
output = args.output

print(
    """%s
  __         
 |  |  _ |  ' _|_
 |__| |  |) |  |  %sv2.0
%s"""
    % (green, white, end)
)



database = []  # array of DB 
processed = set()

seeds = args.seeds.split(",")
for seed in seeds:
    database.append(DB(from_=seed))

getQuark()

def crawl(addresses, processed, database, limit):
    threadpool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    futures = (
        threadpool.submit(getTransactions, address, processed, database, limit)
        for address in addresses
    )
    for i, _ in enumerate(concurrent.futures.as_completed(futures)):
        print("%s Progress: %i/%i        " % (info, i + 1, len(addresses)), end="\r")



try:
    for i in range(depth):
        print("%s Crawling level %i" % (run, i + 1))
        #database = ranker(database, top + 1)
        toBeProcessed = getNewAddresses(database, processed)
        #toBeProcessed = database
        print("%s %i addresses to crawl" % (info, len(toBeProcessed)))
        crawl(toBeProcessed, processed, database, limit)
except KeyboardInterrupt:
    pass

#database = ranker(database, top)

jsoned = {"edges": [], "nodes": []}
num = 0
doneNodes = []
doneEdges = []

txn: DB
for txn in database:
    x, y = genLocation()
    
    size = getSize(database,txn.from_,FROM)
    node = txn.from_

    if node not in doneNodes:
        doneNodes.append(node)
        jsoned["nodes"].append(
            {"label": node, "x": x, "y": y, "id": "id=" + node, "size": size}
        )
    uniqueSize = size
    x, y = genLocation()
    txn2: DB
    for txn2 in database:
        if txn2.from_ != node:
            continue
        
        uniqueSize = getSize(database,txn2.to,TO)
        
        x, y = genLocation()
        childNode = txn2.to if txn2.to else ""
        if childNode not in doneNodes:
            doneNodes.append(childNode)
            jsoned["nodes"].append(
                {
                    "label": childNode,
                    "x": x,
                    "y": y,
                    "id": "id=" + childNode,
                    "size": uniqueSize,
                }
            )
        if (node + ":" + childNode or childNode + ":" + node) not in doneEdges:
            doneEdges.extend([(node + ":" + childNode), (childNode + ":" + node)])
            jsoned["edges"].append(
                {
                    "source": "id=" + childNode,
                    "target": "id=" + node,
                    "id": num,
                    "size": uniqueSize / 3 if uniqueSize > 3 else uniqueSize,
                }
            )
        num += 1

print("%s Total wallets:%i" % (info, len(jsoned["nodes"])))
print("%s Total connections:%i" % (info, len(jsoned["edges"])))

render = json.dumps(jsoned).replace(" ", "").replace("'", '"')

prepareGraph("%s.json" % seeds[0], render)
webbrowser.open("file://" + os.getcwd() + "/quark.html")

if output:
    data = exporter(output, jsoned)
    new = open(output, "w+")
    new.write(data)
    new.close()

quit()
