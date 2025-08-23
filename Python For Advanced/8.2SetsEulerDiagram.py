
# Question 1
# Reads six integers and calculates: n + (m - x) + (k - y) + z
n, m, k, x, y, z = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
print(n + (m - x) + (k - y) + z)


# Question 2
# Reads eight integers and calculates set relationships between groups:
#  - Line 1: unique elements in each group (after exclusions).
#  - Line 2: pairwise overlaps.
#  - Line 3: number of elements outside all groups.
n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())

print((n - (n + m - t - x) - t - (n + k - t - z)) +
      (m - (n + m - t - x) - t - (m + k - t - y)) +
      (k - (n + k - t - z) - t - (m + k - t - y)))

print((n + m - t - x) + (n + k - t - z) + (m + k - t - y))

print(a - ((n - (n + m - t - x) - t - (n + k - t - z)) +
           (m - (n + m - t - x) - t - (m + k - t - y)) +
           (k - (n + k - t - z) - t - (m + k - t - y))) -
           ((n + m - t - x) + (n + k - t - z) + (m + k - t - y)) - t)
