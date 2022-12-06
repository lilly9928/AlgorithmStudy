x = list(input().upper())

list = dict()

for i in x:
    if i in list:
        list[i] += 1
    else:
        list[i] = 1

if len([k for k,v in list.items() if max(list.values()) == v]) > 1:
    print('?')
    exit()


print(max(list,key=list.get))

