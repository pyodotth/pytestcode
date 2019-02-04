# TODO average 2 value
# Additional multi input


def avgValue(x, y):
    return (x+y)/2


def avgMultValue(arg):
    size = len(arg)
    return sum(arg)/size


if __name__ == "__main__":
    # x1 = int(input("Value of one :"))
    # x2 = int(input("Value of two :"))

    # print("Average of {} and {} is {}".format(x1, x2, avgValue(x1, x2)))
    multiInput = []
    while True:
        valEnter = int(input("Enter Number for find Average :"))
        if valEnter == 0:
            print(avgMultValue(multiInput))
            break
        else:
            multiInput.append(valEnter)
            # print(multiInput)
