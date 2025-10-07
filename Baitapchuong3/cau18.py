def ve_hinh_chu_nhat_rong(n):
    """Vẽ hình chữ nhật rỗng, chiều cao n."""
    print("--- Hình 1: Hình Chữ Nhật Rỗng ---")
    if n < 2:
        print("Chiều cao phải >= 2.")
        return

    # Hàng đầu tiên
    print("* " * n)

    # Các hàng giữa
    for i in range(2, n):
        # * + (2n - 3) khoảng trắng + *
        print("*" + " " * (2 * n - 3) + "*")

    # Hàng cuối cùng
    print("* " * n)

# ---

def ve_hinh_tam_giac_can(n):
    """Vẽ hình tam giác cân, chiều cao n."""
    print("\n--- Hình 2: Hình Tam Giác Cân (Đặc) ---")

    # Vẽ tam giác
    for i in range(1, n + 1):
        # Số khoảng trắng: n - i
        # Số dấu sao: 2 * i - 1
        print(" " * (n - i) + "* " * i)

# ---

def ve_hinh_zic_zac(n):
    """Vẽ hình zic-zac / móc câu, chiều cao n (cần n >= 4)."""
    print("\n--- Hình 3: Hình Zic-Zac/Móc Câu ---")
    if n < 4:
        print("Chiều cao phải >= 4 cho hình này.")
        return

    # Phần trên (Vẽ 1/2 tam giác đầu)
    for i in range(1, n // 2 + 1):
        # Dấu sao ở cột n - i
        print(" " * (n - i) + "*")

    # Phần giữa (ngang)
    print("*" * n)

    # Phần dưới (Vẽ 1/2 tam giác cuối)
    # Bắt đầu từ hàng thứ 1 (i=1) của phần dưới
    for i in range(1, n - (n // 2) + 1):
        # Dấu sao ở cột n + i - 1
        # Độ lùi: n - 1 + i
        print(" " * (n - 1 + i) + "*")
        
# ---

# Chương trình chính
while True:
    try:
        chieu_cao = int(input("Nhập chiều cao n (nên >= 4 để thấy rõ 3 hình): "))
        if chieu_cao <= 0:
            print("Chiều cao phải là số nguyên dương.")
        else:
            break
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

# Gọi các hàm để vẽ
ve_hinh_chu_nhat_rong(chieu_cao)
ve_hinh_tam_giac_can(chieu_cao)
ve_hinh_zic_zac(chieu_cao)