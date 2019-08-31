from Q1input import *

# Your code - begin
l=[]
c=1
output=""
for i in range (len(inp)):
    if i == len(inp) - 1 :
        l.append([inp[i],c])
    elif inp[i]==inp[i+1] :
        c+=1
    else :
        l.append([inp[i],c])
        c=1
for i in l:
    output = output + (str(i[1])+i[0])

print output
    
# Your code - end


