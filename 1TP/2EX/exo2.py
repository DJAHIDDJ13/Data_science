
def write_points(filename, num_points, mini, maxi):
	f = open(filename, "w")
	f.write('X:Y:L\n')
	for i in range(num_points):
		f.write(str(randint(mini, maxi))+":"+str(randint(mini, maxi))+":"+choice(['R', 'D'])+'\n')
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
	return (x1-x2)**2+(y1-y2)**2 # returns the distance between two points squared (omitted the sqrt to optimize the program since it's not needed)

def get_closest(x, y, filename, n):
	points = read_points(filename)
	if n > len(points)-1:
		return
	return sorted(points, key=lambda point: dist(x, y, point[0], point[1]))[:n] # sort the points by their distance from the u_x and u_y and then get the first n values 

##################
filename = "points.csv" # input filename
nbr_closest = 5 # number of point to get that are closest to input point
##################

u_x = int(input("x = "))
u_y = int(input("y = "))

points = read_points(filename)
closest = get_closest(u_x, u_y, filename, nbr_closest)
print(closest)
percR = sum([a[2] == 'R' for a in closest])/float(nbr_closest) # calculating the ratio of R's is closest by doing the sum of a[2] == 'R' which is equal to 1 if a[2] is equal to 'R' otherwise it's 0
percD = 1 - percR # 1 - the ratio of R's yields the ratio of D's
print('R:'+str(100*round(percR, 4))+'%/ D:'+str(100*round(percD, 4))+'%')  # print the rounded previously calculated values percR and percD
