import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def method(f, f_pr, x0, tol):
  xnew = xold = x0
  dx = 1000.
  iters = 0
  max_iters = 1000
  print "initial guess: ", x0
  
  while dx > tol:
  	if iters > max_iters:
  		print "Exceeded {0:3d} iterations without converging".format(max_iters)
  		return 0
  	xnew = xold - (1./f_pr(xold)) * f(xold)
  	dx = np.abs(xnew-xold)
  	xold = xnew
  	iters+=1
  	print xnew
  return xnew
  

def method_vis(ax, f, f_pr, x0, tol):
  xnew = xold = x0
  ax.plot(xold,0, 'go', label='x0')
  dx = 1000.
  iters = 0
  max_iters = 1000
  
  # initialize data arrays - useful for setting window size 
  data=[[x0],[0]] # Contains matching x and y values for plotting
  
  print "initial guess: ", x0
  
  while dx > tol:
    if iters > 1000:
	    print "Exceeded {0:3d} iterations without converging".format(max_iters)
	    return 0
      
    # draw line from current x straight up to graph of f
    ax.plot((xold, xold), (0, f(xold)), 'k-')
    #ax.arrow(xold, 0, 0, f(xold), lw=.5, head_width=.2)
    
    xnew = xold - (1./f_pr(xold)) * f(xold)
    
    #update data store
    data[0].append(xold)
    data[1].append(f(xold))
    data[0].append(xnew)
    data[1].append(0.)
	
    #draw line from graph of f to new estimate of root
    ax.plot((xold, xnew), (f(xold), 0), 'k-')
    ax.plot(xnew,0, 'ko')
	
    dx = np.abs(xnew-xold)
    xold = xnew
    iters+=1
    print xnew
  ax.plot(xnew,0, 'ro')  # print last point in red
  
  data = np.array(data) 
  set_axis_lims(ax, data, f) # adjust window size
  
  plt.legend()
  plt.show()
  return xnew
  

"""
Perform 1-D Newton's method and create animation
showing extimates and transitions
"""

def method_animate(fig, ax, f, f_pr, x0, tol):
  ax.plot(x0,0, 'go', label='x0')
  dx = 1000.
  iters = 0
  max_iters = 1000
  xnew = xold = x0
  
  # initialize data arrays
  data=[[],[]] # Contains matching x and y values for plotting
  data[0].append(x0)
  data[1].append(0.)
  
  print "initial guess: ", x0
 
  while dx > tol:
    iters+=1
    if iters>1000:
      print "Exceeded {0:3d} iterations without converging".format(max_iters)
      return 0
    
    data[0].append(xold)
    data[1].append(f(xold))
    xnew = xold - (1./f_pr(xold)) * f(xold)
    data[0].append(xnew)
    data[1].append(0.)
    
    dx = np.abs(xnew-xold)
    xold = xnew
    print xnew
   
     
  def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,
    
  data = np.array(data) # convert to numpy array
  set_axis_lims(ax, data, f) # adjust window size
  line, = plt.plot([],[],'r-') # draw lines
  n = len(data[0,:]) # number of points to plot  
  line_ani = animation.FuncAnimation(fig, update_line, n, fargs=(data,line),
                                                   interval=500, blit=True)

  ax.plot(xnew,0, 'ro')  # print last point in red
  plt.legend()
  plt.show()
  return xnew

  
"""
Set axis limits based on given data points and plot data
"""
def set_axis_lims(ax, data, f):
  overhang = 0.5 # window overhang as percent of data width
  num_pts = 1000. # number of points to use for plotting function
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
  
  xvals = np.arange(xlim_low, xlim_high, delta_x/num_pts)
  yvals = f(xvals)
  
  ax.plot(xvals,yvals)