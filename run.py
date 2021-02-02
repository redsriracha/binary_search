import time


def binary_search_1d(arr, num):
    if len(arr) == 0:
        return None

    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if num == arr[mid]:
            return mid
        elif num < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None


def binary_search_2d(mat, num):
    if len(mat) == 0:
        return None

    row_len, col_len = len(mat), len(mat[0])
    low, high = 0, row_len * col_len

    while low <= high:
        mid = (low + high) // 2
        if num == mat[mid // col_len][mid % col_len]:
            return (mid // col_len, mid % col_len)
        elif num < mat[mid // col_len][mid % col_len]:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    row_size = 1000
    col_size = 1000
    total_elements = row_size*col_size

    def test_func(test, func):
        start = time.time()
        for i in range(total_elements):
            found = func(test, i)
            if found == None:
                print(f"Error:{found}")
        end = time.time()
        print(end-start)

    arr = [i for i in range(total_elements)]
    test_func(arr, binary_search_1d)

    mat = [[i+(j*row_size) for i in range(row_size)] for j in range(col_size)]
    test_func(mat, binary_search_2d)
