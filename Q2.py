from Q2input import *

# Your code - begin
left=['(', '{', '[']
right=[')', '}', ']']
stack=[]

for ch in inp:
    if ch in left:
        stack.append(ch)
    elif ch in right:
        pos = right.index(ch)
        if (len(stack))>0 and (left[pos] == stack[len(stack)-1]):
            stack.pop()

    else:
        output = False
if len(stack)==0:
    output = True

print (output)

# Your code - end

