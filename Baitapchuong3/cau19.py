import math

def tinh_giai_thua(k):
    """
    Tính giai thừa của một số k (k!)
    """
    # math.factorial(k) có sẵn trong thư viện math, nhưng ta có thể tự xây dựng 
    # để dễ hiểu hơn, hoặc dùng luôn hàm có sẵn.
    # Tuy nhiên, trong bài toán này ta sẽ dùng math.factorial cho ngắn gọn và hiệu quả.
    return math.factorial(k)
    
def tinh_tong_S(x, n):
    """
    Tính tổng S(x, n) = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!
    """
    S = 0.0  # Khởi tạo tổng S
    
    # Vòng lặp tính tổng các số lẻ từ 1 đến 2n + 1
    # i sẽ nhận các giá trị: 1, 3, 5, ..., 2n + 1
    for i in range(1, 2 * n + 2, 2):
        # Số mũ và mẫu giai thừa là i
        tu_so = x ** i
        mau_so = tinh_giai_thua(i)
        
        # Cộng phần tử vào tổng
        S += tu_so / mau_so
        
    return S

# --- Chương trình chính ---
try:
    # Nhập x và n
    x = float(input("Nhập giá trị x: "))
    n = int(input("Nhập số nguyên dương n: "))
    
    if n < 0:
        print("Lỗi: n phải là số nguyên dương hoặc 0.")
    else:
        # Tính và in kết quả
        ket_qua = tinh_tong_S(x, n)
        print(f"\nTổng S({x}, {n}) = {ket_qua}")

except ValueError:
    print("\nLỗi: Đầu vào không hợp lệ. Vui lòng nhập số cho x và số nguyên cho n.")
