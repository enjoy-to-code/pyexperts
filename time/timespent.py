import time

def multiply(a, b):
    c = a * b
    time.sleep(2.4)
    print(c) 

start_time = time.time()
multiply(3, 56789)
end_time = time.time()
total_time = end_time - start_time
print('Finished in {} ms'.format(int(total_time * 1000)))


