#ASSIGNMENT NO 1:----
# list1 = [1 ,2, 3, 4, 5, 6, 7,8]
#list2 = ["a" , "b" ,"c" , "d" , "e"]
#convert to a dictionary in one line code using list comprehension(without using zip method)

list1 = [1 ,2, 3, 4, 5, 6, 7,8]
list2 = ["a" , "b" ,"c" , "d" , "e"]
leng1 = min(len(list1) , len(list2))

d1 =  {list1[each] : list2[each] for each in range(leng1)}
print(d1)

