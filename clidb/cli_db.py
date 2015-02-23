import json
import os
import tempfile


class CliDb:
    def __init__(self):
        self._db_file = "/tmp/cli-db.json"  # TODO - make dynamic based on arguments

    def set(self, key, value):
        if not os.path.isfile(self._db_file):
            with open(self._db_file, "w") as db_fp:
                json.dump({}, fp=db_fp, indent=4)

        with open(self._db_file, "r+") as db_fp:
            db = json.load(fp=db_fp)
            db[key] = value

        tmp_fd, tmp_name = tempfile.mkstemp()
        with open(tmp_name, "w") as tmp_db_fp:
            json.dump(db, fp=tmp_db_fp, indent=4)

        os.rename(tmp_name, self._db_file)


    def get(self, key):
        if not os.path.isfile(self._db_file):
            return None

        with open(self._db_file, "r+") as db_fp:
            db = json.load(fp=db_fp)
            value = db.get(key)
            return value