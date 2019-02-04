# FIXME re code loop to def
a = int(input("your point in 30:"))
b = int(input("your point in 30:"))
c = int(input("your point in 40:"))

# print(chk_grade_compare(a+b+c))

start = 49
point = 5
grade = ["D", "D+", "C", "C+", "B", "B+", "A"]
for i in range(8):
    if start <= (a+b+c) <= start+point:
        print("Your grade is : {}".format(grade[i]))
        break
    elif (a+b+c) < start+1:
        print("Your grade is : F")
        break
    else:
        start += point
