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
