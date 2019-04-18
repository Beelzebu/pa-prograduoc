word = input("Por favor ingresa una palabra: ")
wordl = list(word)
while len(wordl) != 0:
    deleted = wordl[0]
    print(wordl[0])
    wordl.remove(deleted)
