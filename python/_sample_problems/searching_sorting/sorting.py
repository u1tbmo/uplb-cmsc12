def selectionsort(a):
    n = len(a)
    # Traverse through all array elements
    for i in range(n):
        min_idx = i
        # Swap the moment you find the minimum element
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]

    return a


r = selectionsort([5, 8, 4, 1, 3, 7, 2, 9, 0, 6])
print(r)


def bubblesort(a):
    n = len(a)
    # Traverse through all array elements
    for i in range(n):
        for j in range(n - i - 1):
            # Swap if the element found is greater
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


s = bubblesort([5, 8, 4, 1, 3, 7, 2, 9, 0, 6])
print(s)
