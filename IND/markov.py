from numpy.random import choice

class Transition:
	def __init__(self, start):
		self.start = start
		self.total = 1
		self.weights = {start: 1}

	def add_weight(self, end):
		if end in self.weights.keys():
			self.weights[end] += 1
		else:
			self.weights[end] = 1
			
		self.total += 1
			
	def get_next(self):
		return choice(list(self.weights.keys()), list(self.weights.values()))

class Markov_chain:
	def __init__(self, states, start):
		self.states = states
		self.transitions = {state:Transition(state) for state in self.states}
		self.current = start
		
	def add_transition(self, start, end):
		self.transitions[start].add_weight(end)

	def advance(self):
		self.current = self.transitions[self.current].get_next()
		print('current: ', self.current)


m = Markov_chain(["one", "two", "three"], "one")
m.advance()
m.add_transition("one", "two")
m.advance()
