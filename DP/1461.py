n, m = map(int,input().split(' '))
location = list(map(int,input().split(' ')))
n_location = []
minus = []
plus = []
answer = 0

if max(location) < abs(min(location)):
    location.sort(reverse=True)
else:
    location.sort()


print(location)

answer = abs(location.pop())
if(len(location)!=0):
    for i in range(1,m):
        location.pop()

while(len(location)!=0):
    print(location)
    if location[-1] < 0:
        location.sort(reverse=True)

    answer+=abs(location.pop())*2
    print(answer)
    print(location)

    for i in range(1,m):
        if len(location)!=0:
            location.pop()

print(answer)


