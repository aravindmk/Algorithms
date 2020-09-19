## Selection sort/Assertion sort

s=eval(input()) #Taking the unsorted list as input from user
for i in range(len(s)):
    a=i
    for j in range(i+1,len(s)):
        if s[j]<s[a]:   #Checking if the number is less than every number succeeding it
            a=j
    s[i],s[a]=s[a],s[i]
print(s)
