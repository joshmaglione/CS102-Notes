# We assume that n is a non-negative integer throughout

# Definition 1: non-recursive
def factorial1(n):
	f = 1
	for i in range(1, n + 1):
		f *= i					# f = f * i
	return f

# x += 1		MEANS 		x = x + 1

# Definition 2: recursive
def factorial2(n:int) -> int:
	if n == 0:						# base case
		return 1
	return n * factorial2(n - 1)	# recursion