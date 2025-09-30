import itertools

n = int(input())
k = int(input())

cards = [input() for _ in range(n)]
numbers = set()

for i in itertools.permutations(cards, k) :
    number = i[0] + i[1]
    numbers.add(number)

print(len(numbers))