import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Màn hình đăng nhập")
        self.root.geometry("300x180")

        # Nhãn và ô nhập Username
        tk.Label(root, text="Tên đăng nhập:").pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        # Nhãn và ô nhập Password (ẩn ký tự)
        tk.Label(root, text="Mật khẩu:").pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        # Nút đăng nhập
        tk.Button(root, text="Đăng nhập", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Ví dụ kiểm tra tài khoản cứng: user="admin", pass="1234"
        if username == "admin" and password == "1234":
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
