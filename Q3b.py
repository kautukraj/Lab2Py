from Q3a import *

#Your code - begin
r = len(output)
c = len(output[0])
if c != r:
  print ("Transpose not possible")
else:
  output1 = [[0 for row in range(c)]for col in range(r)]

  for i in range (r):
      for j in range (c):
          output1[j][i] =  output[i][j]
          
  

print(output1)
# Your code - end

