def isPrime(number):
	if (divAble(number, number -1) == False): return True
	else: return False
def divAble(original, start):
    for x in range(2, original):
        if (original % x == 0): return True
        
    return False

def divAbleRecursive(original, num):
	if (num >1):
		if ((original % num) == 0): return True        
		else:
			
			return divAble(original, num -1)
	else: 
         
         return False

def primeList(max):
    primeList = []

    for x in range((2), max // 2):
        if (isPrime(x) == True): 
            print(str(x) + " added to list of potential primes...")
            primeList.append(x)
            

    return primeList


def compute2(input):
    primeStart = input // 2
    for x in range(primeStart, 2, -1):
        if (isPrime(x) == True): 
            print ("Prime cadidate:" + str(x))
            if (input % x == 0):
                print ("Largest prime factor found:" + str(x))
                break

def compute(bigNumber):
    print("Initializing list of primes...")
    pList = primeList(bigNumber)

    print("List done, trying division...")


    for o in pList:
        
        if (bigNumber % o == 0): 
            print(str(bigNumber) + " divided by " + str(o) + " = 0")
            print ("Prime factor:" + str(o))
    print("EOF")


print(str(compute2(600851475143)))

