def optimize_string(s):
    # Bước 1: loại bỏ khoảng trắng đầu và cuối
    s = s.strip()
    
    # Bước 2: chia chuỗi thành các từ, tự động loại bỏ khoảng trắng dư thừa
    words = s.split()
    
    # Bước 3: viết hoa chữ cái đầu mỗi từ
    optimized_words = [word.capitalize() for word in words]
    
    # Bước 4: ghép lại chuỗi bằng 1 khoảng trắng
    optimized_string = " ".join(optimized_words)
    
    return optimized_string

# Ví dụ sử dụng
input_str = " TRần duY thAnH "
output_str = optimize_string(input_str)
print("Output:", output_str)