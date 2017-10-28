#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 00:17:42 2017

@author: wahidari
"""

import itertools

def select(C):
	return C[0]

def suitable(total, x, needle):
	return (total+x) <= needle

# greedy w/ solution
def greedy_s(C, needle):
	S = []
	total = 0
	while sum(S) != needle:
		for x in C:
			if suitable(total, x, needle):
				total += x
				S.append(x)
	return S

# bruteforce
def bforce(C, needle):
	infinite = 10000
	for repeater in range(1, infinite, 1):
		for S in itertools.product(C, repeat=repeater):
			if sum(S) == needle:
				return S

if __name__ == '__main__':
	# C := Himpunan Kandidat
	# S := Himpunan Solusi
	# n := Needle (Yang diinginkan)

	C = [	[25, 10, 5, 1],
             [25, 10, 5, 1], 
			[5, 4, 3, 1], 
			[10, 7, 1],
			[15, 10, 1]]
	n = [73, 32, 7, 15, 20]
	
	for i in range(4):
		print ('\n[+] Koin: {0}'.format(C[i]))
		print ('[+] Uang yang ditukar: {0}'.format(n[i]))
		print ('[+] Solusi Greedy: {0}'.format(greedy_s(C[i],n[i])))
		print ('[+] Solusi Bruteforce: {0}'.format(bforce(C[i],n[i])))