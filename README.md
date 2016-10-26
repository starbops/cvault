cvault
======

Credential Vault (cvault) is a place where you can save your memory about credentials, e.g. account and password, along with some helpful description.


Installation
------------

Run the installer script to install dependencies and the cvault program.

~~~ sh
$ ./install.sh
~~~

Then initialize the vault (database).

~~~ sh
$ cvault init </path/to/vault>
~~~


Usage
-----

There are two modes in cvault:

1. interactive mode: cvault will open up a dialog, and you can interact with it
2. non-interactive mode: saves entry with one shot, no more dialog

### Interactive Mode

~~~ sh
$ cvault
~~~

And follow the instructions to achive the goal.

### Non-interactive Mode

~~~ sh
$ cvault save -a <account> -p<password> -d <description> # save a new entry
$ cvault remove <id> # remove certain entry
$ cvault list # list all the entries reside in the vault
$ cvault show <id> # show the exact entry
$ cvault search -a <account> # with exact account name
$ cvault search -d <pattern> # pattern searching in description
~~~
