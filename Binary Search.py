# Binary Search

lst=eval(input())
lst.sort()
n=int(input())
beg=0
end=len(lst)-1
while beg<=end:
    mid=(beg+end)//2
    if lst[mid]==n:
        print("Found at position : ",mid+1)
        break
    elif lst[mid]<n:
        beg=mid+1
    else:
        end=mid-1
else:
    print("Not Found")
