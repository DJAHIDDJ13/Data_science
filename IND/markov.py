from numpy.random import choice
from re import match
from os import listdir

class Transition:
	def __init__(self, start):
		self.start = start
		self.total = 0
		self.weights = {}
	
	def add_weight(self, end):
		if end in self.weights.keys():
			self.weights[end] += 1
		else:
			self.weights[end] = 1
		
		self.total += 1
			
	def get_next(self):
		return choice(list(self.weights.keys()), 1, p=list(map(lambda x: x/self.total, self.weights.values())))[0]

class Markov_chain:
	def __init__(self, states, start):
		self.states = states
		self.transitions = {state:Transition(state) for state in self.states}
		self.current = start
		
	def add_transition(self, start, end):
		self.transitions[start].add_weight(end)

	def advance(self):
		self.current = self.transitions[self.current].get_next()
	
	def get_words(self, filename):
		words = []
		try:
			f = open(filename, "r", errors='replace')
			line = f.readline()
			while line:
				words += list(filter(lambda w: match(r'[a-z0-9\-\']+', w), [word.lower() for word in line.split()]))
				line = f.readline()
			f.close()
		except IOError:
			print(filename, ': Could not open file!')
			exit
		return words

	def train(self, filename):
		words = self.get_words(filename)
		self.transitions = {**self.transitions, **{state:Transition(state) for state in words if state not in self.states}}
		self.states += [words]
		for i in range(len(words) - 1):
			self.add_transition(words[i], words[i+1])

	def generate_text(self, length):
		text = [self.current]
		for i in range(length):
			self.advance()
			text.append(self.current)
		return ' '.join(text)

m = Markov_chain([], "the")
dir_name = './exclastxt/'
# ~ files = listdir(dir_name)
# ~ for filename in files:
m.train("tr.txt")
	# ~ print('Trained with:', filename)
print(m.generate_text(40))
