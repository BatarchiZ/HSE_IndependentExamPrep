def binSearch(houses):
    left = 0
    right = 2 ** 128
    while(left + 1 < right):
        ropeSize = (left + right)//2
        suma = 0
        for i in a:
            suma += (i // ropeSize)
        if(suma < houses):
            right = ropeSize
        else:
            left = ropeSize
    return left


f = open("ropes.in")
n, k = map(int, f.readline().split())
a = [int(n) for n in f.readlines()]
# print(a)
print(binSearch(k))

