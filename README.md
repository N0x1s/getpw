# getpw!
[![Python 3.7.1](https://img.shields.io/badge/Python-3.7.1-green.svg)](http://www.python.org/download/)

A better way to get passwords from users in python

what getpw do for you?
----
* a secure way to read passwords from users
* check password strength and length
* custom prompt and mask
## install
You can either install from pypi or  the source code
1) Using pip
```bash
pip install getpw
```
2) from the source code
```bash
git clone https://github.com/n0x1s/getpw
cd getpw
pip install -e .
```
## How to use

Let us suppose you want to get a password or a secret token from the user without exposing him
```python
>>> from getpw import getpw
>>> getpw()
> Enter Password: ***********
```
[![asciicast](https://asciinema.org/a/ZbPCRLDoQ904FfGfDhLcd3lXt.svg)](https://asciinema.org/a/ZbPCRLDoQ904FfGfDhLcd3lXt)
arguments that you can pass:
- prompt : message that will be showen to the user -> default 'Enter Password: '
- mask : char that will replace password chars -> default '*'
- minlength : the minimum length -> default 1
- minlength : the maximum length -> default 32
- delay : delay in seconds -> default None
- strong: check if password strong -> default False

## Todo
I will try to maintain this respiratory and update or add new things to it you are welcome to contribute :relaxed:

And, as always have a beautiful day!
