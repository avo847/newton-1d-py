import numpy as np
import scipy.linalg as linalg
"""
Set axis limits based on given data points and plot data
"""
def set_axis_lims(ax, data):
  overhang = 0.5 # window overhang as percent of data width
  #num_pts = 1000. # number of points to use for plotting function
  xmin = np.min(data[0,:])
  xmax = np.max(data[0,:])
  ymin = np.min(data[1,:])
  ymax = np.max(data[1,:])
  
  delta_x = xmax - xmin
  delta_y = ymax - ymin
  
  xlim_low = xmin - overhang * delta_x
  xlim_high = xmax + overhang * delta_x
  ylim_low = ymin - overhang * delta_y
  ylim_high = ymax + overhang * delta_y
  ax.set_xlim(xlim_low, xlim_high)
  ax.set_ylim(ylim_low, ylim_high)
  


"""
Solve a square linear system using 
LU factorization, forward- and back-
substitution.
"""
def solve(A, b):
  [nrows, ncols] = np.shape(A)
  nrows = int(nrows)
  ncols = int(ncols)
  if ncols != nrows:
    print "WARNING: System is not square."
  P,L,U = linalg.lu(A)
  
  #Use forward substitution to solve Ly = Pb
  Pb = np.dot(P,b)
  y = np.array([0.]*ncols)
  for i in np.arange(0,ncols):
    y[i] = ( Pb[i] - np.dot(L[i,0:i],y[0:i])) / L[i,i]
  
  # Use back-substitution to solve Ux = y
  x = np.array([0.]*ncols)
  for i in range(ncols-1, -1, -1):
    x[i] = (y[i] - np.dot(U[i,(i+1):ncols], x[i+1:ncols]))/U[i,i]

  return x