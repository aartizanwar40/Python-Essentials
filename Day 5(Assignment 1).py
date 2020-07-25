def fun(num1):
    a = [0 for i in range(num1.count(0))]
    x = [i for i in num1 if i != 0]
    x.sort()
    x.extend(a)
    return(x)


print(fun([0 , 1 , 2 , 10 , 4 , 1 , 0 , 56 , 2 , 0 , 1 , 3 , 0 , 56 , 0 , 4]))
