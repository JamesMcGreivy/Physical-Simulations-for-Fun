import numpy as np 
from matplotlib import animation, cm, pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(111)
x_limit = [-5,5]
y_limit = [-1,1]

def first_derivative(x,y):
	delx = x[1]-x[0]
	dy_list = np.copy(y)

	for i in range(len(y)):

		if i==0:
			dy = 0

		elif i == len(y) - 1:
			dy = 0

		else:

			dy = (y[i+1] - y[i-1])/(2*delx)

		dy_list[i] = dy

	return dy_list

def second_derivative(x,y):
	delx = x[1]-x[0]
	dy_list = np.copy(y)

	for i in range(len(y)):

		if i==0:
			dy = (y[1] - y[0]) / delx

		elif i == len(y) - 1:
			dy = (y[i] - y[i-1]) / delx

		else:

			dy = (y[i+1] - y[i-1])/(2*delx)

		dy_list[i] = dy

	return dy_list





def animate(i):
	dt=0.03

	global previ
	global x
	global y
	global v
	
	dv = dt*second_derivative(x,first_derivative(x,y))

	v = v+dv

	y = 0.999*(y + (v*dt))

	if max(y) > 0.9:
		if i-previ > 1:
			print(i-previ)
		previ = i

	ax.clear()
	scatterplot = ax.plot(x,y)	

	ax.set_xlim(-5,5)
	ax.set_ylim(-5,25)

	return scatterplot


previ = 0
x = np.linspace(-5,5,400)
#y = np.sin(np.pi * x / 4)
y = x**2

v = 0*x

ani = animation.FuncAnimation(fig, animate, interval=20, blit=False)

plt.show()




