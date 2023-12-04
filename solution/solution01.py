from collections import deque
import heapq
import sys

n = int(sys.stdin.readline().rstrip())

peers = sorted([*map(int, sys.stdin.readline().rstrip().split())], reverse=True)

res = []
cnt = 0

for p in peers:
    res.append(p)
    if res[0] == len(res):
        cnt += 1
        res.clear()

print(cnt)