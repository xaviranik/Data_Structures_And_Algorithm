def number_ones(x):
    count = 0
    while x != 0:
        if x % 2 == 1:
            count += 1
        x = int(x / 2)
    return count


print(number_ones(50))
