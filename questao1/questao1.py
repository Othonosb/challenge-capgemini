n = int(input("digite um numero:"))

for i in range(0, n+1):
    print(" " * (n-i) + "*" * i)