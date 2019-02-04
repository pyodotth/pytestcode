# TODO add 7 number from 9 number = 100
# try add each 2 value / no work
# try 100 - data = x / work
# find dou number x no repeat and remove it


data = [7, 8, 10, 13, 15, 19, 20, 23, 25]
# print(sum(data))
over100 = 100 - sum(data)
# print(over100)
found = False
for i in range(9):
    for j in range(9):
        if data[i]+data[j] == abs(over100):
            print("{} / {} ".format(data[i], data[j]))
            print(data[i], data[j])
            found = True
            break
    if found:
        data.remove(data[j])
        data.remove(data[i])
        print(data)
        break
