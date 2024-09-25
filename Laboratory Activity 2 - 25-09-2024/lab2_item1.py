
def is_palindrome(num):
    
    return str(num) == str(num)[::-1]

number = int(input("Enter an integer: "))

if is_palindrome(number):
    print("Palindrome")
else:
    print("Not a Palindrome")
