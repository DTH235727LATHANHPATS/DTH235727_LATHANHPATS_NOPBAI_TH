def main():
    s = input("Nhập vào 1 chuỗi: ")

    # Khởi tạo bộ đếm
    hoa = 0
    thuong = 0
    so = 0
    dac_biet = 0
    khoang_trang = 0
    nguyen_am = 0
    phu_am = 0

    # Tập hợp nguyên âm
    vowels = "aeiouAEIOU"

    for c in s:
        if c.isupper():
            hoa += 1
        elif c.islower():
            thuong += 1
        if c.isdigit():
            so += 1
        if c.isspace():
            khoang_trang += 1
        if not c.isalnum() and not c.isspace():
            dac_biet += 1
        if c.isalpha():
            if c in vowels:
                nguyen_am += 1
            else:
                phu_am += 1

    # Xuất kết quả
    print(f"Số chữ IN HOA: {hoa}")
    print(f"Số chữ in thường: {thuong}")
    print(f"Số chữ số: {so}")
    print(f"Số ký tự đặc biệt: {dac_biet}")
    print(f"Số khoảng trắng: {khoang_trang}")
    print(f"Số nguyên âm: {nguyen_am}")
    print(f"Số phụ âm: {phu_am}")

# Chạy chương trình
main()
