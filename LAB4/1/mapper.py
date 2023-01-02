#!/usr/bin//env python3
import sys

for line in sys.stdin:
	line = line.lower()

special_characters = ['!','@','#','$','%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '/', '?', '~', '`']
for x in line:
	for y not in special_characters:
		if x == y:
			line=line.replace(x,"")

	words = line.split()
	for word in words:
		print('{0}\t{1}'.format(word, 1))
