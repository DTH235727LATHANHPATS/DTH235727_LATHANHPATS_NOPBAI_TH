import json
import os

FILE_PATH = "sinhvien.json"

# ============================
# HÀM XỬ LÝ FILE JSON
# ============================
def doc_file():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def luu_file(data):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ============================
# CHỨC NĂNG
# ============================
def them_sinhvien():
    ds = doc_file()
    malop = input("Nhập mã lớp: ")
    tenlop = input("Nhập tên lớp: ")

    # Tìm lớp đã tồn tại
    lop = next((l for l in ds if l["malop"] == malop), None)
    if lop is None:
        lop = {"malop": malop, "tenlop": tenlop, "sinhvien": []}
        ds.append(lop)

    masv = input("Nhập mã sinh viên: ")
    hoten = input("Nhập họ tên: ")
    namsinh = int(input("Nhập năm sinh: "))
    lop["sinhvien"].append({"masv": masv, "hoten": hoten, "namsinh": namsinh})
    luu_file(ds)
    print("✅ Đã thêm sinh viên thành công!\n")

def xem_danh_sach():
    ds = doc_file()
    if not ds:
        print("❌ Chưa có dữ liệu.\n")
        return
    for lop in ds:
        print(f"\nLớp: {lop['malop']} - {lop['tenlop']}")
        print(f"{'Mã SV':<10}{'Họ tên':<25}{'Năm sinh':>10}")
        print("-"*45)
        for sv in lop["sinhvien"]:
            print(f"{sv['masv']:<10}{sv['hoten']:<25}{sv['namsinh']:>10}")
    print()

def tim_sinhvien():
    tu = input("Nhập tên hoặc mã SV cần tìm: ").lower()
    ds = doc_file()
    ketqua = []
    for lop in ds:
        for sv in lop["sinhvien"]:
            if tu in sv["hoten"].lower() or tu in sv["masv"].lower():
                ketqua.append((lop["malop"], sv))
    if not ketqua:
        print("❌ Không tìm thấy sinh viên nào.\n")
    else:
        print(f"{'Lớp':<10}{'Mã SV':<10}{'Họ tên':<25}{'Năm sinh':>10}")
        print("-"*55)
        for malop, sv in ketqua:
            print(f"{malop:<10}{sv['masv']:<10}{sv['hoten']:<25}{sv['namsinh']:>10}")
        print()

def xoa_sinhvien():
    masv = input("Nhập mã sinh viên cần xóa: ")
    ds = doc_file()
    found = False
    for lop in ds:
        sv_moi = [sv for sv in lop["sinhvien"] if sv["masv"] != masv]
        if len(sv_moi) != len(lop["sinhvien"]):
            lop["sinhvien"] = sv_moi
            found = True
    if found:
        luu_file(ds)
        print("🗑️ Đã xóa sinh viên thành công!\n")
    else:
        print("❌ Không tìm thấy mã sinh viên cần xóa.\n")

def sua_sinhvien():
    masv = input("Nhập mã sinh viên cần sửa: ")
    ds = doc_file()
    found = False
    for lop in ds:
        for sv in lop["sinhvien"]:
            if sv["masv"] == masv:
                found = True
                print("Thông tin cũ:", sv)
                sv["hoten"] = input("Họ tên mới (Enter để giữ nguyên): ") or sv["hoten"]
                ns = input("Năm sinh mới (Enter để giữ nguyên): ")
                if ns:
                    sv["namsinh"] = int(ns)
    if found:
        luu_file(ds)
        print("✏️ Đã sửa thông tin sinh viên!\n")
    else:
        print("❌ Không tìm thấy mã sinh viên.\n")

def sapxep_theo_tuoi():
    ds = doc_file()
    all_sv = []
    for lop in ds:
        for sv in lop["sinhvien"]:
            all_sv.append((lop["malop"], sv))
    all_sv.sort(key=lambda x: x[1]["namsinh"])  # năm sinh tăng dần = tuổi giảm dần
    print("📊 Danh sách sắp xếp theo năm sinh:")
    print(f"{'Lớp':<10}{'Mã SV':<10}{'Họ tên':<25}{'Năm sinh':>10}")
    print("-"*55)
    for malop, sv in all_sv:
        print(f"{malop:<10}{sv['masv']:<10}{sv['hoten']:<25}{sv['namsinh']:>10}")
    print()

# ============================
# MENU CHÍNH
# ============================
def menu():
    while True:
        print("======= QUẢN LÝ SINH VIÊN (JSON) =======")
        print("1. Thêm sinh viên")
        print("2. Xem danh sách")
        print("3. Sửa sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm")
        print("6. Sắp xếp theo năm sinh (tăng dần)")
        print("0. Thoát")
        chon = input("Chọn chức năng: ")
        if chon == "1": them_sinhvien()
        elif chon == "2": xem_danh_sach()
        elif chon == "3": sua_sinhvien()
        elif chon == "4": xoa_sinhvien()
        elif chon == "5": tim_sinhvien()
        elif chon == "6": sapxep_theo_tuoi()
        elif chon == "0":
            print("Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!\n")

if __name__ == "__main__":
    menu()
