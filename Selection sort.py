## Selection sort/Assertion sort

lst=eval(input()) #Taking the unsorted list as input from user
for i in range(len(lst)):
    a=i #Temporarily storing the index of the number in a variable
    for j in range(i+1,len(lst)):
        if lst[j]<lst[a]:   #Checking if the number is less than every number succeeding it
            a=j
    lst[i],lst[a]=lst[a],lst[i]
print(lst)
