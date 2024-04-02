n = int(input())
address = sorted(map(int, input().split()))
m = address[n // 2]
print(sum(abs(e - m) for e in address))