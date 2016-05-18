import numpy as np
import matplotlib.pyplot as plt
import utility as util

"""
Arguments:
- f   = function defined on arrays of size m
  which returns np.array of size n
- Df = Jacobian matrix of entries for f; n x m
- x0 = initial guess for root; array of size m
- tol = convergence criterion
"""

def method(f, Df, x0, tol):
  xnew = xold = x0
  dx = 1000.
  iters = 0
  max_iters = 1000
  print "initial guess: ", x0
  while dx > tol:
    if iters > max_iters:
      print "Exceeded {0:3d} iterations without converging".format(max_iters)
      return 0
    deltax = util.solve(Df(xold), -f(xold))
    xnew = xold + deltax
    dx = np.linalg.norm(deltax)
    xold = xnew
    iters+=1
    print xnew
  return xnew