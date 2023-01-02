j = []
a = 10
for i in range(1,a+1):
    a1 = int(input("nhập chiều cao: "))
    a1 = float(a1)
    a1 = a1/0.0254
    j.append(a1)
print("3 chiều cao đầu tiên là: ",j[0],j[1],j[2])
print("3 chiều cao cuối cùng là: ",j[7],j[8],j[9])
print('chiều cao trung bình là: ',sum(j)/len(j))
print("chiều cao lớn nhất là: ",max(j))
print("chiều cao nhỏ nhất là; ",min(j))
j.sort()
print("list theo thứ tự tăng dần là: ",j)
j.reverse()
print("list theo giá trị giảm dần là; ",j)
