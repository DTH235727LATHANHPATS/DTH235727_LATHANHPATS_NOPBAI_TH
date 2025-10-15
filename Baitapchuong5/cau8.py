import os

def get_filename(path):
    """
    Hàm lấy ra tên file kèm phần mở rộng
    Ví dụ: d:\\music\\muabui.mp3 -> muabui.mp3
    """
    return os.path.basename(path)

def get_name_without_extension(path):
    """
    Hàm lấy ra tên file **không có phần mở rộng**
    Ví dụ: d:\\music\\muabui.mp3 -> muabui
    """
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    return name

# Ví dụ sử dụng
path = "d:\\music\\muabui.mp3"

print("Tên file kèm đuôi:", get_filename(path))         # Output: muabui.mp3
print("Tên file không đuôi:", get_name_without_extension(path))  # Output: muabui