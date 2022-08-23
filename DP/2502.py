import sys
d,k = map(int,input().split())

count = [1,1]

for i in range(2,d):
    count.append(count[i - 1] + count[i - 2])

#print(count)
a = count[d-3]
b = count[d-2]

for i in range(1,k):
    for j in range(1,k):
        if a*i+b*j == k:
            print(i)
            print(j)
            sys.exit()