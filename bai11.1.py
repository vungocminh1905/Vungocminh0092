f = [1,2,3]
g = [1,[2,3]]
h = []
k = [1,2,3][1:]
def a():
    e = 0
    for i in f:
        e = e + 1
    return e
def b():
    e = 0
    for i in g:
        e = e + 1
    return e
def c():
    e = 0
    for i in h:
        e = e + 1
    return e
def d():
    e = 0
    for i in k:
        e = e + 1
    return e
print("số phần tử trong a là: ",a())
print("số phần tử trong b là: ",b())
print("số phần tử trong c là: ",c())
print("số phần tử trong d là: ",d())
    