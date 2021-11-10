def is_palindrome(str):
    if str[::-1]==str:
        return True
    return False
str=input()
if is_palindrome(str)==True:
    print(" Given string is Palindrome")
else:
    print("Given String is not Palindrome")