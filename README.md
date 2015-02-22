# cli-db

A stateless (no daemon) kay-value database that can be safely used from command line.

Data is stored on the file system and concurrent access protection is done using simple file locking.

Performance is predicted to be limited since for every read/write the whole database is locked.

Usage:
```
cli-db [--database my.db.json] <set|get> <value>
```

Example:
```
$ cli-db set foo bar
$ cli-db get foo
foo
```
