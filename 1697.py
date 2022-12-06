from collections import deque

def bfs(x):
    count = 0
    q=deque()
    q.append(x)
    while q:
        x = q.popleft()
        x1,x2,x3 = x+1,x-1,x*2



n,k = map(int,input().split())
graph = [0]*(max(n,k)+1)
graph[n]=1

bfs(n)

print(graph)



