def binary_search(elements, item):
    start = 0
    end = len(elements) - 1

    while (start < end):
        middle = (start + end) // 2

        if (item == elements[middle]):
            return middle

        elif (item < elements[middle]):
            end = middle - 1

        elif (item > elements[middle]):
            start = middle + 1

    return None


ordered_elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(ordered_elements, 6)

print(result)
