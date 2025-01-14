# As written in class
def SimpleSearch(L, x):
	for i in range(len(L)):
		if L[i] == x:
			return i
	return None


# A variation using "enumerate"
def SimpleSearch_v2(L, x):
	for i, guess in enumerate(L):
		if guess == x:
			return i
	return None