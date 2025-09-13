#cau3
toan=float(input("Nhap diem toan: "))
ly=float(input("Nhap diem ly: "))
hoa=float(input("Nhap diem hoa: "))
dtb=(toan+ly+hoa)/3
print("Diem trung binh=",dtb)
print("Diem trung binh=",round(dtb,2))
#cau4: Python hỗ trợ các kiểu dữ liệu cơ bản: kiểu số, kiểu chuỗi, kiểu logic, kiểu tập hợp, kiểu đặc biệt.
"""
câu 5: Các kiểu ghi chú trong Python: 
    -Ghi chú một dòng: dùng ký hiệu #
    -Ghi chú nhiều dòng: '''...''' 
"""

'''
câu 6: trình bày các toán tử
-Toán tử chia: /
-Toán tử chia nguyên(lấy phần nguyên)://
-Toán tử chia lấy dư: %
-Toán tử lũy thừa: **(tính số mũ)
-Toán tử logic:
    +and: đúng(True) khi cả hai đều đúng
    +or: đúng(True) khi ít nhất một điều kiện đúng
    +is: so sánh đối tượng(có phải cùng một object hay không)

    
câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím
    -Hàm input(): vd: name=input("Nhập tên:")
    -Ép kiểu dữ liệu khi nhập: vd: age=int(input("Nhap tuoi:"))
    -Nhập nhiều giá trị trên một dòng: vd: a, b = map(int, input("Nhập 2 số cách nhau bằng khoảng trắng: ").split())
print("Tổng =", a + b)
    -Nhập danh sách  nhiều phần tử: vd: numbers = list(map(int, input("Nhập các số: ").split()))
    -Nhập nhiều dòng: n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử {i+1}: "))
    arr.append(x)
print("Mảng:", arr)


câu 8: trình bày các lỗi lập trình và cách bắt lỗi trong Python
        -Lỗi cú pháp
        -Lỗi thời gian chạy
        -Lỗi logic
        =>Cách bắt lỗi:
        try – except (xử lý lỗi)
        finally (luôn chạy)
        else (chạy nếu không có lỗi)
câu 9:
a)	-13
(b)	4
(c)	1.0
(d)	1
(e)	-2.6
(f)	-3
(g)	8.666...
(h)	8
(i)	4.0
(j)	4
(k)	-0.5
(l)	-0.5
(m)	0.9
(n)	0.3636...
(o)	6.8333...
(p)	2.1666...
(q)	6.8333...
(r)	52.5


câu 10:
(a) x = x + 1 ⟶ x += 1
(b) x = x / 2 ⟶ x /= 2
(c) x = x - 1 ⟶ x -= 1
(d) x = x + y ⟶ x += y
(e) x = x - (y + 7) ⟶ x -= (y + 7)

(f) x = 2 * x ⟶ x *= 2
(g) number_of_closed_cases = number_of_closed_cases + 2*ncc
⟶ number_of_closed_cases += 2*ncc

''' 

