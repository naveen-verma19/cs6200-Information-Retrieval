
convTable = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V')

def to32(n):
    a = []
    if n == 0:
        return '0'
    m=abs(n)
    while m > 0:
        r = m % 32
        a.append(convTable[r])
        m = m // 32
    a.reverse()
    final= "".join(a)

    if n>0:
        return final
    else:
        return "-"+final


s=to32(86790)
print(s)
print(int(s,32))

for i in range(-180000,180000):
    t32=to32(i)
    if i!=int(t32,32):
        print("didnt"+ str(i))
