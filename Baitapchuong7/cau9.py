# ==========================
# QUẢN LÝ SẢN PHẨM THEO DANH MỤC
# ==========================
import os

FILE_PATH = "database.txt"

# ========== HÀM XỬ LÝ FILE ==========
def DocFile(path):
    ds = []
    if not os.path.exists(path):
        return ds
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip()
            if data != "":
                arr = data.split(";")
                ds.append(arr)
    return ds

def LuuFile(path, ds):
    with open(path, "w", encoding="utf-8") as f:
        for sp in ds:
            line = ";".join(sp)
            f.write(line + "\n")

# ========== CÁC CHỨC NĂNG ==========
def ThemSanPham():
    madm = input("Nhập mã danh mục: ")
    tendm = input("Nhập tên danh mục: ")
    masp = input("Nhập mã sản phẩm: ")
    tensp = input("Nhập tên sản phẩm: ")
    while True:
        try:
            dongia = float(input("Nhập đơn giá: "))
            break
        except ValueError:
            print("Đơn giá phải là số!")

    line = [madm, tendm, masp, tensp, str(dongia)]
    ds = DocFile(FILE_PATH)
    ds.append(line)
    LuuFile(FILE_PATH, ds)
    print("✅ Đã thêm sản phẩm thành công!\n")

def XemDanhSach():
    ds = DocFile(FILE_PATH)
    if not ds:
        print("❌ Chưa có dữ liệu.\n")
        return
    print(f"{'Mã DM':<8}{'Tên danh mục':<20}{'Mã SP':<8}{'Tên sản phẩm':<20}{'Đơn giá':>10}")
    print("-"*70)
    for sp in ds:
        print(f"{sp[0]:<8}{sp[1]:<20}{sp[2]:<8}{sp[3]:<20}{sp[4]:>10}")
    print()

def TimKiem():
    tu = input("Nhập từ khóa cần tìm: ").lower()
    ds = DocFile(FILE_PATH)
    ketqua = [sp for sp in ds if tu in sp[1].lower() or tu in sp[3].lower()]
    if not ketqua:
        print("❌ Không tìm thấy sản phẩm nào.\n")
    else:
        XuatDanhSach(ketqua)

def XuatDanhSach(ds):
    print(f"{'Mã DM':<8}{'Tên danh mục':<20}{'Mã SP':<8}{'Tên sản phẩm':<20}{'Đơn giá':>10}")
    print("-"*70)
    for sp in ds:
        print(f"{sp[0]:<8}{sp[1]:<20}{sp[2]:<8}{sp[3]:<20}{sp[4]:>10}")
    print()

def XoaSanPham():
    masp = input("Nhập mã sản phẩm cần xóa: ")
    ds = DocFile(FILE_PATH)
    ds_moi = [sp for sp in ds if sp[2] != masp]
    if len(ds_moi) == len(ds):
        print("❌ Không tìm thấy sản phẩm cần xóa.\n")
    else:
        LuuFile(FILE_PATH, ds_moi)
        print("🗑️ Đã xóa sản phẩm thành công!\n")

def SuaSanPham():
    masp = input("Nhập mã sản phẩm cần sửa: ")
    ds = DocFile(FILE_PATH)
    timthay = False
    for sp in ds:
        if sp[2] == masp:
            timthay = True
            print("Thông tin cũ:", sp)
            sp[3] = input("Tên sản phẩm mới: ") or sp[3]
            sp[4] = input("Đơn giá mới: ") or sp[4]
    if timthay:
        LuuFile(FILE_PATH, ds)
        print("✏️ Đã sửa sản phẩm thành công!\n")
    else:
        print("❌ Không tìm thấy sản phẩm cần sửa.\n")

def SapXepTheoGia():
    ds = DocFile(FILE_PATH)
    ds.sort(key=lambda x: float(x[4]), reverse=True)
    print("📊 Danh sách sau khi sắp xếp giảm dần theo giá:")
    XuatDanhSach(ds)

# ========== MENU CHÍNH ==========
def Menu():
    while True:
        print("======= QUẢN LÝ SẢN PHẨM =======")
        print("1. Thêm sản phẩm")
        print("2. Xem danh sách")
        print("3. Sửa sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm sản phẩm")
        print("6. Sắp xếp theo đơn giá (giảm dần)")
        print("0. Thoát")
        chon = input("Chọn chức năng: ")

        if chon == "1":
            ThemSanPham()
        elif chon == "2":
            XemDanhSach()
        elif chon == "3":
            SuaSanPham()
        elif chon == "4":
            XoaSanPham()
        elif chon == "5":
            TimKiem()
        elif chon == "6":
            SapXepTheoGia()
        elif chon == "0":
            print("Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!\n")

Menu()
