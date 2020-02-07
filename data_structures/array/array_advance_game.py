def array_advance(arr):
    furthest_reached = 0
    end_index = len(arr) - 1
    i = 0
    while i <= furthest_reached < end_index:
        furthest_reached = max(furthest_reached, arr[i] + i)
        i += 1

    return furthest_reached >= end_index


a = [3, 3, 1, 0, 2, 1]
b = [3, 3, 1, 0, 0, 1]
print(array_advance(a))
print(array_advance(b))
