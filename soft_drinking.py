n, k, l, c, d, p, nl, np = list(map(int, input().split(' ')))

total_mililiters = k * l
total_lime_slices = c * d

toasts = min(total_mililiters // (n * nl), total_lime_slices // n, p // (n * np))

print(toasts)