import tkinter as tk
from tkinter import ttk

def show_styles():
    root = tk.Tk()
    root.title("Demo các style của Button trong ttk")

    style = ttk.Style(root)
    styles = style.theme_names()  # Danh sách theme có sẵn
    print("Themes có sẵn:", styles)

    # Dùng theme hiện tại
    current_theme = style.theme_use()
    ttk.Label(root, text=f"Theme hiện tại: {current_theme}").pack(pady=5)

    # Một số style mặc định của ttk.Button:
    button_styles = [
        "TButton",      # Default
        "Toolbutton",   # Nhỏ, như nút toolbar
        "ToggleButton", # Nút bật tắt (cần custom thêm)
        "Link.TButton", # Nút kiểu link (màu xanh dương)
    ]

    for st in button_styles:
        try:
            b = ttk.Button(root, text=st, style=st)
            b.pack(padx=10, pady=5, fill="x")
        except tk.TclError:
            # Nếu style không có sẵn sẽ lỗi
            print(f"Style {st} không có sẵn")

    root.mainloop()

if __name__ == "__main__":
    show_styles()
