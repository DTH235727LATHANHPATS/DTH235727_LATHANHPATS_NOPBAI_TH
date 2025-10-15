'''
1️ Hàm kiểm tra
Hàm	Mô tả	Ví dụ
str.isalpha()	Kiểm tra tất cả ký tự đều là chữ cái	"abc".isalpha() → True
str.isdigit()	Kiểm tra tất cả ký tự đều là số	"123".isdigit() → True
str.isalnum()	Kiểm tra tất cả ký tự là chữ hoặc số	"abc123".isalnum() → True
str.islower()	Kiểm tra chuỗi toàn chữ thường	"abc".islower() → True
str.isupper()	Kiểm tra chuỗi toàn chữ hoa	"ABC".isupper() → True
str.isspace()	Kiểm tra chuỗi toàn khoảng trắng	" ".isspace() → True
2️ Hàm đổi chữ hoa – chữ thường
Hàm	Mô tả	Ví dụ
str.upper()	Chuyển tất cả ký tự thành chữ hoa	"abc".upper() → "ABC"
str.lower()	Chuyển tất cả ký tự thành chữ thường	"ABC".lower() → "abc"
str.title()	Viết hoa ký tự đầu mỗi từ	"hello world".title() → "Hello World"
str.capitalize()	Viết hoa ký tự đầu tiên	"hello".capitalize() → "Hello"
3️ Hàm tìm kiếm
Hàm	Mô tả	Ví dụ
str.find(sub)	Trả về vị trí đầu tiên của sub, không tìm thấy trả về -1	"hello".find("e") → 1
str.index(sub)	Tương tự find nhưng nếu không tìm thấy sẽ báo lỗi	"hello".index("e") → 1
str.count(sub)	Đếm số lần xuất hiện của sub	"hello".count("l") → 2
4️ Hàm cắt, nối và thay thế
Hàm	Mô tả	Ví dụ
str.split(sep)	Chia chuỗi thành list theo sep	"a,b,c".split(",") → ["a","b","c"]
str.join(list)	Nối các phần tử list thành chuỗi	",".join(["a","b","c"]) → "a,b,c"
str.replace(old, new)	Thay thế chuỗi old bằng new	"hello".replace("l","x") → "hexxo"
5️ Hàm loại bỏ khoảng trắng
Hàm	Mô tả	Ví dụ
str.strip()	Bỏ khoảng trắng ở đầu và cuối chuỗi	" hello ".strip() → "hello"
str.lstrip()	Bỏ khoảng trắng bên trái	" hello".lstrip() → "hello"
str.rstrip()	Bỏ khoảng trắng bên phải	"hello ".rstrip() → "hello"
6️ Một số hàm tiện ích khác
Hàm	Mô tả	Ví dụ
len(str)	Độ dài chuỗi	len("hello") → 5
str.startswith(prefix)	Kiểm tra bắt đầu bằng prefix	"hello".startswith("he") → True
str.endswith(suffix)	Kiểm tra kết thúc bằng suffix	"hello".endswith("lo") → True
str[::-1]	Đảo ngược chuỗi	"hello"[::-1] → "olleh"
'''