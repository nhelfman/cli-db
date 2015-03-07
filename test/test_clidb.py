import os
import tempfile
import unittest
import sys
import clidb
from clidb.cli_db import CliDb
import main


DB_FILE = os.path.join(tempfile.gettempdir(), "_test_cli-db.json")


class CliDbTest(unittest.TestCase):
    def setUp(self):
        self.db = CliDb(DB_FILE)
        if os.path.isfile(DB_FILE):
            os.remove(DB_FILE)

    def tearDown(self):
        if os.path.isfile(DB_FILE):
            os.remove(DB_FILE)

        if os.path.isfile(DB_FILE + ".lock"):
            os.remove(DB_FILE + ".lock")

    def test_basic(self):
        self.db.set("foo", "bar")

        self.db = CliDb(DB_FILE) # new instance
        actual = self.db.get("foo")

        self.assertEquals("bar", actual, "value should be bar")

    def test_no_val(self):
        val = self.db.get("foo")

        self.assertIsNone(val, "value should not exist")

    def test_delete(self):
        self.db.set("foo", "bar")

        self.db.delete("foo")

        val = self.db.get("foo")
        self.assertIsNone(val, "value should be None after delete")

    def test_delete_none_existing(self):
        self.db.delete("foo")

        val = self.db.get("foo")
        self.assertIsNone(val, "value should be None after delete")
