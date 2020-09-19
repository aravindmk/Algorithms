#Bubble sort

lst=eval(input())
n=len(lst)
for i in range(n):
    for j in range(n-1,i,-1):
        if lst[j-1]>lst[j]:
            lst[j],lst[j-1]=lst[j-1],lst[j]
print(lst)
