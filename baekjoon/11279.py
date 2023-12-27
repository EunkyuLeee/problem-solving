import heapq
import sys

n = int(input())
heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        try:
            print(-heapq.heappop(heap))
        except IndexError:
            print(0)
    else:
        heapq.heappush(heap, -num)
