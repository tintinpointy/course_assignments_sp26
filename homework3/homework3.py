def say_goodbye(name):
	print("Goodbye", name)
name = "Eve"
say_goodbye(name)

def area_of_circ(radius):
	#Area of circle = pi * r^2
	# pi = 3.14
	print(radius * radius * 3.14)
radius = 9
area_of_circ(radius)

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

def what_should_I_wear(readings):
	min_and_max = (min(readings), max(readings))
	print(min_and_max)
readings = [3, 1, 5, 0, 9]
what_should_I_wear(readings)

def is_weekend(day):
	if (day - 6) % 7 == 0 or day % 7 == 0:
		return True
	else:
		return False

print(is_weekend(36))
print(is_weekend(20))

def fuel_efficiency(miles, gallons):
	return miles/gallons
miles = 300
gallons = 10
print(fuel_efficiency(miles, gallons))

def encryption(code):
	last_digit = code % 10
	rest_of_num = code // 10
	new_code = str(last_digit) + str(rest_of_num)
	return int(new_code)

code = 1035982
print(encryption(code))

def power(x, y):
	product = x
	for y in range (1,y):
		product = product * x
	return product

print(power(2,4))

def minimum(list):
	minimum = list[0]
	for i in list:
		if i < minimum:
			minimum = i
	return minimum

def maximum(list):
	maximum = list[0]
	for i in list:
		if i > maximum:
			maximum = i
	return maximum

list = [4, 2, 5, 7, 2, 3]
print(minimum(list))
print(maximum(list))

def new_max(list):
	maximum = list[0]
	i = 0
	while i < len(list):
		if list[i] > maximum:
			maximum = list[i]
		i += 1
	return maximum

def new_min(list):
	minimum = list[0]
	i = 0
	while i < len(list):
		if list[i] < minimum:
			minimum = list[i]
		i += 1
	return minimum

print(new_max(list))
print(new_min(list))

def summation(num):
	sum = 0
	while num > 0:
		dig = num % 10
		num = num // 10
		sum += dig
	return sum
print(summation(2468))

print(f"The result of the summation function, if you input 2568, is 20")