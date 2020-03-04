import matplotlib.pyplot as plt
import matplotlib.cm as cm

#This takes forever to render

def in_set(a,b):

	c = a + 1j * b
	z = 0
	n=0
	while n<100:
		
		if abs(z) > 2:
			return 1-(n/100)
		
		z = z**2 + c
		n += 1
	print("Got point!")
	return 1-(n/100)


colors = []
x_points = []
y_points = []

def get_points():
	
	x = -2.0
	while x <= 2.0:
		y = -2.0

		while y <= 2.0:
			n = in_set(x,y)

			x_points.append(x)
			y_points.append(y)
			colors.append(cm.winter(n))


			y += 0.005
		x += 0.005

	return x_points , y_points

x, y = get_points()
plt.scatter(x_points,y_points, s = 0.01, color = colors)

plt.axis('off')
plt.show()

