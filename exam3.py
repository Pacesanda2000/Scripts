def is_palindrome():
    string=input("Enter a string: ")
    if(string==string[::-1]):
        print("True")
    else:
        print("False")

is_palindrome()
