from math import factorial

# This function returns the value for a given position (n, k)
def PascalsTriangle(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# This function returns the Pascal's triangle graphically for n rows
def GraphicPascalsTriangle(p):
    # Rows counting start in zero (0), so n = 2 means 3 rows: 0, 1, 2
    for i in range(p + 1):
        # Columns counting start in zero (0), so 3 columns are counted: 0, 1, 2
        for j in range(0, i + 1):
            print(PascalsTriangle(i, j), end=" ")   # Avoiding a new line
        print(end = "\n")                           # Adding a new line at the en of the row

GraphicPascalsTriangle(3)
