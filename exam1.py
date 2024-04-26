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
