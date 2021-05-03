def bubble_sort(arr: list):
    """
    Time complexity of n^2
    """
    len_arr = len(arr) - 1

    sorted_list = False

    while not sorted_list:
        sorted_list = True
        for index in range(len_arr):
            if arr[index] > arr[index + 1]:
                sorted_list = False
                arr[index], arr[index + 1] = arr[index + 1], arr[index]

    return arr


if __name__ == '__main__':
    sorted_list = bubble_sort([25, 6, 3, 57, 2, 1, 0, 4, 3, 12, 17])
    print(sorted_list)
