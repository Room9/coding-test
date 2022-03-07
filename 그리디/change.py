import sys

input = sys.stdin.readline

n, cnt = list(map(int,input().split()))

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    cnt += n // coin
    n %= coin

print(coin)