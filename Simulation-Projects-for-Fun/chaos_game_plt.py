import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider
from math import * 
import random
# 1000,1000 grid
width = 1000
height = 1000

attractors = [[0,0],[width,0],[width/2,height]]


jump = 0.5
resolution = 100000

x_pts = []
y_pts = []

ax = plt.subplots()

def get_next_point(x,y,attractor_x,attractor_y):

	distance_x = (attractor_x - x)
	distance_y = (attractor_y - y)

	move_x = distance_x * jump
	move_y = distance_y * jump

	return x + move_x, y + move_y



def plot_points(): 
	
	attractor = attractors[1]
	x = width/2
	y = height/2

	for i in range(resolution):

		x_pts.append(x)
		y_pts.append(y)


		x , y = get_next_point(x,y,attractor[0],attractor[1])

		next = int((random.random()*100/10 % len(attractors)))
		attractor = attractors[next]

def show_plot():
	plt.scatter(x_pts,y_pts,  s = 0.5)
	plt.axis('off')
	plt.show()




plot_points()
show_plot()