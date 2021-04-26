def has_duplicates(list):
    return len(list) != len(set(list))

x = [1,2,3,3,4,5,5,6,7]
y = [1,2,3,4,5]
print(has_duplicates(x)) # True
print(has_duplicates(y)) # False


