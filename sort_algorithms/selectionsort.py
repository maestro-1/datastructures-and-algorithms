def selection_sort(arr: list):
    """
    Time complexity of n^2
    """
    for i in range(0, len(arr) - 1):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        if minimum != i:
            arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr


if __name__ == '__main__':
    sorted_list = selection_sort([25, 6, 3, 57, 2, 1, 0, 4, 3, 12, 17])
    print(sorted_list)
