#/usr/bin/env python3

import sys
import re

def eval_sheet(sheet, values):
	for i in range(len(sheet)):
		for j in range(len(sheet[i])):
			eval_cell(sheet, values, (i,j))

def eval_cell(sheet, values, cell):
	i, j = cell
	result = None
	if values[i][j] == ():
		print("error: recursive formula")
	elif values[i][j] == None:
		values[i][j] = ()
		result = eval_s(sheet, values, sheet[i][j])
		values[i][j] = result
	else:
		result = values[i][j]
	return result
	
def eval_s(sheet, values, s):
	if isinstance(s, list) and len(s) > 0:
		op = s[0]
		if op in operators:
			result = operators[op](sheet, values, s[1:])
		else:
			result = [eval_s(sheet, values, i) for i in s]
	else:
		result = s
	return result

def convert(t):
	if t.isdigit():
		result = int(t)
	elif re.match("\d+(\.\d*)?",t) == (0,len(t)):
		result = float(t)
	else:
		result = t
	return result

def parse_s(text):
	root = []
	currents = []
	current = root
	for i in re.split("([\(\)])",text):
		if i == "(":
			t = []
			current.append(t)
			currents.append(current)
			current = t
		elif i == ")":
			current = currents.pop()
		else:
			current += [convert(j) for j in i.split()]
	return root[0]

def rec_reduce(sheet, values, s, op, neutral):
	result = neutral
	for i in s:
		tmp = eval_s(sheet, values, i)
		if isinstance(tmp, list):
			tmp = rec_reduce(sheet, values, tmp, op, neutral)
		result = op(result, tmp)
	return result

def op_sum(sheet, values, s):
	return rec_reduce(sheet, values, s, lambda x,y: x+y, 0)

def op_rest(sheet, values, s):
	return rec_reduce(sheet, values, s, lambda x,y: x-y, 0)

def op_mult(sheet, values, s):
	return rec_reduce(sheet, values, s, lambda x,y: x*y, 1)

def op_div(sheet, values, s):
	return rec_reduce(sheet, values, s[1:], lambda x,y: x/y, float(s[0]))

def op_range(sheet, values, s):
	ai, aj, bi, bj = s
	return [["@",i,j] for i in range(ai,bi) for j in range(aj,bj)]

def parse_input():
	textsheet = [i.strip().split("\t") for i in sys.stdin.readlines()]
	sheet = [[parse_s(j) for j in i] for i in textsheet]
	values = [[None for j in i] for i in sheet]
	return sheet, values

def print_sheet(v):
	for i in v:
		print("\t".join(map(str, i)))

operators = {
    "+": op_sum,
    "-": op_rest,
    "*": op_mult,
    "/": op_div,
    "@": eval_cell,
    "#": op_range,
}

s, v = parse_input()
eval_sheet(s, v)

print_sheet(v)