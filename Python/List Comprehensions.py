#https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = 1#int(input())
    y = 1#int(input())
    z = 1#int(input())
    n = 2#int(input())
    
    print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n])