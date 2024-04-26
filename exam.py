def filterUppercase(list):
    return [i for i in list if any(o.isupper() for o in i)]

list = []
while True:
    daco = input("Zadaj string (alebo 'end' pre ukoncenie): ")
    if daco == 'end':
        break
    list.append(daco)

my_new_list= filterUppercase(list)
print(my_new_list)



def parseStringWithoutVowel(daco):
    samohlasky = ['a', 'e', 'i', 'o', 'u', 'y']
    list = []
    for i in daco:
        if i.lower() not in samohlasky:
            list.append(i)
    return list

daco = "Hello There!"
list = parseStringWithoutVowel(daco)
print(list)



def is_palindrome():
    string=input("Enter a string: ")
    if(string==string[::-1]):
        print("True")
    else:
        print("False")

is_palindrome()
