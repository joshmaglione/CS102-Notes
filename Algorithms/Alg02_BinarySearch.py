def BinarySearch(L, x):
	low = 0							# low is first entry of snippet
	high = len(L) - 1				# high is last entry of snippet
	while low <= high:				# TRUE if we can further subdivide
		mid = (low + high)//2		# find midpoint
		guess = L[mid]				# a_i to compare with
		if x == guess:
			return mid
		if x < guess:
			high = mid - 1			# decrease large endpoint
		else:
			low = mid + 1			# increase small endpoint
	return None