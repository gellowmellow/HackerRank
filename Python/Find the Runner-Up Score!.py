#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n=int(5)
    arr=sorted(list(map(int, "2 3 6 6 5".split())),reverse=True)
    m=max(arr)

    for i in arr:
        if m>i:
            print(i)
            break