list1 = [10 , 20 , 40 , 60 , 70 , 80]
list2 = [5 , 15 , 25 , 35 , 45 , 60]
a = list1 + list2
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]

print(a)