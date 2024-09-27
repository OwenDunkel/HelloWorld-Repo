"""
Owen Dunkel
9/27/24

This program decodes an encoded word
"""


def main():
	
	encoded_word = "WBLARF8TTS"
	#encoded_word = "L8KAOUL"
	#encoded_word = "E8N8N8" 
	#encoded_word = "8TRA8DY T8LA"
	#encoded_word = "8TT LHA TILLTA LIMAS"	
	#encoded_word = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	#encoded_word = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	
	#encoded_word = "UUHO"  		#Used for Bonus
	#encoded_word = "EOUUUUOUU" 	#Used for Bonus
	
	print(DecodeWord(encoded_word))






def DecodeWord(encoded_word):
	decoded_word = ''
	#This loop replaces the letter with correct letter if it is wrong
	for letter in encoded_word:
		if letter == 'T':
			decoded_word += 'L'
		elif letter == 'L':
			decoded_word += 'T'
		elif letter == '8':
			decoded_word += 'A'
		elif letter == 'B':
			decoded_word += 'A'
		elif letter == 'A':
			decoded_word += 'E'
		elif letter == 'E':
			decoded_word += 'B'
		else:
			decoded_word += letter

	
	
	return decoded_word



#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()
