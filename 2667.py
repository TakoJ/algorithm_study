
def main():
    n = int(input())
    check = [[0 for x in range(n)] for x in range(n)]
    map = []
    stack = []
    village = []
    cnt = 0
    for i in range(n):
        map.append(input())

    for i in range(n):
        for j in range(n):
            if map[i][j] == '1' and check[i][j] == 0:
                check[i][j] = 1
                cnt += 1
                stack.append([i, j])
                while stack:
                    current = stack.pop()

                    current_i = current[0]
                    current_j = current[1]

                    # 좌
                    if current_j != 0:
                        if map[current_i][current_j-1] == '1' and check[current_i][current_j-1] == 0:
                            stack.append([current_i, current_j-1])
                            check[current_i][current_j-1] = 1
                            cnt += 1
                    # 우
                    if current_j < n-1:
                        if map[current_i][current_j+1] == '1' and check[current_i][current_j+1] == 0:
                            stack.append([current_i, current_j+1])
                            check[current_i][current_j+1] = 1
                            cnt += 1

                    # 상
                    if current_i != 0:
                        if map[current_i - 1][current_j] == '1' and check[current_i - 1][current_j] == 0:
                            stack.append([current_i - 1, current_j])
                            check[current_i-1][current_j] = 1
                            cnt += 1

                    # 하
                    if current_i < n-1:
                        if map[current_i+1][current_j] == '1' and check[current_i+1][current_j] == 0:
                            stack.append([current_i+1, current_j])
                            check[current_i+1][current_j] = 1
                            cnt += 1

                village.append(cnt)
                cnt = 0

    print(len(village))
    for i in sorted(village):
        print(i)


if __name__ == "__main__":
    main()
