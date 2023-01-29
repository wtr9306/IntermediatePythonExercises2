import random
import time

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = random.randint(15, 35)
start_time = time.time()
result = fibonacci(n)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"The {n}th term of the Fibonacci sequence is: {result}")
print(f"Time taken: {elapsed_time} seconds")
