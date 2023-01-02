def find_max(a, b, c, d):
    max = a
    if max < b: max = b
    if max < c: max = c
    if max < d: max = d
    return max
def find_min(a, b, c, d):
    min = a
    if b < min: min = b
    if c < min: min = c
    if d < min: min = d
 
print("Nhập vào số thứ nhất: ")
a = (input())
 
print("Nhập vào số thứ hai: ")
b = (input())
 
print("Nhập vào số thứ ba: ")
c = (input())

print("Nhập vào số thứ tư: ")
d = (input())
print("Số lớn nhất trong bốn số ", a, " ", b, " ", c, " ",d," là ", find_max(a, b, c, d))
print("Số nhỏ nhất trong bốn số ", a, " ", b, " ", c, " ",d," là ", find_min(a, b, c, d))
