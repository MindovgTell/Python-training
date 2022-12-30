
a = int(input( ))
b = input()
c = int(input())
def her(a,b,c):
    if b == '+':
        return a + c
    if b == '*':
        return a * c
    if b == '-':
        return a - c
    if b == '/':
        return a / c
print(her(a,b,c))