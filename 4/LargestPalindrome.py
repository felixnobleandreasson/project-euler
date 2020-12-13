def isPalindrome(num):
	numString = str(num)
	length = len(numString)
	first_half  = numString[0:length//2]
	second_half = numString[length//2 if length%2 == 0 else ((length//2)+1):]
	if (first_half == revString(second_half)):
		return True
	return False

def revString(s):
	return s[::-1]

def compute(factorDigits):
	largestFactor = int('9'*factorDigits)
	smallestFactor = int("1" + '0'*(factorDigits -1))
	print("Largest factor: " + str(largestFactor))
	print("Smallest factor: " + str(smallestFactor))
	for i in range(largestFactor, smallestFactor-1, -1):
		for j in range(largestFactor, i-1, -2):
			if (isPalindrome(i*j)):
				print("New largest palindrome: " +  str(i) + " * " + str(j) + " = " + str(i*j))
				return True

compute(3)

