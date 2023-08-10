# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 04:23:36 2022

@author: mthak
"""

def isPalindrome(x: int) -> bool:
    x_str = str(x)
    var = int(len(x_str)/2)
    for i in range(var):
        if str(x%10) != x_str[i]:
            return False
        else:
            x = int(x/10)
    return True
x=1221
print (isPalindrome(x))


def isPalindrome_without_string(x: int) -> bool:
    x_str = str(x)
    num = 0
    if (x<0 & x%10 ==0):
        return False
    for i in range(int(len(x_str)/2)):
        num = (num*10) + (x%10)
        x=int(x/10)
        print("num = " + str(num))
        print("x = " + str(x))
    if (len(x_str)!=2) and (int(len(x_str))%2) == 1:
        x=int(x/10)
    if(num == x):
        return True
    else:
        return False
    
m = -10
print (isPalindrome_without_string(m))
        
        