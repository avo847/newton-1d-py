import numpy as np
import matplotlib.pyplot as plt

import newton

def f(x):
  return x**2 - 3
  #return x**3 - x + np.sqrt(2.)/2.
  
def f_pr(x):
  return 2*x
  #return 3*x**2 -1

fig = plt.figure()
ax = fig.add_subplot(111)
plt.grid('on')

try:
  x = newton.method_animate(fig, ax, f, f_pr, 10., 0.0001)
  print "final value:", x 

except ZeroDivisionError:
	print "Oops, divided by zero."
	print "Try again with different initial guess."


