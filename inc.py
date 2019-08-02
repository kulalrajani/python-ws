'''program to accept a five-digit number, increment each digit by 1'''
num = int(input("Enter a five digit number:"))
temp = num
rev = 0
s = 0
while not temp == 0:
    r = temp % 10
    rev = (rev * 10) + r
    temp = temp // 10  
    
while not rev == 0:
    r = rev % 10
    if r == 9 or r == 0:
        r = 0
    else:
        r = r + 1
    s = (s * 10) + r
    rev = rev // 10
print(f"Incremented value of {num} is {s}")
