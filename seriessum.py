'''Program to accept a number “n” from the user; then display the sum of the following series:
1/2^3 + 1/3^3 + 1/4^3 + …… + 1/n^3'''
n = int(input("Enter the value for n:"))
sum = 0
for i in range(2,n+1):
    sum += 1/(i ** 3)
print(f"Total sum is:{sum}")    
