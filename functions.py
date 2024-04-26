def split_names(fname,lname):
    split = fname+lname
    print(split)

split_names("David","Majoros")


def is_palindrome():
    string=input("Enter a string:")
    if(string==string[::-1]):
        print("True")
    else:
        print("False")

is_palindrome()

def build_list():
    string=input("Zadaj string: ")
    count=int(input("Zadaj count: "))
    multiple=(string+",")*count
    my_list=[multiple]
    print(my_list)

build_list()
