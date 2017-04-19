#!/usr/bin/env python3

import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit as curve_fit

def generate_equation():
	nums = list(map(str, range(1,10)))
	ops = ['+', '-', '*', '/', '^', '']

	result = list([None]*(2*len(nums)-1))
	result[::2] = nums
	for i in range(1,len(result),2):
		result[i] = random.choice(ops)
	return ''.join(result)

def remaining_numbers(results):
	return [i for i, eq in enumerate(results) if eq is None]

def plot(results, iterations, remaining):
	fig, ax = plt.subplots(2)

	# Remaining plot
	ax[0].hist(remaining_numbers(results), bins=1000)

	# Progress plot
	ax[1].plot(iterations, remaining)
	ax[1].set_ylim(0,11111)
	ax[1].set_xlabel('Iterations')

	plt.show()

def main():
	NUM = 1e7

	results = [None]*11111
	iterations = []
	remaining = []

	i = 0
	while True:
		i += 1
		try:
			if i%10000 == 0:
				iterations.append(i)
				remaining.append(len(remaining_numbers(results)))
				print('{:.0f}%'.format(i/NUM*100))
			if i > int(NUM):
				break

			eq = generate_equation()
			result = eval(eq)
			if isinstance(result, int):
				if 1 <= result <= 11111:
					results[result-1] = eq
				if result == 10958:
					print('Found it! -> {}'.format(eq))
		except TypeError:
			continue

	plot(results, iterations, remaining)

if __name__ == '__main__':
	main()