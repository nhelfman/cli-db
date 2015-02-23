import json
import os
import tempfile
import portalocker

DEFAULT_DB_FILE=os.path.join(tempfile.gettempdir(), "cli-db.json")

class CliDb:
    def __init__(self, db_file=DEFAULT_DB_FILE):
        self._db_file = db_file

    @property
    def db_lock(self):
        return portalocker.Lock(self._db_file + ".lock", timeout=0.5)

    def set(self, key, value):
        with self.db_lock:
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
        with self.db_lock:
            if not os.path.isfile(self._db_file):
                return None

            with open(self._db_file, "r+") as db_fp:
                db = json.load(fp=db_fp)
                value = db.get(key)
                return value