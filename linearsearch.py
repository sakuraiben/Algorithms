def doLinearSearch(array, targetValue):
	for guess in range(0, len(array)):
		if(array[guess]==targetValue):
			return guess
	return -1

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
result = doLinearSearch(primes, )
print result