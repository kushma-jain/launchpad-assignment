//reverseing the sentence
str_1 = input("Enter a string: ")
str_2 = ''

str_1 = str_1.lower()
str_1 = str_1.split()[::-1]
str_2 = ' '.join(str_1)
str_2 = str_2.capitalize()
print(str_2)