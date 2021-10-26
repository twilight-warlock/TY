superSeq = [3, 5, 9, 20, 44]
publicKey = []
m = 67
n = 89

for i in superSeq:
    x = (i*n) % m
    publicKey.append(x)

print(f"\nPublic Key:\t{publicKey}")
print(f"\nPrivate Key:\t{superSeq}")


def knapsackEncrypt(plainText, superSeq, n, m):
    cipherText = []
    index = 0
    sum = 0

    for bit in plainText:
        if bit == '1':
            sum += publicKey[index]
        index += 1
        if index == 5:
            cipherText.append(sum)
            index = 0
            sum = 0
    return cipherText


def inverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1


def knapsackDecrypt(ciphertext, superSeq, n, m):
    inversed = inverse(n, m)
    decodedValues = [(x * inversed) % m for x in cipherText]
    sum = 0
    plainText = ''

    for value in decodedValues:
        ans = []
        for item in superSeq[::-1]:
            if sum + item <= value:
                sum += item
                ans.append('1')
            else:
                ans.append('0')

        plainText += ''.join(ans[::-1])
        sum = 0

    return plainText


plainText = input('Enter plaintext bits: ')
binChunks = [plainText[6*i:6*(i+1)] for i in range(len(plainText)//6)]
print(f"\nSplitted plain text:\t{binChunks}")

cipherText = knapsackEncrypt(plainText, superSeq, n, m)
decodedPlainText = knapsackDecrypt(cipherText, superSeq, n, m)
print(f'CipherText:\t{cipherText}')
print(f'\nPlainText:\t{decodedPlainText}')
