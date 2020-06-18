def simple_interest(p, r, t):
	'''
	Calculate simple interest given p, r, t
	'''
	return(p*r*t/100)

def compound_interest(principle, rate, time):
	'''
	Calculate compound interest
	'''
	result = principle * (pow((1 + rate / 100), time))
	return result
