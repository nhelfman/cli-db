# cli-db

A "no daemon" key-value database that can be safely used from command line from multiple concurrent processes.

Might be useful where a very light weight persistable state communication between processes/scripts is need. 
Data is stored on the file system and concurrent access protection is done using simple file locking.
Performance is predicted to be limited since for every read/write the whole database is locked.

```
Usage: python cli-db <set key value|get key|del key>
```

Example:
```
$ python cli-db set foo bar
$ python cli-db get foo
foo
$ python cli-db del foo
$ python cli-db get foo
$
```
