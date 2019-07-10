

def find_duplicates(array: list):
    """
    This function finds duplicates entries in an array/list.

    Args:
        array: A list with data.

    Returns:
        Prints duplicated entries.
    """
    for i in range(len(array)):

        for j in range(len(array)):
            if i == j:
                continue

            if array[i] == array[j]:
                print(array[i])


chars = ['a', 'b', 'c', 'd', 'f', 'g', 'f']
find_duplicates(chars)