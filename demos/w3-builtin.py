ord = input("Enter a word: ")
for letter in word:
  if ord(letter) >= 97and ord(letter) <= 122:
    print(chr(ord(letter)-32))
  else:print(letter)