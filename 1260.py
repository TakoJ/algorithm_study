# 백준 1260번 문제
visited = []


def dfs(graph, v, check):
    visited.append(v)
    check[v] = 1
    for i in range(1, n+1):
        if check[i] == 1 or graph[v][i] == 0:
            continue

        # check == 0 이고 graph == 1일경우에만 재귀.
        dfs(graph, i, check)

    return visited


def bfs(graph, v):
    check = [0] * (n + 1)
    queue = [v]
    visited = [v]
    check[v] = 1

    while queue:
        current = queue.pop(0)
        for i in range(1, n+1):
            if graph[current][i] == 1 and check[i] == 0:
                visited.append(i)
                check[i] = 1
                queue.append(i)
    return visited


n, m, v = map(int, input().split())

def main():
    graph = [[0 for x in range(n+1)]for x in range(n+1)]
    check = [0] * (n + 1)
    for i in range(m):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    for i in dfs(graph, v, check):
        print(i, end=' ')
    print("")
    for j in bfs(graph, v):
        print(j, end=' ')

main()