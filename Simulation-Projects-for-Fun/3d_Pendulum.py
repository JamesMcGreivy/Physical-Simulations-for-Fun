from mpl_toolkits.mplot3d import axes3d
import numpy as np 
from matplotlib import animation, cm, pyplot as plt

g = 9.8

# Pendulum 1 Parameters
L1 = 4
theta1 = 0
phi1 = np.pi/3

dtheta1 = 0.8
ddtheta1 = 0

dphi1 = 0
ddphi1 = 0

# Pendulum 2 Parameters
L2 = 4
theta2 = 0
phi2 = np.pi/3

dtheta2 = 0
ddtheta2 = 0

dphi2 = 0
ddphi2 = 0


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x_limit = [-4,4]
y_limit = [-4,4]
z_limit = [-5,0]


def animate(i):
	global theta1, phi1, dtheta1, ddtheta1, dphi1, ddphi1
	global theta2, phi2, dtheta2, ddtheta2, dphi2, ddphi2



	dt = 0.01


	# Pendulum 1 Dif Eq
	ddphi1 = (-g/L1)*np.sin(phi1) + (dtheta1**2)*np.cos(phi1)*np.sin(phi1)
	dphi1 = dphi1 + ddphi1 * dt
	phi1 = phi1 + dphi1 * dt
	
	if dtheta1 != 0:
		ddtheta1 = -2*(dtheta1*dphi1)*(np.cos(phi1)/np.sin(phi1))
	dtheta1 = dtheta1 + ddtheta1 * dt
	theta1 = theta1 + dtheta1 * dt

	# Pendulum 2 Dif Eq
	ddphi2 = 0
	dphi2 = 0
	phi2 = phi2 + dphi2 * dt
	
	ddtheta2 = 0
	dtheta2 = dtheta2 + ddtheta2 * dt
	theta2 = theta2 + dtheta2 * dt

	# Plots two 3-d lines with a sphere on the end of them
	x1 = [0, L1*np.cos(theta1)*np.sin(phi1)]
	y1 = [0, L1*np.sin(theta1)*np.sin(phi1)]
	z1 = [0, -L1*np.cos(phi1)]

	u1 = np.linspace(0, np.pi, 17)
	v1 = np.linspace(0, 2 * np.pi, 17)
	x_sph1 = x1[1]+0.25*np.outer(np.sin(u1), np.sin(v1))
	y_sph1 = y1[1]+0.25*np.outer(np.sin(u1), np.cos(v1))
	z_sph1 = z1[1]+0.25*np.outer(np.cos(u1), np.ones_like(v1))

	"""
	x2 = x1[1] + [0, L2*np.cos(theta2)*np.sin(phi2)]
	y2 = y1[1] + [0, L2*np.sin(theta2)*np.sin(phi2)]
	z2 = z1[1] + [0, -L2*np.cos(phi2)]

	u2 = np.linspace(0, np.pi, 17)
	v2 = np.linspace(0, 2 * np.pi, 17)
	x_sph2 = x2[1]+0.25*np.outer(np.sin(u2), np.sin(v2))
	y_sph2 = y2[1]+0.25*np.outer(np.sin(u2), np.cos(v2))
	z_sph2 = z2[1]+0.25*np.outer(np.cos(u2), np.ones_like(v2))

	"""
	ax.clear()
	ax.plot(x1,y1,z1)
	ax.plot_wireframe(x_sph1,y_sph1,z_sph1)
	
	"""
	ax.plot(x2,y2,z2)
	ax.plot_wireframe(x_sph2,y_sph2,z_sph2)
	"""

	ax.set_xlim(x_limit[0],x_limit[1])
	ax.set_ylim(y_limit[0],y_limit[1])
	ax.set_zlim(z_limit[0],z_limit[1])


ani = animation.FuncAnimation(fig, animate, interval=100, blit=False, frames = 1000)

plt.show()





