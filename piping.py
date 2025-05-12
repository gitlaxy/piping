import numpy as np
import math
from scipy.optimize import fsolve

def equations(vars):
	gra = 9.81
	g2 = 2*gra
	d = 0.015
	area = (math.pi*d**2)/4	
	ks = 1.004E-6
	const = 1.5E-6/(3.7*d)
	den_gra = 998.0*gra
	
	v1_dot, v2_dot, v3_dot, v1, v2, v3,	Re1, Re2, Re3, f1, f2, f3 = vars

	#eq1 = v1_dot - 0.0009
	eq2 = v1_dot - v2_dot - v3_dot
	eq3 = f1*((5/d)*(v1**2/g2)) + (f2*6/d + 24.7)*(v2**2/g2) - (200000/den_gra) + 2
	eq4 = f1*((5/d)*(v1**2/g2)) + (f3*1/d + 26.9)*(v3**2/g2) - (200000/den_gra) + 1
	eq5 = v1 - v1_dot/area
	eq6 = v2 - v2_dot/area
	eq7 = v3 - v3_dot/area
	eq8 = Re1 - v1*d/ks
	eq9 = Re2 - v2*d/ks
	eq10 = Re3 - v3*d/ks
	eq11 = 1/math.sqrt(f1) + 2*math.log2(const + 2.51/(Re1*math.sqrt(f1)))
	eq12 = 1/math.sqrt(f2) + 2*math.log2(const + 2.51/(Re2*math.sqrt(f2)))
	eq1 = 1/math.sqrt(f3) + 2*math.log2(const + 2.51/(Re3*math.sqrt(f3)))
	#eq14 = DP_12 - DP_13
	#eq1 = DP_12 - 200000

	return [eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, eq12]

initial_guesses = [0.0009, 0.00042,0.00048,5.09,2.4,2.7,7e10,8e10,9e10,0.00008,0.00008,0.00008]

solution = fsolve(equations, initial_guesses)
print("Solution to the system:", solution)

# Print the results
v1_dot, v2_dot, v3_dot, v1, v2, v3, Re1, Re2, Re3, f1, f2, f3 = solution

print(f"Solved values are \
	v1_dot = {v1_dot:.6f}, v2_dot = {v2_dot:.6f}, v3_dot = {v3_dot:.6f}, \
	v1 = {v1:.2f}, v2 = {v2:.2f}, v3 = {v3:.2f}, \
	Re1 = {Re1:.2f}, Re2 = {Re2:.2f}, Re3 = {Re3:.2f}, \
	f1 = {f1:.5f}, f2 = {f2:.5f}, f3 = {f3:.5f}")

den_gra = 998.0*9.81
d = 0.015
const = 1.5E-6/(3.7*d)
	
print((200000/den_gra) - 2)
print((200000/den_gra) - 1)
print(1/math.sqrt(f1))
print(2*math.log2(const + 2.51/(Re1*math.sqrt(f1))))
