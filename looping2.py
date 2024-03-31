#no 1

length = 1
for i in range(9,4,-1):
    for j in range(length):
        print(i-j,end=" ")
    length += 1
    print()
    
#no 2

for i in range(5,0,-1):
    for j in range(i):
        print(i-j, end=" ")
    print()
    

#no 3
for i in range(5):
    for j in range(1,10,+2):
        print(i+j, end=" ")
    print()

#no 4
b = 1
c = 2
for i in range(5):
    a = b
    for j in range(5):
        print(a, end=" ")
        a += c
    b += 1
    c += 1
    print()

#no 5
a = 5
b = 5

for i in range(a, 0, -1):
    for f in range(1, b + 1):
        if f < i:
            print("-", end=" ")
        else:
            print(f, end=" ")
    print()

#no 6
for i in range(4):
    for j in range(5):
        if (i + j) % 2 == 0:
            print("A", end=" ")
        if (i + j) % 2 == 1:
            print("B", end=" ")
    print()

#no 7
for i in range(5, 0, -1):
    for j in range(i):
        if (i + j) % 2 == 0:
            print("O", end=" ")
        if (i + j) % 2 != 0:
            print("S", end=" ")
    print()

#no 8
for i in range(1, 8):
    for j in range(1, i + 1):
        print("* ", end="")
    print()

#no 9
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()

#no 10
for i in range(7):
    for j in range(7):
        print("1" 
              if j == i 
              or j == 6 - i 
              else "+", end=" ")
    print()