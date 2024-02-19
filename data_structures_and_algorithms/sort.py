def bubble_sort(arr):
    """Sort the given list using the bubble sort algorithm.
    Best case: O(n)
    Average case: O(n^2)
    Worst case: O(n^2)
    """

    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    """Sort the given list using the insertion sort algorithm.
    Best case: O(n)
    Average case: O(n^2)
    Worst case: O(n^2)
    """
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    """Sort the given list using the selection sort algorithm.
    Best case: O(n^2)
    Average case: O(n^2)
    Worst case: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def merge_sort(arr):
    """Sort the given list using the merge sort algorithm.
    Best case: O(n log n)
    Average case: O(n log n)
    Worst case: O(n log n)
    """

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
