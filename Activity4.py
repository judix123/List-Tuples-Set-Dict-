def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter a number of term: "))
print("Fibonacci sequence")
for i in range(n):
    print(fibonacci(i), end= " ")