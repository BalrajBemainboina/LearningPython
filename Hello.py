from array import *
vals = array('i',[5,3,7,13,343])
print(vals)
for e in range(len(vals)):
    if e == (len(vals)-1):
        vals[e] = int(None)
        break
    if e >= 2:
        vals[e] = vals[e + 1]
print (vals)
count = len(vals)
for e in range(0,len(vals)):
    count -= 1
    print (vals[count],end=" ")