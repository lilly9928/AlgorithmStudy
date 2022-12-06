from collections import deque

def dfs(list,v,visited):
    visited[v] = True
    print(v , end=' ')

    for i in list[v]:
        if visited[i]==False:
            dfs(list,i,visited)

def bfs(list,v,visited):
    deq = deque([v])
    visited[v]= False

    
n,m,v = map(int,input().split())

list = [[] for i in range(n+1)]

for i in range(m):
    x1,x2 = map(int,input().split())
    list[x1].append(x2)
    list[x2].append(x1)

visited = [False]*(n+1)

for i in range(1,n+1):
    list[i].sort()

dfs(list,v,visited)
