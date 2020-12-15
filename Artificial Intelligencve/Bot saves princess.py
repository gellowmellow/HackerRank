#https://www.hackerrank.com/challenges/saveprincess

import math

def displayPathtoPrincess(n,grid):
    if grid[0][0]=="p":
        py,px=0,0
    elif grid[0][n-1]=="p":
        py,px=0,n-1
    elif grid[n-1][0]=="p":
        py,px=n-1,0
    else:
        py=px=n-1
        
    bx=by=math.floor(n/2)
    
    if bx>px:
        print("\n".join(["LEFT" for x in range(bx-px)]))
    else:
        print("\n".join(["RIGHT" for x in range(px-bx)]))

    if by>py:
        print("\n".join(["UP" for x in range(by-py)]))
    else:
        print("\n".join(["DOWN" for x in range(py-by)]))

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)