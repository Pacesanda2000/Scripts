name    = input("Tvoje meno: ")
surname = input("Tvoje priezvisko: ")

username=name[0] + surname[0:6]
email=((name) + "." + (surname) + "@example.com")
reversed=((name)[::-1] + " " + (surname)[::-1])
lenght_name=len(name)
lenght_surname=len(surname)

print(email)
print(reversed)
print(username)
print(f"Dlzka mena je: {lenght_name}")
print(f"Dlzka priezviska je: {lenght_surname}")
