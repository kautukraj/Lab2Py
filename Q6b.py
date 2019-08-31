from Q6input import *

# Your code - begin
len = len(l)
l.sort()
if len % 2 !=0 :
    output = l[int((len+1) / 2)]
else:
    output = l[int((len/2 + (len/2+1)) / 2)]
    
print (output)
# Your code - end

