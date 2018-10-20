def main():
    answer = []
    bool = [False for n in range(n)]
    perm(answer, bool, n)


def perm(answer, bool, n):
    if len(answer) == n:
        print(answer)
    else:
        for i in range(n):
            if bool[i]:  # if bool[i] is True
                continue
            else: # if bool[i] is False
                answer.append(i+1)
                bool[i] = True
                perm(answer, bool, n)
                answer.pop()
                bool[i] = False


if __name__ == "__main__":
    n = int(input())
    main()