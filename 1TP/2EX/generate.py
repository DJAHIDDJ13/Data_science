from random import randint
from random import choice

def write_points(filename, num_points, mini, maxi):
	f = open(filename, "w")
	f.write('X:Y:L\n')
	for i in range(num_points):
		f.write(str(randint(mini, maxi))+":"+str(randint(mini, maxi))+":"+choice(['R', 'D'])+'\n') # the choice function chooses randomly between 'R' and 'D' 50%/50%
	f.close()
	
filename = "points.csv" # output filename
nbr_points = 200 # num_points is the number of points generated
mini = 1 # mini is the minimum value of generated values
maxi = 1000 # the maximum


write_points(filename, nbr_points, mini, maxi)
