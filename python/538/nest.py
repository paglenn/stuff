# Translation to Python/NumPy of Sauer's
# Program 0.1 Nested multiplication
# Evaluates polynomial from nested form using Horner's method
# Input: 
# degree d of polynomial,
# array of d+1 coefficients c (constant term first)
# x-coordinate(s) x at which to evaluate, and
# array of d base points r, if needed
# Output: value y of polynomial at x
from numpy import *
def nest(d,c,x,b=[]):
	if b==[]:
		b = zeros(d) 
	y = c[d]
	for i in range(d-1,-1,-1):
		y *= (x-b[i])
		y += c[i]
	return y
'''
# test_nest.py
# Test on examples on Sauer p4 (1st ed)
from nest import nest
print nest(4,[-1,5,-3,3,2],1.0/2.0,[0,0,0,0])
print nest(4,[-1,5,-3,3,2],1.0/2.0)        # test default base-points argument
print nest(4,[-1,5,-3,3,2],[-2,-1,0,1,2])  # works on list of evaluation points too
print nest(3,[1,0.5,0.5,-0.5],1,[0,2,3])
'''
