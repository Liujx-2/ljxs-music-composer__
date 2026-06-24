def decode(code, mode=1):
    o = []
    if mode == 1:
        preprocess = [code[n:n+8] for n in range(0, len(code), 8)]
        for data in range(len(preprocess)):
            if data != len(preprocess) - 1:
                a = int(preprocess[data][:4], 2)
                b = int(preprocess[data][4:], 2)
                o.append([a, b])
            else:
                o.append(int(preprocess[data], 2))
    return o
