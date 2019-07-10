# TODO: add docstrings
# TODO: reformat code using Python Convention

# O(1)
def sum_up_to(n: int):
    print(n * (n + 1) // 2)


# O(n)
def sum_up_to_2(n: int):
    result = 0
    for i in range(n + 1):
        result += i
        print(result)

# O(n²)


# O(log n)
def binary_search(array: list, x: int, low_position: int, high_position: int):
    mid = (low_position + high_position) // 2

    if x > array[high_position] or x < array[low_position]:
        return print('x: {} is out of range.'.format(x))

    if x == array[mid]:
        return print('True', x)
    elif x > array[mid]:
        binary_search(array, x, mid+1, high_position)
    elif x < array[mid]:
        binary_search(array, x, low_position, mid-1)


array = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
binary_search(array, 4099, 0, (len(array)-1))


# O(n!)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


