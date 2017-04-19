#!/usr/bin/env python3

import re

def parse_line(line):
	line = line.rstrip() # strip line endings
	line = line.replace('\item [] ', '').replace('\mathit', '').replace('\\times ', '*') # replace latex commands
	line = re.sub(r'[$\{\}\.]', '', line) # replace formatting characters
	line = re.sub('^[0-9]{1,5}\s?=\s?', '', line) # replace results on line beginnings
	line = line.replace('^', '**')
	line = re.sub(r'([0-9])\(', '\g<1>*(', line) # fix '123(' problem
	line = line.replace(')(', ')*(') # fix ')(' problem
	try: eval(line) # malformed lines like '\\' and the 10958 line '\mboxstill not available'
	except SyntaxError: return None
	return line

def get_equations(lines):
	begin = r'\\item\[\]\$?\\mbox\{Increasing order\}\$?'
	end = r'\\item\[\]\$?\\mbox\{Decreasing order\}\$?'

	eqs = []
	in_block = False
	for line in lines:
		if re.match(begin, line):
			in_block = True
			continue
		if re.match(end, line):
			in_block = False
			continue
		if in_block:
			eq = parse_line(line)
			if eq: eqs.append(eq)

	return eqs

def read_equations(filename):
	with open(filename, errors='replace') as input_file:
		content = input_file.readlines()

	eqs = get_equations(content[115:22659])
	assert len(eqs) == 11111 # 0 to 11111 = 11112 minus the one for 10958

	for eq in eqs:
		print('{} = {}'.format(eq, eval(eq)))

def main():
	equations = read_equations('10958.tex')

if __name__ == '__main__':
	main()