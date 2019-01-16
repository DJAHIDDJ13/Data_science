
def write_points(filename, num_points, mini, maxi):
	f = open(filename, "w")
	f.write('X:Y:L\r\n')
	for i in range(num_points):
		f.write(str(randint(mini, maxi))+":"+str(randint(mini, maxi))+":"+choice(['R', 'D'])+'\r\n')
	f.close()

def read_points(filename):
	points = []
	f = open(filename, "r")
	f.readline() # ignore first line
	line = f.readline()
	while line:
		spl = line.split(':')
		points.append([int(spl[0]), int(spl[1]), spl[2][:-1]])
		line = f.readline()
	f.close()
	return points
	
def dist(x1, y1, x2, y2):
	return (x1-x2)**2+(y1-y2)**2

def get_closest(x, y, filename, n):
	points = read_points(filename)
	if n > len(points)-1:
		return
	return sorted(points, key=lambda point: dist(x, y, point[0], point[1]))[:n]

##################
filename = "points.csv"
nbr_closest = 5
##################

u_x = int(input("x = "))
u_y = int(input("y = "))

points = read_points(filename)
closest = get_closest(u_x, u_y, filename, nbr_closest)
print(closest)
percR = sum([a[2] == 'R' for a in closest])/nbr_closest
percD = 1 - percR
print('R:'+str(100*round(percR, 4))+'%/ D:'+str(100*round(percD, 4))+'%')
