#Assignment No 2 --> take a integer nd fing prime or not
num1 = int(input("Enter the number"))
if num1 > 1:
    for i in range(2 , num1):
        if(num1 % i ) == 0:
            print("Number is not Prime")
            break
        else:
            print("Number is Prime")
            break
else:
    print("Number is not Prime")

