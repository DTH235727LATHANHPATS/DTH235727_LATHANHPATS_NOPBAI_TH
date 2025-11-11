import tkinter as tk
from tkinter import messagebox

# Danh sách Can và Chi trong chu kỳ 60 năm
CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu",
       "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]

CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ",
       "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

def duong_lich_sang_am_lich(year):
    # Tính Can
    can_index = (year + 6) % 10
    # Tính Chi
    chi_index = (year + 8) % 12
    return CAN[can_index] + " " + CHI[chi_index]

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Chuyển năm Dương lịch sang Âm lịch")
        self.root.geometry("350x150")

        tk.Label(root, text="Nhập năm Dương lịch:").pack(pady=10)
        self.year_entry = tk.Entry(root)
        self.year_entry.pack()

        tk.Button(root, text="Chuyển đổi", command=self.convert).pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack()

    def convert(self):
        try:
            year = int(self.year_entry.get())
            if year <= 0:
                raise ValueError("Năm phải lớn hơn 0")
            am_lich = duong_lich_sang_am_lich(year)
            self.result_label.config(text=f"Năm Âm lịch: {am_lich}")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập năm Dương lịch hợp lệ (số nguyên dương)")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
