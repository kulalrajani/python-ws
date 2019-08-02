'''Program to accept a number from the user and determine the sum of digits of that number'''
n = int(input("Enter a number:"))
sum = n 
while sum >= 10:
    sum = 0
    while not n == 0:
        r = n % 10
        sum = sum + r
        n = n // 10
    n = sum
print(f"sum of number:{sum}")
