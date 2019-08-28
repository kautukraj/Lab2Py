from Q3input import *

#Your code - begin
r1 = len(m1)
c1 = len(m1[0])
r2 = len(m2)
c2 = len(m2[0])
if c1 != r2:
  print ("Multiplication not possible")

output = [[0 for row in range(c2)]for col in range(r1)]

for i in range(r1):
  for j in range(c2):
    for k in range(c1):
       output[i][j] += m1[i][k] * m2[k][j]


# Your code - end
print(output)
