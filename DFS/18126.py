import sys
sys.setrecursionlimit(10**9)
n = int(input())

def dfs(list,v,visited):
    visited[v]=1
    for i in range(len(list[v])):
        togo = list[v][i][0]
        if visited[togo] == 0: #방문하지 않았으면
             dist[togo]=list[v][i][1]+dist[v]
             dfs(list,togo,visited)

list = [[]for i in range(n+1)]
visited = [0]*(n+1)
dist = [0]*(n+1)
for i in range(n-1):
    a,b,c = map(int,input().split())

    list[a].append([b,c])
    list[b].append([a,c])

dfs(list,1,visited)
print(max(dist))
