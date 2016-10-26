#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Usage:
  cvault.py init <vault_name>
  cvault.py save <account> <password> <description>
  cvault.py remove <entry_id>
  cvault.py list
"""
from docopt import docopt
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

import datetime
import os

db = SqliteExtDatabase('vault.db')


class Entry(Model):
    acct = CharField()
    passwd = CharField()
    desc = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def init_vault(vault_name):
    db.connect()
    try:
        db.create_tables([Entry])
    except OperationalError:
        print("Vault \"{}\" is already initialized.".format(vault_name))

def save_entry(acct, passwd, desc):
    entry = Entry(acct=acct, passwd=passwd, desc=desc)
    entry.save()

def remove_entry(entry_id):
    try:
        entry = Entry.get(Entry.id == entry_id)
    except Entry.DoesNotExist:
        print('The given entry ID does not exist.')
    else:
        entry.delete_instance()

def list_entries():
    for entry in Entry.select():
        print("{e.id}: {e.acct}|{e.passwd}|{e.desc}" .format(e=entry))

def cvault(vault_name, acct, passwd, desc, entry_id, init=False, save=False,
        remove=False, dump=True):
    if init:
        init_vault(vault_name)
    elif save:
        save_entry(acct, passwd, desc)
    elif remove:
        remove_entry(entry_id)
    elif dump:
        list_entries()
    else:
        list_entries()

def main():
    args = docopt(__doc__, version='cvault 0.1')

    kwargs = {
        'init': args['init'],
        'vault_name': args['<vault_name>'],
        'save': args['save'],
        'acct': args['<account>'],
        'passwd': args['<password>'],
        'desc': args['<description>'],
        'remove': args['remove'],
        'entry_id': args['<entry_id>'],
        'dump': args['list'],
    }

    cvault(**kwargs)


if __name__ == '__main__':
    main()
