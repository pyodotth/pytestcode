# TODO move Ball mode A (1 to 2) B (2 to 3) C (3 to 1)
# Input Mode A/B/C and find ball position


def findBall(s):
    last_position = 0
    for i in s:
        if i in "A" and last_position == 0:
            last_position += 1
        elif i in "A" and last_position == 1:
            last_position -= 1
        if i in "B" and last_position == 1:
            last_position += 1
        elif i in "B" and last_position == 2:
            last_position -= 1
        if i in "C" and last_position == 2:
            last_position -= 2
        elif i in "C" and last_position == 0:
            last_position += 2
    print(last_position)


ballMove = input("Enter mode ball move A/B/C :")
findBall(ballMove.upper())
