import os
import re
import sys
import time
import string
if os.name == 'nt':
	from msvcrt import getwch
else:
	from .getchar import getwch



def getpw(prompt=None, mask=None, minlength=1,
				maxlength=32, delay=None, strong=False):
	display_msg(prompt if prompt is not None else 'Enter Password : ', delay)
	mask = mask if mask is not None else '*'
	length = range(minlength, maxlength)
	length_err = '\nlength is too {}, please enter a value in range of {}!'

	password = list()
	while True:
		ch = ord(getwch())
		if ch == 13:
			if len(password) not in length:
				s1 = 'short' if len(password) < length[0] else 'long'
				s2 = f'({length[0]} - {length[-1] + 1})'
				print(length_err.format(s1, s2))
				return getpw(prompt, mask, minlength, maxlength, delay, strong)
			elif strong:
				if not check_strength(password):
					print('\npassword is too weak')
					return getpw(prompt, mask, minlength, maxlength,
									delay, strong)
			break
		elif ch in {8, 127}:
			if len(password) != 0:
				sys.stdout.write('\b \b')
				sys.stdout.flush()
			password = password[:-1]
			continue
		elif ch == 2:
			sys.stdout.write('\b \b' * len(password))
			sys.stdout.flush()
			password = list()
			continue
		elif ch == 3:
			raise KeyboardInterrupt
		if chr(ch) in string.printable:
			password.append(ch)
			print(mask, end='', flush=True)
	print(flush=True)
	return ''.join(map(chr, password))

def display_msg(prompt, delay):
	for ch in prompt:
		print(ch, end='', flush=True)
		if delay is not None:
			time.sleep(delay)

def check_strength(password):
	password = ''.join(map(chr, password))
	return all({
		re.search(r"\d", password),
		re.search(r"[A-Z]", password),
		re.search(r"[a-z]", password),
		re.search(r"\W", password),
		}
	)
