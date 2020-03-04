from mpl_toolkits.mplot3d import axes3d
import numpy as np 
from matplotlib import animation, cm, pyplot as plt
def first_derivative(x,y):
	delx = x[1]-x[0]
	dy_list = np.copy(y)

	for i in range(len(y)):

		if i==0:
			#dy = 0
			dy = (y[1] - y[0]) / delx


		elif i == len(y) - 1:
			#dy = 0
			dy = (y[i] - y[i-1]) / delx


		else:

			dy = (y[i+1] - y[i-1])/(2*delx)

		dy_list[i] = dy

	return dy_list
def second_derivative(x,y):
	delx = x[1]-x[0]
	dy_list = np.copy(y)

	for i in range(len(y)):

		if i==0:
			#dy = (y[1] - y[0]) / delx
			dy = 0
		elif i == len(y) - 1:
			#dy = (y[i] - y[i-1]) / delx
			dy = 0
		else:

			dy = (y[i+1] - y[i-1])/(2*delx)

		dy_list[i] = dy

	return dy_list

def local_laplacian(z, x, y):
	dz = np.copy(z)

	dx = np.copy(x)
	for i in range(len(x)):
		dx[i] = second_derivative(x[i],first_derivative(x[i],z[i]))
		
	dy = np.copy(y)	
	for i in range(len(y)):
		dy[:,i] = second_derivative(y[:,i],first_derivative(y[:,i],z[:,i]))


	for i in range(len(y)):
		for k in range(len(x)):
			dz[i][k] = dx[i][k] + dy[i][k]

	return dz
		

def animate(i):
	dt=0.025

	global x
	global y
	global z
	global v
	
	dv = dt * local_laplacian(z,x,y)

	v = v+(dv)

	z = (z + (v*dt))
	
	ax.clear()
	print("FRAME ", i, " RENDERED")
	#ax.axis('off')
	surface = ax.plot_surface(x,y,z)	

	ax.set_xlim(x_limit[0],x_limit[1])
	ax.set_ylim(y_limit[0],y_limit[1])
	ax.set_zlim(z_limit[0],z_limit[1])
	return surface


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x_limit = [-6,6]
y_limit = [-6,6]
z_limit = [0,3]


x = np.linspace(x_limit[0],x_limit[1],60)
y = np.linspace(y_limit[0],y_limit[1],60)

x,y = np.meshgrid(x,y)

z= 1/(1+ x**2 + y**2)
v = 0*x

	


ani = animation.FuncAnimation(fig,animate,interval=180,blit=False,frames=1500)


#ani.save('test_wave.gif',fps=60)

plt.show()

