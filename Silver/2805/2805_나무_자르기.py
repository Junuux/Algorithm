import sys
input = sys.stdin.readline

N, M = map(int, input().split())
height = list(map(int, input().split()))
start, end = 0, max(height)

while end >= start:
    mid = (start+end)//2
    tree = 0
    for i in height:
        if i > mid:
            tree += (i-mid)
    if tree >= M:
        start = mid+1
    else:
        end = mid-1
print(end)