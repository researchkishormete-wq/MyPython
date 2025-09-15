
# Program to
f=open("pendulum.txt")
pend=f.readlines()
print(type(pend))
#print(pend)
#Lines=pend.splitlines()
for line in pend:
    print(line)
f.close()