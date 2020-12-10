'''
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive.
Once all operations have been performed, return the maximum value in the array.
'''

n=5
queries=[[1,2,100],[2,5,100],[3,4,100]]

#init array of zeroes with length = n
arr=[0]*n

for query in queries:
    a=query[0]
    b=query[1]
    k=query[2]

    arr[a-1]+=k
    try:
        arr[b] -= k
    except:
        pass

prev=m=0
for i in range(len(arr)):
    prev+=arr[i]
    arr[i]=prev
    if prev>m:
        m=prev

print(m)
