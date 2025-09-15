
# Program to parse File

student={'name':'Kishor',
         'age':10}
print(student)
student['height']=5.7
print(student)
if 'height' in student:
    print(student['height'])
for key,val in student.items():
    print(key,val)
