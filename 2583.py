from collections import deque

def bfs(y,x):
    d = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    count = 1
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < m and 0 <= nx < n:
                if graph[ny][nx] == 0:
                    q.append((ny, nx))
                    graph[ny][nx] = 2
                    count +=1

    return count


m,n,k = map(int,input().split(' '))
answer=[]
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    y1,x1,y2,x2= map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[i][j] = 1

for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            graph[i][j]=2
            answer.append(bfs(i,j))
answer.sort()
print(len(answer))
print(*answer)
