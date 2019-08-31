from Q5input import *

# Your code - begin
len = len(l)
temp=[]
output=[]
k=0
p=n
for i in range(n):
    temp.append(l[i])
    
for i in range(len):
    if i<=n :
        output.append(l[p])
        p+=1
    else:
        output.append(temp[k])
        k+=1
print (output)        
# Your code - end


