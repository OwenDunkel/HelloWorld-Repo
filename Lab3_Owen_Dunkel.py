'''
Owen Dunkel
9/13/2024

Lab 4
'''

income = int(input('Enter the amount of income you earned in 2023: '))
marital_status = input('married or single: ')

if marital_status == 'single' and (0 < income < 11001):
	print('taxed owed: ' + str(income * 0.1))
elif marital_status == 'single' and (11000 < income < 44726):
	print('taxed owed: ' + str((11000 * 0.1) + ((income - 11000)*.12)))
elif marital_status == 'single' and (44725 < income < 95376):
	print('taxed owed: ' + str((11000 * 0.1) + (33725 * .12) + ((income - 44725)*.22)))
elif marital_status == 'married' and (0 < income < 22001):
	print('taxed owed: ' + str(income * 0.1))
elif marital_status == 'married' and (22000 < income < 89451):
	print('taxed owed: ' + str((22000 * 0.1) + ((income - 22000) * .12)))
elif marital_status == 'married' and (89450 < income < 190751):
	print('taxed owed: ' + str((22000 * 0.1) + (67450 * .12) + ((income - 89450) * .22)))
elif marital_status == 'single' and (income > 95375):
	print('income is too high to be calculated')
elif marital_status == 'married' and (income > 190750):
	print('income is too high to be calculated')
else:
	print('invalid')
