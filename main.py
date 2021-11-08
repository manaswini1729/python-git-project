def is_palindrome(str):
    if str[::-1]==str:
        return True
    return False
str=input()
if is_palindrome(str)==True:
    print("palindrome")
else:
    print(" Not palindrome")