#Assignment 1-->  sum of n numbers using while loop
sum1 = 0
while True:
    num1 = int(input("Enter the number"))
    sum1 = sum1 + num1
    print(sum1)
    if num1 == 0:
        break
print("Final sum is " , sum1)