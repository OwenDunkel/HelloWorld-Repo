'''
Owen Dunkel
9/13/2024

Lab 4
'''

upper_bound = int(input("Enter an upper bound for a check: "))
print(f'Between 1 and {upper_bound} there are')

sum_proper_divisors = 0
count_abundant = 0
count_deficient = 0
count_perfect = 0

for x in range(1, upper_bound + 1):
	sum_proper_divisors = 0
	for number in range(1, x + 1):
		if(x % number == 0) and (x != number):
			sum_proper_divisors += number
	if(sum_proper_divisors > number):
		count_abundant += 1
	elif(sum_proper_divisors < number):
		count_deficient += 1
	elif(sum_proper_divisors == number):
		count_perfect += 1
	
print(f'{count_deficient} deficient numbers')
print(f'{count_perfect} perfect numbers')
print(f'{count_abundant} abundant numbers')
