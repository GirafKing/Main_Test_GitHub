A, B = map(int, input().split())
N = int(input())

dict = {}
for _ in range(N) :
    radio_button = int(input())
    dict[radio_button] = abs(B - radio_button)

current_hz = A
count = 0

close_radio_button = min(dict, key=dict.get)
if abs(A - B) > dict[close_radio_button] :
    current_hz = close_radio_button
    count += 1
    count += abs(current_hz - B)
else :
    count += abs(current_hz - B)

print(count)