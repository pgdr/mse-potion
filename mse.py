n, k = map(int, input().split())
data = list(map(int, input().split()))

INF = 10**10
DP = [INF] * (n + 1)
DP[0] = 0

prefix_sum = [0] * (n + 1)
prefix_sum_sq = [0] * (n + 1)
for i, x in enumerate(data, 1):
    prefix_sum[i] = prefix_sum[i - 1] + x
    prefix_sum_sq[i] = prefix_sum_sq[i - 1] + x**2


def squared_error(l, r):
    L_sq = prefix_sum_sq[l]
    s = prefix_sum[l] - prefix_sum[r]
    return (l - r) * (L_sq - prefix_sum_sq[r]) - s**2


def divide_and_conquer(l, r, l_opt, r_opt, cur):
    if l > r:
        return
    mid = (l + r) // 2
    best_val = INF
    best_p = -1
    hi = min(r_opt, mid - 1)
    for p in range(l_opt, hi + 1):
        v = DP[p] + squared_error(mid, p)
        if v < best_val:
            best_val = v
            best_p = p

    cur[mid] = best_val
    divide_and_conquer(l, mid - 1, l_opt, best_p, cur)
    divide_and_conquer(mid + 1, r, best_p, r_opt, cur)


# DO the DP
for b in range(1, k + 1):
    cur = [INF] * (n + 1)
    divide_and_conquer(b, n, b - 1, n - 1, cur)
    DP = cur

print(DP[n])
