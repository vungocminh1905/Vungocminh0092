def bmi(m,h):
    return m/(h*h)
m = float(input("nhập cân nặng(kg): "))
h = float(input("Nhập chiều cao(m): "))
if bmi(m,h)<18.5:
    print("Bạn gầy")
elif bmi(m,h)<24.99:
    print("Bạn bình thường")
else:
    print("Bạn béo phì")