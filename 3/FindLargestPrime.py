# %%
def isPrime(number):
	if (dividable(number, number -1) == False): return True
	else: return False
def allPrimes(bigNumber):
	sqrt = math.ceil(math.sqrt(bigNumber))
	while (bigNumber % 2 == 0):
		bigNumber = bigNumber // 2
		print("2", end=" ")
	for i in range(3, sqrt, 2):
		if (bigNumber % i == 0 and isPrime(i)):
			bigNumber = bigNumber // i
			print(str(i), end=" ")
# %%
allPrimes(600851475143)