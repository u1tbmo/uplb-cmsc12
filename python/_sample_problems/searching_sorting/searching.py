linear_search_iterations = 0
binary_search_iterations = 0


def linear_search(lst, x):
    for i in range(len(lst)):
        global linear_search_iterations
        linear_search_iterations += 1
        if lst[i] == x:
            return i
    return None


print(linear_search([_ for _ in range(1, 100000 + 1)], 100000))
print(f"Linear Search Iterations: {linear_search_iterations}")


def binary_search(lst, x):
    low = 0
    high = len(lst) - 1
    while low <= high:
        global binary_search_iterations
        binary_search_iterations += 1
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(binary_search([_ for _ in range(0, 100001)], 100000))
print(f"Binary Search Iterations: {binary_search_iterations}")
