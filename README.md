# cli-db

A stateless (no daemon) kay-value database that can be safely used from command line from multiple concurrent processes.

Might be useful where a very light weight persistable state communication between processes/scripts is need. 
Data is stored on the file system and concurrent access protection is done using simple file locking.
Performance is predicted to be limited since for every read/write the whole database is locked.

```
Usage: cli-db <set key value|get key|del key>
```

Example:
```
$ cli-db/main.py set foo bar
$ cli-db/main get foo
foo
$ cli-db/main del foo
$ cli-db/main get foo
$
```
