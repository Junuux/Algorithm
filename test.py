import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
name = []
for i in range(N):
    _, x = input().strip().split('.')
    name.append(x)
counter = sorted(Counter(name).most_common())
print(Counter(name))
print(counter)
for i in range(len(counter)): 
    print('{} {}'.format(counter[i][0], counter[i][1]))