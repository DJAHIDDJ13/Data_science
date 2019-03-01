import numpy as np
import random
import pprint

print = pprint.pprint

class Classifier:
	def __init__(self):
		self.means = {'male': [0, 0], 'female':[0,0]}
		self.variances = {'male': [0, 0], 'female':[0,0]}
		self.male = 1.0
		self.female = 0.0
		
	def train(self, data):
		self.male = sum([data[i][0] for i in range(len(data))])/len(data)
		self.female = 1 - self.male
		
		self.means['male'][0] = np.mean([data[i][1] for i in range(len(data)) if data[i][0] == 1])
		self.means['male'][1] = np.mean([data[i][2] for i in range(len(data)) if data[i][0] == 1])
		self.means['female'][0] = np.mean([data[i][1] for i in range(len(data)) if data[i][0] == 0])
		self.means['female'][1] = np.mean([data[i][2] for i in range(len(data)) if data[i][0] == 0])

		self.variances['male'][0] = np.var([data[i][1] for i in range(len(data)) if data[i][0] == 1])
		self.variances['male'][1] = np.var([data[i][2] for i in range(len(data)) if data[i][0] == 1])
		self.variances['female'][0] = np.var([data[i][1] for i in range(len(data)) if data[i][0] == 0])
		self.variances['female'][1] = np.var([data[i][2] for i in range(len(data)) if data[i][0] == 0])
		print(self.means)
		print(self.variances)
		
	def calc_prob(self, g, v, test_value):
		c1 = np.sqrt(2*np.pi*(self.variances[g][v]**2))
		c1 = 1/c1

		c2 = -1*((test_value-self.means[g][v])**2)
		c3 = (2*(self.variances[g][v]**2))
		
		return c1*np.exp(c2/c3)

	def classify(self, d):
		pmale = self.male*self.calc_prob('male', 0, d[1])*self.calc_prob('male', 1, d[1])
		pfemale = self.female*self.calc_prob('female', 0, d[1])*self.calc_prob('female', 1, d[1])
		evidence = pmale+pfemale
		
		return pmale/evidence > pfemale/evidence
	
	def test(self, t_data):
		accuracy = 0
		for d in t_data:
			accuracy += self.classify(d) == d[0]
		return accuracy / len(t_data)

def getdata(filename):
	# getting the data
	data = []
	f = open(filename, "r")
	line = f.readline() # ignore first line
	line = f.readline()
	while line:
		d = line.split(',')
		d[0] = 1 if len(d[0]) == 6 else 0
		d[1] = float(d[1])
		d[2] = float(d[2])
		
		data.append(d)
		line = f.readline()
	
	# splitting the data into test data and training data
	p = 1
	test_data = []
	train_data = []
	for i in range(len(data)):
		if random.uniform(0,1) < p:
			test_data.append(data[i])
		else:
			train_data.append(data[i])
	
	return (train_data, test_data)


test, train = getdata('GENDER.csv')

c = Classifier()
c.train(train)

print(c.test(train))
