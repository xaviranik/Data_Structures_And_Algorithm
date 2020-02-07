def arbitrary_increment(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            return arr
        arr[i] = 0
        arr[i-1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    return arr


a1 = [1, 2, 8]
a2 = [9, 9, 9]
print(arbitrary_increment(a1))
print(arbitrary_increment(a2))
