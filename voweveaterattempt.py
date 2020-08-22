userWord = input("please enter a word: ")
userWord = userWord.upper()
for letter in userWord:
    if (letter == 'A' or 'E' or 'I' or 'O' or 'U'):
        userWord.remove(letter)
        continue
print(userWord)