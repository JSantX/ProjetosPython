a = int(input())
b = int(input())

for n in range(a, b+1):
    primo = True
    if n < 2:
        primo = False
    else:
        for i in range(2, n):
            if n % i == 0:
                primo = False
                break
    if primo:
        print(n)