# Program to parse File
#Find mean of one subject marks from one region
math_marks_A=[]
for line in open("student_record.txt"):
    fields=line.split(";")
    region_code=fields[0]
    region_code_stripped=region_code.strip()
    math_mark_str=fields[5]
    math_mark=float(math_mark_str)
    if region_code_stripped=="A":
        math_marks_A.append(math_mark)
mean=sum(math_marks_A)/len(math_marks_A)
print(mean)