# 이진탐색 O(log N) - 자료는 오름차순으로 정렬된 자료여야 한다.


# 반복을 이용한 이진탐색
def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


def binary_search_recursive(target, start, end, data):
    if start > end:
        return None
    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search_recursive(target, start, end, data)


if __name__ == "__main__":
    li = [i**2 for i in range(11)]
    print(li)
    target = 9  # 찾고자 하는 값
    idx = binary_search(target, li)

    if idx:
        print(idx)
    else:
        print("찾으시는 타겟 {}가 없습니다.".format(target))

    recursive_idx = binary_search_recursive(64, 0, 10, li)
    print("재귀함수 답", recursive_idx)
