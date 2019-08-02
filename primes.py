'''a program to accept 2 different numbers from the user and
print all the prime numbers between these 2 numbers.'''
a = int(input("Enter lower bound:"))
b = int(input("Enter upper bound:"))
flag = 1
for i in range(a,b+1):
    if i >= 2:
        for j in range(2, (i // 2)+1):
            if i % j == 0:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            print(i, end=" ")
            