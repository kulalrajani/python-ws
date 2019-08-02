'''Program to accept a number from the user; then display the reverse of the entered number.'''
n = int(input("Enter a number:"))
temp = n
rev = 0
while not n == 0:
    r = n % 10
    rev = (rev * 10) + r
    n = n // 10
print(f"Reverse of {temp} is {rev}")    
