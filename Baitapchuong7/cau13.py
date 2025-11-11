import tkinter as tk
from tkinter import ttk, messagebox
import xml.etree.ElementTree as ET
from collections import defaultdict

# ====== HÀM ĐỌC NHÓM THIẾT BỊ ======
def read_groups(file_path="nhomthietbi.xml"):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        groups = []
        for nhom in root.findall("nhom"):
            ma = nhom.find("ma").text
            ten = nhom.find("ten").text
            groups.append((ma, ten))
        return groups
    except Exception as e:
        messagebox.showerror("Lỗi đọc nhóm", str(e))
        return []

# ====== HÀM ĐỌC THIẾT BỊ ======
def read_devices(file_path="thietbi.xml"):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        devices = []
        for tb in root.findall("thietbi"):
            manhom = tb.get("manhom")
            ma = tb.find("ma").text
            ten = tb.find("ten").text
            devices.append((ma, ten, manhom))
        return devices
    except Exception as e:
        messagebox.showerror("Lỗi đọc thiết bị", str(e))
        return []

# ====== CHƯƠNG TRÌNH CHÍNH ======
class ThietBiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý Thiết Bị (XML)")
        self.root.geometry("700x500")

        # Dữ liệu
        self.groups = read_groups()
        self.devices = read_devices()

        # ====== GIAO DIỆN ======
        frame_top = tk.Frame(root)
        frame_top.pack(pady=10)

        tk.Label(frame_top, text="Chọn nhóm thiết bị:").grid(row=0, column=0, padx=5)
        self.group_var = tk.StringVar()
        self.cbo_group = ttk.Combobox(frame_top, textvariable=self.group_var, width=25)
        self.cbo_group["values"] = ["-- Tất cả --"] + [f"{ma} - {ten}" for ma, ten in self.groups]
        self.cbo_group.current(0)
        self.cbo_group.grid(row=0, column=1)

        tk.Button(frame_top, text="Hiển thị nhóm", command=self.show_groups).grid(row=0, column=2, padx=5)
        tk.Button(frame_top, text="Hiển thị thiết bị", command=self.show_devices).grid(row=0, column=3, padx=5)
        tk.Button(frame_top, text="Lọc theo nhóm", command=self.filter_by_group).grid(row=0, column=4, padx=5)
        tk.Button(frame_top, text="Nhóm nhiều thiết bị nhất", command=self.most_devices_group).grid(row=0, column=5, padx=5)

        # ====== BẢNG HIỂN THỊ ======
        columns = ("Mã", "Tên", "Mã Nhóm")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200, anchor="center")
        self.tree.pack(fill="both", expand=True, pady=10)

    # ====== HIỂN THỊ NHÓM ======
    def show_groups(self):
        self.tree.delete(*self.tree.get_children())
        for ma, ten in self.groups:
            self.tree.insert("", "end", values=(ma, ten, ""))

    # ====== HIỂN THỊ THIẾT BỊ ======
    def show_devices(self):
        self.tree.delete(*self.tree.get_children())
        for ma, ten, manhom in self.devices:
            self.tree.insert("", "end", values=(ma, ten, manhom))

    # ====== LỌC THEO NHÓM ======
    def filter_by_group(self):
        selected = self.group_var.get()
        if selected == "-- Tất cả --":
            self.show_devices()
            return
        if "-" not in selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn nhóm hợp lệ.")
            return

        ma_nhom = selected.split(" - ")[0]
        filtered = [tb for tb in self.devices if tb[2] == ma_nhom]
        self.tree.delete(*self.tree.get_children())
        for ma, ten, manhom in filtered:
            self.tree.insert("", "end", values=(ma, ten, manhom))

    # ====== NHÓM CÓ NHIỀU THIẾT BỊ NHẤT ======
    def most_devices_group(self):
        count = defaultdict(int)
        for _, _, manhom in self.devices:
            count[manhom] += 1
        if not count:
            messagebox.showinfo("Kết quả", "Không có dữ liệu thiết bị.")
            return

        max_group = max(count, key=count.get)
        max_count = count[max_group]
        ten_nhom = next((ten for ma, ten in self.groups if ma == max_group), "Không rõ")

        messagebox.showinfo("Kết quả", f"Nhóm nhiều thiết bị nhất: {ten_nhom} ({max_count} thiết bị)")

# ====== CHẠY CHƯƠNG TRÌNH ======
if __name__ == "__main__":
    root = tk.Tk()
    app = ThietBiApp(root)
    root.mainloop()
