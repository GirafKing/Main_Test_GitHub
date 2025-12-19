A, B = map(int, input().split())
N = int(input())

dict = {}
for _ in range(N) :
    radio_button = int(input())
    dict[radio_button] = abs(B - radio_button)

current_hz = A
count = 0

