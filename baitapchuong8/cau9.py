import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy tính BMI")
        self.root.geometry("350x250")

        # Cân nặng
        tk.Label(root, text="Cân nặng (kg):").pack(pady=5)
        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        # Chiều cao
        tk.Label(root, text="Chiều cao (cm):").pack(pady=5)
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        # Nút tính BMI
        tk.Button(root, text="Tính BMI", command=self.calculate_bmi).pack(pady=15)

        # Label hiển thị kết quả
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack()

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height_cm = float(self.height_entry.get())
            if weight <= 0 or height_cm <= 0:
                raise ValueError("Cân nặng và chiều cao phải lớn hơn 0")

            height_m = height_cm / 100
            bmi = weight / (height_m ** 2)

            category = self.bmi_category(bmi)

            self.result_label.config(text=f"BMI của bạn: {bmi:.2f}\nPhân loại: {category}")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ và lớn hơn 0 cho cân nặng và chiều cao")

    def bmi_category(self, bmi):
        if bmi < 18.5:
            return "Gầy"
        elif bmi < 25:
            return "Bình thường"
        elif bmi < 30:
            return "Thừa cân"
        else:
            return "Béo phì"

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
