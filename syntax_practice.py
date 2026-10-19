from collections import defaultdict, Counter
import heapq, bisect
d = defaultdict(list)
d[key].append(x)
c = Counter(nums); c.most_common(k)
key = ''.join(sorted(s))

nums.sort(key=lambda x: (x[0], -x[1]))

bisect.insort(arr, x)

heapq.heappush(h, x); heapq.heappop(h)

for i, v in enumerate(arr): ...
grid = [[0]*m for _ in range(n)]

n = int(input())
arr = list(map(int, input().split()))

class Thing:
    def __init__(self, x):
        self.x = x
    def get(self):
        return self.x