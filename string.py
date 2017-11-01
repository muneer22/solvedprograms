a = input().strip()
s = input().strip()

sum = 0
for i in range(len(a) - len(s) + 1):
    if a[i:i+len(s)] == s:
        sum += 1
print sum
