frase = input("Ingresa una frase: ")
print (frase)
print ()

vocales = list(filter(lambda c: c in "AEIOU", frase))
print(vocales)
