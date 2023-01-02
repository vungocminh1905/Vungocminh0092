j = []
h = []
b = 0
c = 0
a = int(input("nhập số lượng phần tử bạn muốn: "))
for i in range(1,a+1):
    print("nhập phần tử thứ: ",i)
    a = int(input())
    j.append(a)
#--------------------------------------------------------
print("tổng các phần tử trong list là: ",sum(j))
#-------------------------------------------
x = int(input("nhập phần tử x bạn muốn check: "))
for i in j:
    if x == i:
        c = c+1
    if x < i:
        h.append(i)
if c == 0:
    print("x không xuất hiện trong list ")
else:
    print("x xuất hiện trong list ",c,"lần")
print("các phần tử lớn hơn x là: ",h)


