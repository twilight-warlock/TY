def columnar_encrypt(text, key):
    m = { i : [] for i in key }
    cols = [list(text[j:j+len(key)]) for j in range(0, len(text), len(key))]
    if len(cols[-1]) < len(key):
        while len(cols[-1]) != len(key):
            cols[-1].append(' ')
    i = 0
    for k in m.keys():
        if i < len(key):
            for j in cols:
                m[k] += j[i]
            i += 1
    s = {k : m[k] for k in sorted(m)}
    cipher = ''
    for i in s.keys():
        for x in s[i]:
            cipher += x
    print(m)
    return cipher

def columnar_decrypt(cipher, key):
    if len(cipher) < len(key):
        key = key[:len(cipher)]
    n = len(cipher) // len(key)
    s = { k : [] for k in sorted(key) }
    cols = [cipher[j:j+n] for j in range(0, len(cipher), n)]    
    i = 0
    for k in s.keys():
        if i < len(key):
            s[k] = list(cols[i])
            i += 1
    m = {}  
    for k in key:
        m[k] = s[k]
    plain = ''
    import pandas as pd
    m = pd.DataFrame(m)
    for i in m.itertuples():
        for j in i[1:]:
            plain += j
    print(s, '\n')
    return plain.strip()