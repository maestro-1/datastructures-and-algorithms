def quick_sort(arr: list, greater: list = None, lesser: list = None):
    """
    Time complexity of nlog2(n)
    """

    greater = []
    lesser = []

    if len(arr) <= 1:
        return arr

    pivot = arr.pop()

    for item in arr:
        if item < pivot:
            lesser.append(item)

        if item > pivot:
            greater.append(item)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    sorted_list = quick_sort([25, 6, 3, 57, 2, 1, 0, 4, 3, 12, 17])
    print(sorted_list)
