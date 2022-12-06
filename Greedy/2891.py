n,s,r = map(int,input().split())
broken_teams = list(map(int,input().split()))
more_teams = list(map(int,input().split()))
temp=[]
count = 0

for broken_team in broken_teams:
    if broken_team in more_teams:
        temp.append(broken_team)

for item in temp:
    broken_teams.remove(item)
    more_teams.remove(item)

temp=[]
temp_more=[]

for broken_team in broken_teams:
    up = broken_team+1
    down = broken_team-1

    if down in more_teams and up in more_teams and down not in temp_more and up not in temp_more:
        temp.append(broken_team)
        temp_more.append(down)
        continue
    if up in more_teams and up not in temp_more:
        temp.append(broken_team)
        temp_more.append(up)
        continue
    if down in more_teams and down not in temp_more:
        temp.append(broken_team)
        temp_more.append(down)
        continue

for item in temp:
    broken_teams.remove(item)

for item in temp_more:
    more_teams.remove(item)

print(len(broken_teams))

