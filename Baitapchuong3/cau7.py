print("Nhập vào ngày tháng năm")
# Nhập dữ liệu
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Xác định số ngày trong tháng
if thang in [1, 3, 5, 7, 8, 10, 12]:
    ngay_trong_thang = 31
elif thang in [4, 6, 9, 11]:
    ngay_trong_thang = 30
else:
    # tháng 2
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        ngay_trong_thang = 29
    else:
        ngay_trong_thang = 28

# Tìm ngày kế tiếp
if ngay < ngay_trong_thang:
    ngay += 1
else:
    ngay = 1
    if thang == 12:
        thang = 1
        nam += 1
    else:
        thang += 1

print("Ngày kế tiếp là: {}/{}/{}".format(ngay, thang, nam))