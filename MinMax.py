# use min() / max
# step 1 input int
# step 2 insert int to list
# step 3 find min/max by function


def MinMax(dat):
    dat_min = min(dat)
    dat_max = max(dat)
    return dat_min, dat_max
# TODO main find min/max make def return value of min/max
# FIXME


dat_inp = []
while True:
    inp = int(input("Enter for sort number :"))
    if inp == 0:
        findMinMax = MinMax(dat_inp)
        print(
            f"Min of value : {findMinMax[0]} / Max of value : {findMinMax[1]}")
        break
    else:
        dat_inp.append(inp)
        inp = None
