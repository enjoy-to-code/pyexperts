import sys 

variable = 42
variable_i = int(42)
variable_f = float(42)
variable_s = str(42)

print(sys.getsizeof(variable))   # 28 bytes
print(sys.getsizeof(variable_i)) # 28 bytes
print(sys.getsizeof(variable_f)) # 24 bytes
print(sys.getsizeof(variable_s)) # 51 bytes



