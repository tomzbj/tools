import math

pi = math.pi
print("Input initial z:", end=" ")
z = complex(input())
print("Input frequency:", end=" ")
f = float(input())

while True:
    comp_type = ""
    conn = ""
    exponent = 1
    while True:
        exponent = 1 
        print("New component:", end=" ")
        str = input()
        arr = str.split()
        if len(arr) != 2:
            print("Illegal Input!1")
            continue
        comp, conn = arr
        if comp[-1].upper() == "H":
            comp_type = "L"
        elif comp[-1].upper() == "F":
            comp_type = "C"
        elif comp[-1].upper() == "R":
            comp_type = "R" 
        comp = comp[:-1]

        if comp[-1].isalpha():
            if comp[-1] == "p":
                exponent = 1e-12
            elif comp[-1] == "n":
                exponent = 1e-9
            elif comp[-1] == "u":
                exponent = 1e-6
            elif comp[-1] == "m":
                exponent = 1e-3
            elif comp[-1].upper() == "K":
                exponent = 1e3
            elif comp[-1] == "M":
                exponent = 1e6
            elif comp[-1] == "G":
                exponent = 1e9
            elif comp[-1] == "T":
                exponent = 1e12

            comp = comp[:-1]

        try:
            val = float(comp)
        except ValueError:
            print("Illegal Input!2")
            continue
        comps = ["R", "L", "C"]
        if not (comp_type in comps):
            print("Illegal Input!3")
            continue
        conn = conn.upper()
        conns = ["S", "P"]
        if not (conn in conns):
            print("Illegal Input!4")
            continue
        break 
    if comp_type == "R":
        z2 = val * exponent
    elif comp_type == "L":
        z2 = 2 * pi * f * val * 1j * exponent
    elif comp_type == "C":
        z2 = 1 / (2 * pi * f * val * 1j * exponent)


    if conn == "S":
        z = z + z2
    elif conn == "P":
        z = 1 / (1 / z + 1 / z2)

    print("Z={:,.2f}".format(z)) 
