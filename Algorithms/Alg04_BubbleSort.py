def BubbleSort(L:list) -> list:
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(L) - 1):
			if L[i] > L[i+1]:
				swapped = True
				(L[i], L[i+1]) = (L[i+1], L[i])
	return L