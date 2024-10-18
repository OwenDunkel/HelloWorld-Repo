"""
Owen Dunkel

Lab 7
Functions and List review
"""




#Problem 1

def calc_toll(hour, is_morning, is_weekend):
	toll_fee = 0
	if is_weekend == True:
		if is_morning == True and hour == 12 or hour < 7:
			toll_fee = 1.05
		elif is_morning == True and 7 <= hour < 12:
			toll_fee = 2.15
		elif is_morning == False and hour == 12 or hour < 8:
			toll_fee = 2.15
		elif is_morning == False and 8 <= hour < 12:
			toll_fee = 1.10
	elif is_weekend == False:
		if is_morning == True and hour == 12 or hour < 7:
			toll_fee = 1.15
		elif is_morning == True and 7 <= hour < 10:
			toll_fee = 2.95
		elif is_morning == True and 10 <= hour < 12:
			toll_fee = 1.90
		elif is_morning == False and hour == 12 or hour < 3:
			toll_fee = 1.90
		elif is_morning == False and 3 <= hour < 8:
			toll_fee = 3.95
		elif is_morning == False and 8 <= hour < 12:
			toll_fee = 1.40
	return(print(f'${float(toll_fee):.2f}'))
				
		

calc_toll(12, True, False)


#Problem 2

def GCD(num1, num2):
	while num2:
		num1, num2 = num2, num1 % num2
	return(num1)
	
def LCM(num1, num2):
	lcm = (num1 * num2) // GCD(num1, num2)
	return(lcm)


		

#Problem 3


def factorial(num1):
	result = 1
	for num in range(1, num1 + 1):
		result *= num
	return(result)
	


def combination(i, j):
	numerator = factorial(i)
	denominator = factorial(j) * factorial(i - j)
	answer = numerator / denominator
	return(answer)
	
	
	
	



if __name__ == '__main__':
	#print(calc_toll(8, True, False))  #answer 2.95
	#print(calc_toll(1, False, False)) #answer 1.9
	#print(calc_toll(3, False, True))  #answer 2.15
	#print(calc_toll(5, True, True))   #answer 1.05



	#Uncomment this when working on Problem 2
	
	if LCM(10,25) == 50:
		print("LCM(10,25) is correct")
	else:
		print(f"LCM(10,25) is incorrect.  You got {LCM(10,25)}, but the correct answer should be 50.")
	if LCM(90,342) == 1710:
		print("LCM(90,342) is correct")
	else:
		print(f"LCM(90,342) is incorrect. You got {LCM(90,342)}, but the correct answer should be 1710.")
	if LCM(45,240) == 720:
		print("LCM(45,240) is correct")
	else:
		print(f"LCM(45,240) is incorrect.  You got {LCM(45,240)}, but the correct answer should be 720.")



	#Uncomment this when working on Problem 3
	
for i in range(10):
	for j in range(i+1):
		print((combination(i,j)), end=' ')
	print()







