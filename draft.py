import datetime
a = {'S':2, 'd':4}
a = dict(sorted(a.items(), key=lambda x: x[1], reverse=True))
print(a)
for i in a:
    print(i)

k = ''
k += 'adsf'
print(k)
a = set(0, 1, 2)
b = set(1, 3, 4)
print(a & b)