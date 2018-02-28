#!/usr/bin/env python3

def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[x]+L[x+1] for x in range(0, len(L)-1)] + [1]

g = triangles()

for i in range(0, 10):
    print(next(g))
