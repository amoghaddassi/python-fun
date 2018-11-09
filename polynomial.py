"""Polynomial object."""

import numpy as np

class Polynomial:
	def __init__(self, *coeffs):
		self.coeffs = coeffs

	def __repr__(self):
		return 'Polynmoial{}'.format(self.coeffs)

	def __add__(self, other):
		return Polynomial(*(x + y for x,y in zip(self.coeffs, other.coeffs)))

	def __len__(self):
		return len(self.coeffs)

	def __call__(self, x):
		x_vals = np.array([])
		for i in np.arange(len(self.coeffs)):
			x_vals = np.append(x_vals, x ** (len(self.coeffs) - 1))
		return sum(np.array(self.coeffs) * x_vals)

		