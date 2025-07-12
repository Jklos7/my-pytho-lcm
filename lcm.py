def lcm(a, b):
	max_num = max(a, b)
	while True:
		if max_num % a == 0 and max_num % b == 0:
			lcm = max_num
			break
		max_num += 1
	return lcm


if __name__ == "__main__":
	a = int(input("Enter your first number: "))
	b = int(input("Enter your second number: "))

	print(f"The LCM of {a} and {b} is {lcm(a, b)}")
