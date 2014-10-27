import fractions
import math

def main():

	n = int(input("Enter integer n to be tested:"))
	a = int(input("Enter integer a as potential witness:"))

	gcd = fractions.gcd(a, n)
	if n % 2 == 0 or 1 < gcd < n:
		print("Composite")

	# write n-1 as 2**k * q
	# repeatedly try to divide n-1 by 2
	k = 0
	q = n-1
	while True:
		quotient, remainder = divmod(q, 2)
		if remainder == 1:
			break
		k += 1
		q = quotient
	assert(2**k * q == n-1)

	a = a**q % n
	if a == 1:
		print("Test fails")

	for j in range(k):
		if a % n == 1:
			print("Test fails")
		a = a**2 % n

	def try_composite(a):
		if pow(a, d, n) == 1:
			return False
		for i in range(s):
			if pow(a, 2**i * d, n) == n-1:
				return False
		return True # n is definitely composite

main()
