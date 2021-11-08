import math 
num = int(input())
root = math.sqrt(num)
if int(root) ** 2 == num:
    print( 'perfect square')
else:
    print('not a perfect square')
