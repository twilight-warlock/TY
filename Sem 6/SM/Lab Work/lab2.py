# X i+1= (a X i + c) mod m
def linearCongruenceGenerator(seed, a, c, m):
    Xn = None
    Xn_1 = seed
    randomNumbers = []

    while(Xn != seed):
        randomNumbers.append(round(Xn_1/m, 4))
        Xn = (Xn_1*a + c) % m
        Xn_1 = Xn

    n = len(randomNumbers)
    density = (max(randomNumbers)-min(randomNumbers))/n

    return randomNumbers, n, density


#int(input("Seed Value: "))
seed = 1

#int(input("Multiplier: "))
a = 13

#int(input("Inceremnt: "))
c = 1

#int(input("Modulus: "))
m = 256

randomList, Period, Density = linearCongruenceGenerator(seed, a, c, m)

print("Random numbers: ", end=" ")
for i in range(len(randomList)):
    if i % 10 == 0:
        print()
    print(randomList[i], end=" ")
print("\nPeriod: ", Period)
print("Density: ", Density)

N = 100
n = 10
Ei = N/n
final = []

# defining the classes
Oi = [0]*n

# Selecting the first 100 numbers
testList = randomList[:N]

# sorting the list
testList.sort()

print("Test List: ")
for i in range(len(testList)):
    if i % 10 == 0:
        print()
    print(testList[i], end=" ")


for number in testList:
    Oi[int(number//0.1)] += 1

for each in Oi:
    final.append((each-Ei)**2/Ei)

Chi_o = sum(final)

print(f"\nChi_o: {Chi_o}")

# float(input("Enter Chi apliha value for 0.05: "))
Chi_aplha = 16.9

if(Chi_aplha > Chi_o):
    print("H_o is accepted")
else:
    print("H_o is rejected")
