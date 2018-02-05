e24_base = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.49, 2.7, 3.0, 3.3,\
        3.6, 3.9, 4.3, 4.7, 4.99, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]

e24 = []
for i in range(6):
    e24 += e24_base
    e24_base = [x * 10 for x in e24_base]

print('Input Rx: ', end = '')
r = float(input())
if r in e24:
    print('Rx is in e24 series!')
    exit()
    
result = []
for r1 in e24:
    if r1 < r:
        continue
    if r1 > r * 2:
        break
    r2_raw = 1 / (1 / r - 1 / r1)
    diff = [round(abs(x - r2_raw), 3) for x in e24]
    r2 = e24[diff.index(min(diff))] 
    
    rx = 1 / (1 / r1 + 1 / r2)
    err = (rx - r) / r * 100
    result.append((r1, r2, rx, err))

result.sort(key = lambda x:abs(x[3]))

print('    R1       R2       Rx       ERR')
for r1, r2, rx, err in result:
    print('%8.2f %8.2f %8.2f %8.2f%%' % (r1, r2, round(rx, 3), round(err, 1)))
