n = int(input())
rock = list(map(int,input().split()))
#[1, 4, 2, 2, 1]
s = int(input())


def dfs(li,V,visited):
    #현재 노드 방문 처리
    visited[V] = 1
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in li[V]:
        if visited[i] == 0:
            dfs(li,i,visited)

dfs_rock = [[]for i in range(n+1)]
visited = [0] * (n + 1)

for i in range(n):
    index= i+1
    if index+rock[i] < n+1:
        dfs_rock[index].append(index+rock[i])
    if index-rock[i]>0:
        dfs_rock[index].append(index - rock[i])


dfs(dfs_rock, s, visited)
print(visited.count(1))

