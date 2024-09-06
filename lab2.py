'''
Owen Dunkel
9/6/24

Lab 2
'''

#This program calculates human age to dog age. 1 human age equals 7 dog age

human_age = float(input('Enter Human Age here '))
dog_age = (7 * human_age)
dog_age_year = dog_age // 1
dog_age_month = ((dog_age - dog_age_year) * 12) // 1
dog_age_day = ((((dog_age - dog_age_year) * 12) % 1) * 30) // 1


print('your age in dog years is: ' + str(dog_age_year) + ' years ' + str(dog_age_month) + ' months ' + str(dog_age_day) + ' days')

#This program calculates human age to cat age. 1 human age equals 9 cat age

cat_age = (human_age / 9)
cat_age_year = cat_age // 1
cat_age_month = ((cat_age - cat_age_year) * 12) // 1
cat_age_day = ((((cat_age - cat_age_year) * 12) % 1) * 30) // 1


print('your age in cat years is: ' + str(cat_age_year) + ' years ' + str(cat_age_month) + ' months ' + str(cat_age_day) + ' days')

#This program calculates human age to horse age

horse_age = 3 * ((((human_age ** 2) - 47) / 7) + 12)
horse_age_year = horse_age // 1
horse_age_month = ((horse_age - horse_age_year) * 12) // 1
horse_age_day = ((((horse_age - horse_age_year) * 12) % 1) * 30) // 1

print(' your age in cat years is: ' + str(horse_age_year) + ' years ' + str(horse_age_month) + ' months ' + str(horse_age_day) + ' days')



