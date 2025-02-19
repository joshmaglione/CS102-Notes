# Slightly fancy
def BubbleSort(L:list) -> list:
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(L) - 1):
			if L[i] > L[i + 1]:
				swapped = True
				(L[i], L[i + 1]) = (L[i + 1], L[i])
	return L


# Bare-bones
def BubbleSort_bare(L:list) -> list:
    n = len(L)
    for i in range(n):
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                (L[j], L[j + 1]) = (L[j + 1], L[j])
    return L