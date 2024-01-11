# AirBnB clone - The console

The console marks the initial phase of the AirBnB project at Holberton School, covering essential concepts in higher-level programming. objective of the AirBnB project is to deploy a server with a simplified version of the AirBnB website (HBnB). This segment focuses on the creation of a command interpreter to efficiently manage objects within the context of the AirBnB (HBnB) website.
 > This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## 🛠️ Installation
- Clone this repository and switch into the project's directory.
- Run in interactive mode.
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
- Run in non-interactive mode: 
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
