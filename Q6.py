from Q6input import *

# Your code - begin
sum = sum(l)
len = len(l)
mean = sum / float(len)
l.sort()
if len % 2 !=0 :
    median = l[int((len+1) / 2)]
else:
    median = l[int((len/2 + (len/2+1)) / 2)]

# Your code - end
print (mean,median)
