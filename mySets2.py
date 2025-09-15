student={'name','Kishor',
         'age',10}
a=set([9,0])
print(student|a)
if a.issuperset(student):
    print('yes')
else:
        print('no')
if a<student:
    print('yes')
else:
    print('no')