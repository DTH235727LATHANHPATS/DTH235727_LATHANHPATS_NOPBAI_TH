import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator đơn giản")
        self.root.geometry("300x400")

        self.expression = ""

        # Hiển thị
        self.text_display = tk.Entry(root, font=("Arial", 20), bd=5, relief="sunken", justify="right")
        self.text_display.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # Khung chứa các nút
        btns_frame = tk.Frame(root)
        btns_frame.pack()

        # Danh sách nút (text, hàng, cột)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)  # Nút bằng kéo dài 4 cột
        ]

        for (text, row, col, colspan) in [(*btn, 1) if len(btn)==3 else btn for btn in buttons]:
            action = self.clear if text == 'C' else \
                     self.evaluate if text == '=' else \
                     lambda x=text: self.add_to_expression(x)
            btn = tk.Button(btns_frame, text=text, width=5, height=2, font=("Arial", 18), command=action)
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        # Cấu hình kích thước hàng và cột để nút tự mở rộng
        for i in range(6):
            btns_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btns_frame.columnconfigure(j, weight=1)

    def add_to_expression(self, char):
        self.expression += char
        self.text_display.delete(0, tk.END)
        self.text_display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.text_display.delete(0, tk.END)

    def evaluate(self):
        try:
            # Đánh giá biểu thức an toàn hơn là dùng eval trực tiếp
            result = str(eval(self.expression))
            self.text_display.delete(0, tk.END)
            self.text_display.insert(tk.END, result)
            self.expression = result
        except:
            self.text_display.delete(0, tk.END)
            self.text_display.insert(tk.END, "Lỗi")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
