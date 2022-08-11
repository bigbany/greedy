# 미로 탈출
# 동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 동빈이의 위치는 (1,1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이 때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작칸과 마지막 칸을 모두 포함해서 계산한다.

# 입력 조건
# 첫째 줄에 두 정수 N, M(4<=N, M <= 200)이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다. 각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.

# 출력 조건
# 첫째 줄에 최소 이동 칸의 개수를 출력한다.
#

from collections import deque


# 1. 입력


n,m = map(int,input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

print(graph)

# bfs 를 이용해보자
# 너비 중심의 탐색

# 입출력을 생각해보자 
# 입력, 출력 칸수를 세는 것

dx =[-1,1,0,0]
dy= [0,0,-1,1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
  # 어떻게 위치를 이동시킬까 ?
    x,y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y+ dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if graph[nx][ny]==0:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))
  return graph[n-1][m-1]

print(bfs(0,0))
        
      
    