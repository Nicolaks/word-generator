import os
import random



global alphabetDico
alphabetDico = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I",
 "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q",
 "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z" ,"z",
 "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", "!", ":", ";", "*", "%", "$", "^", "=",
  ")", "@", "-", "(", "#", "&", "{", "}", "?"]

# Create a while, with a top number, and check if the number
# is prime ans after put him in file.
def main():
	lettres = int(input("Un mot de combien de lettres ? "))
	cbMots = int(input("Combien de mots ?"))

	for i in range(0, cbMots):
		mots = ""
		for p in range(0, lettres):
			lettreHasard = alphabetDico[random.randrange(len(alphabetDico))]
			mots += lettreHasard
		word_file = open("words.txt", "a")
		word_file.write(mots + "\n")
		word_file.close()
		print(mots)

main()
