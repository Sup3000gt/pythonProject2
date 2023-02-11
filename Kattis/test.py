def reading_time(N, P, X, Y):
    pages = (P-1) // N + 1
    your_time = P * X
    their_time = (pages-1) // N * Y
    return your_time + their_time

n, p, x, y = map(int, input().split())
print(reading_time(n, p, x, y))