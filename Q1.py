from Q1input import *

# Your code - begin
output=[]
c=1
for i in range (len(inp)):
    if i == len(inp) - 1 :
        output.append([inp[i],c])
    elif inp[i]==inp[i+1] :
        c+=1
    else :
        output.append([inp[i],c])
        c=1
        
# Your code - end

for i in output:
    print(str(i[1])+i[0],end="")
