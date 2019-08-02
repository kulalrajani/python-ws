'''Program to print the Fibonacci series up to the number 34'''
f1 = 0
f2 = 1
f3 = 0
print(f1,f2,end =" ")
while not f3 == 34:
    f3 = f1 + f2
    print(f3, end =" ")
    f1 = f2
    f2 = f3
