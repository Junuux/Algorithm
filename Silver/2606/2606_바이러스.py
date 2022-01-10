import sys
input = sys.stdin.readline

N = int(input())
n = int(input())
linked = []
result = []
for i in range(n):
    link = list(map(int, input().split()))
    linked.append(link)

def find_set(linked, num):
    check = []
    for i, j in linked:
        if i == num :
            check.append(j)
        elif j == num:
            check.append(i)
    while check:
        a = check.pop()
        if a not in result:
            result.append(a)
            find_set(linked, a)
            
    return result
x = len(find_set(linked, 1)) -1
print(x)