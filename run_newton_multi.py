import numpy as np
import matplotlib.pyplot as plt
import newton_multi_d as newton

def f(x):
  out = np.array([np.cos(x[0]-x[1])-x[1], np.sin(x[0]+x[1]) - x[0]])
  return out
  
def Df(x):
  out = np.array([ [-np.sin(x[0]-x[1]),    np.sin(x[0]-x[1])-1],
                         [ np.cos(x[0]+x[1])-1, np.cos(x[0]+x[1])  ]]  )
  return out

def f1(x):
  out = np.array([x[0]**2 - x[1] + np.sin(x[0]-x[1]) - 2.,
                        x[1]**2 - x[0] - 3.])
  return out

def Df1(x):
  out = np.array([ [2.*x[0] + np.cos(x[0]-x[1]), -1. - np.cos(x[0]-x[1])],
                         [-1., 2.*x[1]] ])
  return out
  
def f2(x):
  a = 0.001
  out = np.array( [x[0] + x[1] + np.sin(x[0]*x[1]) - a,
                         np.sin(x[0]**2 + x[1]) - 2*a])
  return out
  
def Df2(x):
  out = np.array([ [1. + x[1]*np.cos(x[0]*x[1]), 1. + x[0]*np.cos(x[0]*x[1])],
                         [2*x[0]*np.cos(x[0]**2 + x[1]), np.cos(x[0]**2 + x[1])] ])
  return out
  
try:
  x = newton.method(f2, Df2, [0.,0.], 0.00001)
  print "final value:", x 
  print "f(", x, ") = ", f2(x)
except ZeroDivisionError:
	print "Oops, divided by zero."
	print "Try again with different initial guess."