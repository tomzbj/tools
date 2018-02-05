xtals = [0.032768, 3.579545, 3.6864, 4.9152, 6, 7, 8, 9.833, 10, 10.245, 12, \
        13.56, 13.433, 14.318, 16, 16.384, 16.9344, 17.7344, 20, 20.48, 24, \
        25, 27, 27.12, 28.224, 32, 48, 50, 72]

N_XTALS = len(xtals)
N_DIFFS = len(xtals) * 2 
xtals = [i * 1e6 for i in xtals]

while True:
    diff = [1e99] * N_DIFFS
    ids = list(range(N_DIFFS)) 

    print("Input needed freqency: ", end = "")
    buf = input()
    suffix = buf[-1]
    if suffix in ['k', 'K']:
        buf = buf[:-1]
        freq = float(buf) * 1000
    elif suffix in ['m', 'M']:
        buf = buf[:-1]
        freq = float(buf) * 1000000 
    else:
        if not buf.isdigit():
            continue
        freq = float(buf)

    for i in range(N_XTALS):
        div = int(xtals[i] / freq)
        if div == 0:
            continue
        diff[i * 2] = abs(freq - xtals[i] / div)
        diff[i * 2 + 1] = abs(freq - xtals[i] / (div + 1))

    for i in range(N_DIFFS - 1):
        for j in range(i + 1, N_DIFFS):
            if diff[i] > diff[j]:
                diff[i], diff[j] = diff[j], diff[i]
                ids[i], ids[j] = ids[j], ids[i]

    for i in range(5):
        min_id = ids[i]
        div = xtals[min_id // 2] // freq
        if div == 0:
            continue
        if min_id % 2 == 1:
            div += 1
        freq_d = xtals[min_id // 2] / div
        err = (freq_d - freq) / freq * 1e6
        print("%.3fM / %d = %.1f (%s%.0fppm)" % (xtals[min_id // 2] / 1e6, 
            div, freq_d, "+" if err > 0 else "", err) ) 

    print()
