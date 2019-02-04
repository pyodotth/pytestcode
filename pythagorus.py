# TODO formula is C^2 = A^2 + B^2
# No need import anything


def pythagorus(a, b):
    return a**2 + b**2


if __name__ == "__main__":
    sideA = int(input("Enter side A of Triangle :"))
    sideB = int(input("Enter side B of Triangle :"))

    print(f"Pythagorus of {sideA} and {sideB} is {pythagorus(sideA,sideB)}")
