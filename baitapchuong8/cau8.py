import tkinter as tk
from tkinter import messagebox

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Chuyển đổi Độ F sang Độ C")
        self.root.geometry("300x150")

        # Label và Entry nhập độ F
        tk.Label(root, text="Nhập độ F:").pack(pady=5)
        self.f_entry = tk.Entry(root)
        self.f_entry.pack(pady=5)

        # Nút chuyển đổi
        tk.Button(root, text="Chuyển đổi", command=self.convert).pack(pady=10)

        # Label hiển thị kết quả
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack()

    def convert(self):
        try:
            f = float(self.f_entry.get())
            c = (f - 32) * 5 / 9
            self.result_label.config(text=f"Độ C tương ứng: {c:.2f} °C")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho độ F")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()
