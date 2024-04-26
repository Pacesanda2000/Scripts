Users = {}

n = input("Zadaj MENO: ")
a = int(input("Zadaj VEK: "))
g = input("Zadaj POHLAVIE: ")
l = input("Zadaj lokaciu: ")

Users = {
  n : {
    "age" : a,
    "gender" : g,
    "location" : l
  }
}

print(Users[n]["age"])
