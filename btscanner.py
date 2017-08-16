from time import sleep
from datetime import datetime

import pickle

import bluetooth


def open_db():
    try:
        with open('btdump.pickle', 'rb') as dbfile:
            return pickle.load(dbfile)
    except FileNotFoundError:
        return {}


def store_db(db):
    with open('btdump.pickle', 'wb') as dbfile:
        pickle.dump(db, dbfile)


while True:
    db = open_db()
    devices = bluetooth.discover_devices(lookup_names=True)
    db[datetime.now()] = devices
    store_db(db)
    print("Devices: {}".format(devices))
    print("Sleeping 30 s")
    sleep(30)

