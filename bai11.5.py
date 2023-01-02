j = []
h = []
duong_list = []
am_list = []
def kiem_tra_so_nguyen_to(i):
    if (i <2):
        ag = 0
    for p in range(2, i):
        if i % p == 0:
            ag = 0
            break
    else:
        ag = 1
    return ag

running = True
while running:
    a = int(input("nhập giá trị: "))
    j.append(a)
    a1 = int(input("bạn có muốn nhập nữa không: 1,có:::0,không: "))
    if a1 == 0:
        running = False
for v in j:
    b = kiem_tra_so_nguyen_to(v)
    if b == 1:
        h.append(v)
    if v > 0:
        duong_list.append(v)
    else:
        am_list.append(v)
j.sort()
trung_binh_cong = sum(duong_list)/len(duong_list)
trung_binh_cong1 = sum(duong_list)/len(duong_list)
print("trung bình cộng của các phần tử dương là: ",trung_binh_cong)
print("trung bình cộng của các phần tử am là: ",trung_binh_cong1)
print("các số nguyên tố có trong list là: ",h)   
print("giá trị lớn nhất của list bạn nhập vào là: ",max(j))
print("giá trị nhỏ nhất của list bạn nhập vào là: ",min(j))
print("giá trị tăng dần của list như sau: ",j)