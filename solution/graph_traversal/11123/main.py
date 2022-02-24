# Authored by : seonjoo0885
# Co-authored by : -
# Link : http://boj.kr/454a424a9e4d4469ab1af120a7141bb0

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '#' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return 1

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = []
    visited = [[0 for _ in range(m)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        graph.append(list(input()))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '#' and not visited[i][j]:
                cnt += bfs(i, j)
    print(cnt)
