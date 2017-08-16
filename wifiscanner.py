import pickle

from datetime import datetime
from time import sleep

from wifi import parse_cells, scan


def open_db():
    try:
        with open('wifidump.pickle', 'rb') as dbfile:
            return pickle.load(dbfile)
    except IOError:
        return {}


def store_db(db):
    with open('wifidump.pickle', 'wb') as dbfile:
        pickle.dump(db, dbfile)


while True:
    db = open_db()
    cells = parse_cells(scan())
    db[datetime.now()] = cells
    store_db(db)
    print("Cells: {}".format(cells))
    print("Sleeping 30 s")
    sleep(30)
