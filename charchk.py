# TODO check charecter is Upper or Lower
# use string.istitle()


def chkTitle(s):
    return s.istitle()


if __name__ == "__main__":
    strInput = input("Enter String Check Upper/Lower: ")
    for i in strInput:
        print(f"Charecter {i} is Upper : {chkTitle(i)}")
