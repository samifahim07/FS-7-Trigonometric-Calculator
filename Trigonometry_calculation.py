import math

def sin_value(degree):
    return math.sin(math.radians(degree))

def cos_value(degree):
    return math.cos(math.radians(degree))

def tan_value(degree):
    return math.tan(math.radians(degree))

def cot_value(degree):
    return 1 / tan_value(degree)

def sec_value(degree):
    return 1 / cos_value(degree)

def cosec_value(degree):
    return 1 / sin_value(degree)

while True:
    print("\n----- FS-7 Trigonometric Calculator -----")
    print("1. Sin")
    print("2. Cos")
    print("3. Tan")
    print("4. Cot")
    print("5. Sec")
    print("6. Cosec")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 7:
        print("THANK YOU SO MUCH")
        break

    degree = float(input("Enter degree: "))

    if choice == 1:
        print("Sin value =", sin_value(degree))

    elif choice == 2:
        print("Cos value =", cos_value(degree))

    elif choice == 3:
        if degree == 90:
            print("Invalid")
        else:
            print("Tan value =", tan_value(degree))

    elif choice == 4:
        if degree == 0:
            print("Invalid")
        else:
            print("Cot value =", cot_value(degree))

    elif choice == 5:
        if degree == 90:
            print("Invalid")
        else:
            print("Sec value =", sec_value(degree))

    elif choice == 6:
        if degree == 0:
            print("Invalid")
        else:
            print("Cosec value =", cosec_value(degree))

    else:
        print("Invalid Choice")
