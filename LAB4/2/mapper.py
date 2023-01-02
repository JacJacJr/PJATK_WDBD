#!/usr/bin//env python3

import sys

for line in sys.stdin:
	line = line.lower()
	words = line.split()
	for word in words:
		for char in word:
			print('{0}\t{1}'.format(char, 1))
