def to_dictionary(keys, values):
    return dict(zip(keys, values))


keys = ["byte", "kilobyte", "megabyte"]    
values = [1, 1024, 1048576]
print(to_dictionary(keys, values)) 
# {'byte': 1, 'kilobyte': 1024, 'megabyt': 1048576}





