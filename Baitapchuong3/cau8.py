# Nhập dữ liệu
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
pheptoan = input("Nhập phép toán (+, -, *, /): ")

# Xử lý phép toán
if pheptoan == '+':
    kq = a + b
elif pheptoan == '-':
    kq = a - b
elif pheptoan == '*':
    kq = a * b
elif pheptoan == '/':
    if b != 0:
        kq = a / b
    else:
        kq = "Không thể chia cho 0!"
else:
    kq = "Phép toán không hợp lệ!"

# Xuất kết quả
print("Kết quả:", kq)