e24_base = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.49, 2.7, 3.0, \
            3.3, 3.6, 3.9, 4.3, 4.7, 4.99, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]

print('Input Vout: ', end = '')
vout = float(input())
print('Input Vref: ', end = '')
vref = float(input())
ratio = vout / vref;
    
result = []
for i in e24_base:
    r2_accu = i * (ratio - 1)
    r2_base = 0
    k = 1
    while r2_accu < 1.0:
        r2_accu *= 10.0
        k *= 10.0
    while r2_accu > 10.0:
        r2_accu /= 10.0
        k /= 10.0
    err_max = 999
    for j in e24_base:
        err = abs(j - r2_accu)
        if err < err_max:
            err_max = err
            r2_base = j
    r2_final = r2_base / k
    vout_final = ((r2_final / i + 1) * vref * 10) / 10
    err = ((vout_final / vout - 1) * 1000) / 10 
    result.append((i, r2_final, vout_final, err))

result.sort(key = lambda x:abs(x[3]))

print('    R1       R2       Vout       ERR')
for r1, r2, vout, err in result:
    print('%8.2f %8.2f %8.2f %8.2f%%' % (r1, r2, round(vout, 2), round(err, 2)))
