#!/usr/bin/python
import sys
from cli_db import CliDb


def usage():
    print "Usage: cli-db <set key value|get key|del key>"


def main(args):
    if len(args) < 3:
        usage()

    command = args[1]
    if command == "set":
        key = args[2]
        if len(args) < 4:
            print "missing argument: value"
            usage()
            return 1

        value = args[3]
        db = CliDb()
        db.set(key, value)
        return 0

    elif command == "get":
        if len(args) < 3:
            print "missing argument: key"
            usage()
            return 1

        key = args[2]

        db = CliDb()
        value = db.get(key)
        if value:
            print value

        return 0

    elif command == "del":
        if len(args) < 3:
            print "missing argument: key"
            usage()
            return 1

        key = args[2]

        db = CliDb()
        db.delete(key)

        return 0
    else:
        print "Invalid command argument " + command
        usage()
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))

