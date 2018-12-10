from operator import itemgetter, attrgetter

# 사실 python 에서는 sort()를 쓰면 배열이 자동으로 정렬된다. 하지만 연습을 위해 정렬들을 구현해봤다.

# python에서 swap은 그냥 a, b = b, a 이렇게 하면됨 wow
def swap(x, y):
    temp = x
    x = y
    y = temp

    return x, y


#  가장 작은 값을 앞으로 O(n^2)
def selection_sort(arr):
    for i in range(len(arr)-1):
        min = arr[i]
        minindex = i
        # find min value
        for step in range(i+1, len(arr)):
            if min > arr[step]:
                min = arr[step]
                minindex = step
        # swap
        arr[minindex], arr[i] = arr[i], arr[minindex]

    return arr


# 옆에 있는 값과 비교해서 더 작은 값을 앞으로. 버블버블~ O(n^2) 선택정렬과 시간복잡도는 똑같지만
# 버블정렬은 매번 swap을 해주기 때문에 가장 비효율적인 버블정렬.
def bubble_sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


# 원카드 정리하는 방법. 앞에는 이미 정렬이 되있다고 가정하고 올바른 위치에 삽입(필요한 만큼만 이동) O(n^2)
# 데이터가 이미 거의 정렬된 상태에 한해서는 어떤 알고리즘보다도 빠르다. -> 내 왼쪽에가 나보다 작으면(정렬되어있으면) 더이상 왼쪽으로 안 가기 때문
def insertion_sort(arr):
    for idx in range(len(arr)):
        while idx > 0 and arr[idx-1] > arr[idx]:
            arr[idx], arr[idx-1] = arr[idx-1], arr[idx]
            idx -= 1

    return arr


# 특정한 값을 기준(pivot)으로 큰 숫자와 작은 숫자를 오른쪽과 왼쪽으로 정렬 O(N*logN). But, 거의 정렬이 되어있는 경우, 최악 시간복잡도는 O(N^2)
# Divide and conquer algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        greater = [elem for elem in arr[1:] if elem > pivot]
        lesser = [elem for elem in arr[1:] if elem <= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


# 일단 반으로 쪼갠후 합치는 순간에 정렬.  피벗 값 없음 O(N * logN)
# 정렬된 배열을 담을 새로울 배열 필요
# Divide and conquer algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        l = merge_sort(left)
        r = merge_sort(right)
        # 정렬된 두개의 배열을 합치기
        return merge(l, r)
    else:
        return arr


def merge(left, right):
    i = 0
    j = 0
    arr = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    while i < len(left):
        arr.append(left[i])
        i += 1
    while j < len(right):
        arr.append(right[j])
        j += 1

    return arr


def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


# max heap을 만들고 root node(최댓값)과 마지막 노드를 change -> 반복하면 오름차순 정렬된 트리가 완성~
# O(N * logN)
def heap_sort(unsorted):
    n = len(unsorted)
    for i in range(n//2 -1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n-1, 0, -1):
        # root 노드(최댓값) 와 맨 마지막 노드 바꾸기
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return repr((self.name, self.age, self.grade))


def main():
    arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    print("selectionsort:", selection_sort([1, 10, 5, 8, 7, 6, 4, 3, 2, 9]))
    print("bubblesort:", bubble_sort([1, 10, 5, 8, 7, 6, 4, 3, 2, 9]))
    print("insertionsort:", insertion_sort([1, 10, 5, 8, 7, 6, 4, 3, 2, 9]))
    print("quicksort:", quick_sort([1, 10, 5, 8, 7, 6, 4, 3, 2, 9]))
    print("mergesort:", merge_sort([1, 10, 5, 8, 7, 6, 4, 3, 2, 9]))
    print("heapsort:", heap_sort(([1, 10, 5, 8, 7, 6, 4, 3, 2, 9])))

    print(sorted(arr))

    students = [
        ("jane", 22, 'A'),
        ("dave", 32, 'B'),
        ("sally", 17, 'B'),
    ]
    # students의 item인 튜플의 2번째 요소로 sort 하겠다.(age)
    print(sorted(students, key=itemgetter(1)))

    student_objects = [
        Student("jane", 22, 'A'),
        Student("dave", 32, 'B'),
        Student("sally", 17, 'B'),
    ]

    print(sorted(student_objects, key=lambda student: student.age))
    print(sorted(student_objects, key=attrgetter('age'), reverse=True))


if __name__ == "__main__":
    main()
