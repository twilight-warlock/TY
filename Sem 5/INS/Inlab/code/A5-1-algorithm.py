def majorityFn(bit1, bit2, bit3):
    list1 = [bit1, bit2, bit3]
    return max(list1, key=list1.count)


def returnList(string):
    list1 = []
    for x in string:
        list1.append(int(x))
    return list1


def XOR(a, b, c=0, d=0):
    return a ^ b ^ c ^ d


def A51CipherEncrypt(key, bits):
    X = returnList(key[0:19])
    Y = returnList(key[19:41])
    Z = returnList(key[41:64])
    keystream = []
    for bit in range(bits):
        maj = majorityFn(X[8], Y[10], Z[10])

        if X[8] == maj:
            Tx = XOR(X[13], X[16], X[17], X[18])
            X.insert(0, Tx)
            X.pop()

        if Y[10] == maj:
            Ty = XOR(Y[20], Y[21])
            Y.insert(0, Ty)
            Y.pop()

        if Z[10] == maj:
            Tz = XOR(Z[7], Z[20], Z[21], Z[22])
            Z.insert(0, Tz)
            Z.pop()

    keystream.append(XOR(X[18], Y[21], Z[22]))
    keystream = ''.join(str(x) for x in keystream)
    return X, Y, Z, keystream


key = input('Enter the 64 bit key: ')
bits = int(input('Enter the number of bits of keystream: '))
X, Y, Z, keystream = A51CipherEncrypt(key, bits)
print(f'\nTheKeystream is: {keystream}')
print(f'\nThe Register X: {X}')
print(f'\nThe Register Y: {Y}')
print(f'\nThe Register Z: {Z}')
