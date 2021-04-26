def palindrome(a):
    return a == a[::-1]

print (palindrome('rotator')) # True
print (palindrome('rotators')) # False

