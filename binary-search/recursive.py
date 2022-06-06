def binary_search(elements, start, end, item):
    middle = (start + end) // 2

    if (item == elements[middle]):
        return middle

    if (start == end):
        return None

    if (item < elements[middle]):
        return binary_search(elements, start, middle - 1, item)

    if (item > elements[middle]):
        return binary_search(elements, middle + 1, end, item)


ordered_elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
start = 0
end = len(ordered_elements) - 1

result = binary_search(ordered_elements, start, end, 2)

print(result)
