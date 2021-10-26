import math
p = int(input("Enter value of p: "))
q = int(input("Enter value of q: "))


def isPrime(n):

    if (n <= 1):
        return False

    for i in range(2, n):
        if (n % i == 0):
            return False

    return True


checkP = isPrime(p)
checkQ = isPrime(q)
while(((checkP == False) or (checkQ == False))):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    checkP = isPrime(p)
    checkQ = isPrime(q)

n = p*q
print("\nRSA modulus, n is ", n)
phi = (p-1)*(q-1)

e = int(input("\nEnter value of e: "))
while (e < phi):
    if(math.gcd(e, phi) == 1):
        break
    else:
        e += 1
public_key = (e, n)

print(f"\nPublic key is {public_key} ")


def egcd(a, b):

    if(a % b == 0):
        return(b, 0, 1)
    else:
        gcd, s, t = egcd(b, a % b)
        s = s-((a//b) * t)
        print("%d: %d*(%d) + (%d)*(%d)" % (gcd, a, t, s, b))
        return(gcd, t, s)


def inverse(e, phi):
    gcd, s, _ = egcd(e, phi)
    if(gcd != 1):
        return None
    else:
        if(s < 0):
            print("s=%d.\nSince %d is less than 0, s: s(modphi), s: %d." %
                  (s, s, s % phi))
        elif(s > 0):
            print("s=%d." % (s))

        return s % phi


d = inverse(e, phi)
private_key = (d, n)
print(f"\nPrivate key is: {private_key}\n")


def RsaEncrypt(priv, n_text):
    d, n = priv
    x = []
    m = 0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c = pow(m, d) % n
            x.append(c)
        elif(i.islower()):
            m = ord(i)-97
            c = pow(m, d) % n
            x.append(c)
        elif(i.isspace()):
            spc = 400
            x.append(400)
    return x


def RsaDecrypt(pub_key, c_text):
    e, n = pub_key

    txt = list(c_text)
    x = ''
    m = 0
    for i in txt:
        if(i == '400'):
            x += ' '
        else:
            m = pow(int(i), e) % n
            m += 65
            c = chr(m)
            x += c

    return x


message = input("Enter Messge: ")
print(f"\nYour Message is: {message}")
print(f"\nEncrypted message is: {RsaEncrypt(private_key,message)}")
print(
    f"\nDecrypted message is: {RsaDecrypt(public_key,RsaEncrypt(private_key,message))}")
