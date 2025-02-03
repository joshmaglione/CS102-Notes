def SelectionSort(L:list) -> list:
	L_sorted = []						# list we return
	while len(L) > 0:					# main loop
		current_min = L[0]				# adjust as we move through L
		for j in range(1, len(L)):		# find current actual minimum
			if current_min > L[j]:		# check if other entries are smaller
				current_min = L[j]		# if so, reassign current min
		L_sorted.append(current_min)	# insert current actual min at end
		L.remove(current_min)			# remove the current actual min from L
	return L_sorted

