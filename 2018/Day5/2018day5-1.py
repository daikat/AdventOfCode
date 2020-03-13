import numpy as np

with open( "2018day5.data" ) as file:
	polymer = np.array(list(file.read()))

	reactions = int(0)
	i = int(0)
	while i < (len(polymer)-1):
		print(len(polymer))
		if polymer[i].isupper() and polymer[i+1].islower():
			if polymer[i].lower() == polymer[i+1]:
				reaction = [i, i+1]
				polymer = np.delete(polymer, reaction)
				reactions += 1
				if i > 0:
					i -= 1
			else:
				i += 1
		elif polymer[i].islower() and polymer[i+1].isupper():
			if polymer[i].upper() == polymer[i+1]:
				reaction = [i, i+1]
				polymer = np.delete(polymer, reaction)
				reactions += 1
				if i > 0:
					i -= 1
			else:
				i += 1
		else:
			i += 1

np.savetxt('test.out', polymer, fmt='%.12000s', newline='')
print("polymer = ", polymer)
print("len(polymer) = ", len(polymer))
print("reactions = ", reactions)
