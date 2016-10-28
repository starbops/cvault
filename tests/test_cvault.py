from unittest import TestCase
from playhouse.test_utils import test_database
from peewee import *

from cvault import Entry

test_db = SqliteDatabase(':memory:')

class EntryTest(TestCase):

    def create_test_data(self):
        for i in range(10):
            Entry.create(acct="user-{}".format(i),
                         passwd="passwd-{}".format(i),
                         desc="Credential of user-{}".format(i))

    def test_save_entry(self):
        with test_database(test_db, (Entry,)):
            self.create_test_data()
            #self.assertEqual()

        #with test_database(test_db, (Entry,)):
        #    self.test_some_user_thing()

    def test_remove_entry(self):
        assert True

    def test_list_entry(self):
        assert True

    def test_show_entry(self):
        assert True
