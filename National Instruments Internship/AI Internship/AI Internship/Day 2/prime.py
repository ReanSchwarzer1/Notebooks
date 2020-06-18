def calc_prime(start, end):
	a = list()
	for val in range(start, end + 1): 
	    if val > 1: 
	        for n in range(2, val//2 + 2): 
	            if (val % n) == 0: 
	                break
	            else: 
	                if n == val//2 + 1: 
	                    a.append(val) 
	return(a)

print(calc_prime(1000, 2000))