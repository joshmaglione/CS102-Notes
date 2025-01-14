def BinarySearch(L, x):
	low = 0
	high = len(L) - 1
	while low <= high:
		mid = (low + high)//2
		guess = L[mid]
		if x == guess:
			return mid
		if x < guess:
			high = mid - 1
		else:
			low = mid + 1
	return None