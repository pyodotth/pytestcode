# TODO sort number and charecter from input
# use "".join(sorted(val))


def sortChar(s):
    return "".join(sorted(s))


def sortNum(n):
    return "".join(sorted(n))


inpChar = input("Enter some text for sorted :")
inpNum = input("Enter some text for sorted :")
print(sortChar(inpChar.upper()))
print(sortNum(inpNum))
