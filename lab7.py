def knap(i, j):
    global v, w, p
    value = 0
    if v[i][j] < 0:
        if j < w[i]:
            value = knap(i - 1, j)
        else:
            value = max(knap(i - 1, j), p[i] + knap(i - 1, j - w[i]))
        v[i][j] = value
    return v[i][j]


def main():
    global n, w, p, v, cap
    profit, count = 0, 0

    print("Enter the number of objects: ", end="")
    n = int(input())
    x = [0] * (n + 1)

    print("Enter the profit and weights of the elements:")
    w = [0] * (n + 1)
    p = [0] * (n + 1)
    v = [[-1 for _ in range(11)] for _ in range(11)]

    for i in range(1, n + 1):
        print(f"Enter profit and weight for object no {i}: ", end="")
        p[i], w[i] = map(int, input().split())

    print("Enter the capacity: ", end="")
    cap = int(input())

    for i in range(n + 1):
        for j in range(cap + 1):
            if i == 0 or j == 0:
                v[i][j] = 0
            else:
                v[i][j] = -1

    profit = knap(n, cap)
    i, j = n, cap

    while j != 0 and i != 0:
        if v[i][j] != v[i - 1][j]:
            x[i] = 1
            j = j - w[i]
            i -= 1
        else:
            i -= 1

    print("Objects included are:")
    print("Sl.no\tWeight\tProfit")
    for i in range(1, n + 1):
        if x[i]:
            count += 1
            print(f"{count}\t{w[i]}\t{p[i]}")

    print(f"Total profit = {profit}")


if __name__ == "__main__":
    main()
