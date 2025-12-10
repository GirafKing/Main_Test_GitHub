import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
out = []

S = sorted(set(numbers))
dict = {}
for num in numbers :
    count = N - S.index(num) - 1
    dict[num] = count