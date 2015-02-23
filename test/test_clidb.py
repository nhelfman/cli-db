import os
import tempfile
import unittest
from clidb.cli_db import CliDb


DB_FILE=os.path.join(tempfile.gettempdir(), "_test_cli-db.json")

class CliDbTest(unittest.TestCase):
    def setUp(self):
        if os.path.isfile(DB_FILE):
            os.remove(DB_FILE)

    def test_1(self):
        db = CliDb()
        db.set("foo", "bar")

        db = CliDb()
        actual = db.get("foo")

        self.assertEquals("bar", actual, "value should be bar")