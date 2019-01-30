from exo2 import nearestPoints

##################
filename = "points.csv" # input filename
nbr_closest = 5 # number of point to get that are closest to input point
##################

u_x = int(input("x = "))
u_y = int(input("y = "))

nearestPoints(filename, [u_x, u_y], nbr_closest) # we can ommit nbr_closest because it takes the default value 5
