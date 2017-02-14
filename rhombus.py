# rhombus
a = 10
b = 9
k = 1
while (k<2):
    for i in range (0, a):
        print(" "*(a-1) + "x"*i + "@"*i)
        i += 1
        a -= 1
    k += 1
else:
        for o in range(0, b):
            print(" "*o + "#"*b + "$"*b)
            o += 1
            b -= 1
