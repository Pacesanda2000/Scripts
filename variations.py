whatever=input("Napis barsjaky string: ")

lowercase_whatever=whatever.lower()
uppercase_whatever=whatever.upper()
titlecase_whatever=whatever.title()
capitalizedcase_whatever=whatever.capitalize()

x=whatever.split()
y=[word.lower() for word in whatever.split()]
y.sort()
f_word=y[0]
l_word=y[-1]

print(lowercase_whatever)
print(uppercase_whatever)
print(titlecase_whatever)
print(capitalizedcase_whatever)

print(x)
print(y)
print(f_word , l_word)
