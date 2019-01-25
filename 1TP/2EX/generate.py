from random import randint
from random import choice

def write_points(filename, num_points, mini, maxi):
	f = open(filename, "w")
	f.write('X:Y:L\r\n')
	for i in range(num_points):
		f.write(str(randint(mini, maxi))+":"+str(randint(mini, maxi))+":"+choice(['R', 'D'])+'\r\n')
	f.close()
	
filename = "points.csv"
nbr_points = 200
mini = 1
maxi = 1000


write_points(filename, nbr_points, mini, maxi)
