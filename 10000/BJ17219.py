N, M = map(int, input().split())

passwords = {}
for i in range(N) :
    site_name, password = input().split()
    passwords[site_name] = password

for i in range(M) :
    find = input()
    p = passwords[find]
    print(p)