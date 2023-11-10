x = int(input("Please enter a five-digit integer number: "))

div, mod = divmod(x,10000)
A = div
B = mod // 1000
C = mod // 100 % 10
D = mod // 10 % 10
E = x % 10


ED = 10 * E + D
EDC = 10 * ED + C
EDCB = 10 * EDC + B
EDCBA = 10 * EDCB + A

print (EDCBA)