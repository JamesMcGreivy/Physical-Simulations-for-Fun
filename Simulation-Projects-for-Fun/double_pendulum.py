from mpl_toolkits.mplot3d import axes3d
import numpy as np 
from matplotlib import animation, cm, pyplot as plt

#origin
x0 , y0 = 0 , 0


#rod 1
m1 = 200
r1 = 8

theta1 = np.pi / 4

x1, y1, = r1*np.sin(theta1) , -r1*np.cos(theta1)

dtheta1 = 0
ddtheta1 = 0

#rod 2
m2 = 200
r2 = 8

theta2 = -np.pi / 8

x2, y2 = r2*np.sin(theta2) , -r2*np.cos(theta2)

dtheta2 = 2
ddtheta1 = 0

g = 9.81

def animate(i):
	global r1, x1, y1, theta1, dtheta1, ddtheta1, r2, x2, y2, theta2, dtheta2, ddtheta2
	
	dt = 0.018

	top = (-g*(2*m1 + m2)*np.sin(theta1))-(2*np.sin(theta1 - theta2)*m2*(r2*(dtheta2**2) + r1*np.cos(theta1 - theta2)*(dtheta1**2)))
	bot = (r1*(2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2)))
	ddtheta1 = top/bot

	dtheta1 = dtheta1 + ddtheta1*dt
	theta1 = theta1 + dtheta1*dt


	top = (2*np.sin(theta1 - theta2)*((r1*(m1+m2)*(dtheta1**2))+(g*(m1+m2)*np.cos(theta1)) + r2*m2*np.cos(theta1-theta2)*(dtheta2**2) ))
	bot = r2*(2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))
	ddtheta2 = top/bot

	dtheta2 = dtheta2 + ddtheta2*dt
	theta2 = theta2 + dtheta2*dt

	x1, y1, = r1*np.sin(theta1) , -r1*np.cos(theta1)
	x2, y2  = r2*np.sin(theta2) , -r2*np.cos(theta2)

	ax.clear()


	ax.plot([x0,x1], [y0,y1], c='b')
	ax.scatter(x1,y1, s=m1, c='b')

	ax.plot([x1,x1+x2], [y1, y1+y2], c='r')
	ax.scatter(x1+x2,y1+y2, s=m2, c='r')
	
	trail.scatter(x1,y1, c='b', s=0.1)
	trail.scatter(x1+x2,y1+y2, c='r', s=0.1)


	ax.set_xlim(x_limit[0],x_limit[1])	
	ax.set_ylim(y_limit[0],y_limit[1])
	trail.set_xlim(x_limit[0],x_limit[1])	
	trail.set_ylim(y_limit[0],y_limit[1])

	print("Succesfully Rendered Frame ", i)

fig = plt.figure()
ax = fig.add_subplot(111)
trail = fig.add_subplot(331)


x_limit = [-15,15]
y_limit = [-20,0]
ax.set_xlim(x_limit[0],x_limit[1])
ax.set_ylim(y_limit[0],y_limit[1])
trail.set_xlim(x_limit[0],x_limit[1])
trail.set_ylim(y_limit[0],y_limit[1])

ani = animation.FuncAnimation(fig, animate, interval=20, blit=False, frames = 1000)


plt.axis("off")



#ani.save('chaotic motion.gif', fps = 50)
plt.show()