import math

# Nhập giá trị a và số lần lặp (độ sâu căn bậc 2)
a = float(input("Nhập giá trị a: "))
n = int(input("Nhập số lần lồng căn (n): "))

# Tính căn bậc 2 lồng nhau
S = 0
for i in range(n):
    S = math.sqrt(a + S)

print(f"Giá trị căn bậc 2 lồng nhau với a = {a}, n = {n} là: {S:.6f}")