def ispalindrome(x):       
    y = x[::-1]  
    if x == y:
        return f"{x} is palindrome number."
    else:
        return f"{x} is not palindrome number."
number = input("enter your number :")
print(ispalindrome(number))
