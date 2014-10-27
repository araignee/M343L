import math

def main():
	p = int(input("Enter a prime number p: "))
	g = int(input("Enter a primitive root g: "))
	h = int(input("Enter a primitive root h: "))

	baby_list = []
	giant_list = []

	floor_p = math.floor(p**.5)
	for i in range(0, floor_p):
		baby_step = (g ** i) % p
		baby_list.append(baby_step)
	
	inverse = modinv(g**floor_p, p)
	for j in range(0, floor_p + 1):
		giant_step = h * (inverse**j) % p
		giant_list.append(giant_step)

	for x in baby_list:
		for y in giant_list:
			if x == y:
				value_1 = baby_list.index(x)
				value_2 = giant_list.index(y)
				#print(baby_list[value_1], giant_list[value_2])
				break

	final_power = (floor_p * (value_2)) + value_1
	print("x =", final_power)

def euclidian(a, b):
	x, y, u, v, = 0, 1, 1, 0
	while a != 0:
		q, r = b // a, b % a
		m, n = x - u * q, y - v * q
		b, a, x, y, u, v = a, r, u, v, m, n
	gcd = b
	return gcd, x, y ## ax + by = g = gcd(a, b)

def modinv(a, m):
	gcd, x, y = euclidian(a, m)
	if gcd != 1:
		return None
	else:
		return x % m	
	
main()
	
