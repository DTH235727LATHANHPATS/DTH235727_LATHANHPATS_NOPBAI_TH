import re

def NegativeNumberInStrings(s):
    """
    Hàm nhận vào 1 chuỗi s và in ra các số nguyên âm trong chuỗi.
    """
    # Sử dụng Regular Expression để tìm các số âm
    # -\d+ nghĩa là dấu trừ theo sau bởi 1 hoặc nhiều chữ số
    negative_numbers = re.findall(r'-\d+', s)

    # In kết quả
    if negative_numbers:
        print("Các số nguyên âm trong chuỗi là:", ", ".join(negative_numbers))
    else:
        print("Không tìm thấy số nguyên âm trong chuỗi.")

# Ví dụ sử dụng
chuoi = "abc-5xyz-12k9l--p"
NegativeNumberInStrings(chuoi)
