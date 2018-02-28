
def printStar(max):
    for i in range(0, max):
        print(' '*(max-i-1) + '*'*(2*i+1))

printStar(8)
