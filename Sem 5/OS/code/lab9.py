oor = [int(i)
       for i in input('Enter space seperated order of request: ').split()]
currpos = int(input('Enter current position of READ/WRITE head: '))
oor.sort()
st = 0
while(len(oor) != 0):
    min = 99999
    minnum = 0
    for i in oor:
        if abs(i - currpos) < min:
            min = abs(i - currpos)
            minnum = i
    currpos = minnum
    oor.remove(minnum)
    st += min
print('Total seek time =', st)
