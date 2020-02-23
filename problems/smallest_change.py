import sys


def min_coin_change(coins, V):
    m = len(coins)
    table = [0 for i in range(V + 1)]

    table[0] = 0

    for i in range(1, V + 1):
        table[i] = sys.maxsize

    for i in range(1, V + 1):
        for j in range(m):
            if coins[j] <= i:
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    return table[V]


print(min_coin_change([1, 5, 10, 25, 50], 7))
