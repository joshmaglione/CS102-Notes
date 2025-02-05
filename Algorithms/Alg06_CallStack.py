# We are assuming the code is filled in. 
#
def samp_mean(L:list) -> float:
	# CODE
	pass 

def std_dev(L:list) -> float:
	# CODE
	pass

def print_report(n:int, mu:float, sigma:float) -> None:
	# CODE
	pass

def stats_report(L:list) -> None:
	n = len(L)
	mu = samp_mean(L)
	sigma = std_dev(L)
	print_report(n, mu, sigma)