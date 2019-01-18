from random import randint

def write_points(filename, num_points, mini, maxi):
	f = open(filename, "w")
	f.write('R:D\r\n')
	for i in range(num_points):
		f.write(randint(mini, maxi)+":"+randint(mini, maxi)+'\r\n')
	f.close()

write_points("points.csv", 200, 1, 1000)

u_x = int(input("x = "))
u_y = int(input("y = "))

