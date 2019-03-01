import itertools

data  = [
	[1,2,3,4],
	[1,4],
	[2,3,4],
	[4],
	[2,3],
	[1,2]
]
n = max([max(d) for d in data])
freqs = [0 for i in range(n)]
inter = [[0 for i in range(n)] for i in range(n)]

for d in data:
	for j in d:
		freqs[j-1] += 1
	print(list(itertools.combinations(d, 2)))
	for comb in itertools.combinations(d, 2):
		inter[comb[0]-1][comb[1]-1] += 1
		inter[comb[1]-1][comb[0]-1] += 1

supp = 0.3
conf = 0.6
print(freqs)
for i in range(n):
	print(' '.join([str(s) for s in inter[i]]))

for i in range(n):
	for j in range(i, n):
		if inter[i][j]/float(n) > supp:
			try:
				if inter[i][j]/float(freqs[i]) > conf:
					print(i,'->', j, " support=", inter[i][j]/float(n), " confidence=", inter[i][j]/float(freqs[i]))

				if inter[i][j]/float(freqs[j]) > conf:
					print(j,'->', i, " support=", inter[i][j]/float(n), " confidence=", inter[i][j]/float(freqs[j]))
			except:
				continue
