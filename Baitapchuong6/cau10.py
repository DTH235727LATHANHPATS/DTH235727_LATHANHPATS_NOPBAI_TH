def nhap_matrix(name):
    print(f"Nhập ma trận {name}:")
    m = int(input(f"  Nhập số hàng của {name}: "))
    n = int(input(f"  Nhập số cột của {name}: "))
    
    matrix = []
    for i in range(m):
        hang = list(map(float, input(f"  Nhập hàng {i+1} (các phần tử cách nhau bằng dấu cách): ").split()))
        while len(hang) != n:
            print("  ❌ Sai số lượng cột, vui lòng nhập lại!")
            hang = list(map(float, input(f"  Nhập lại hàng {i+1}: ").split()))
        matrix.append(hang)
    return matrix

# Hàm in ma trận
def xuat_matrix(M, name):
    print(f"\nMa trận {name}:")
    for hang in M:
        print(hang)

# Hàm cộng hai ma trận
def cong_matrix(A, B):
    m, n = len(A), len(A[0])
    C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
    return C

# Hàm hoán vị (transpose)
def hoan_vi(M):
    # Dùng zip(*) để hoán vị hàng ↔ cột
    return [list(hang) for hang in zip(*M)]

# ================== Chương trình chính ==================

# Nhập 2 ma trận A và B
A = nhap_matrix("A")
B = nhap_matrix("B")

# Kiểm tra điều kiện cộng ma trận (cùng kích thước)
if len(A) != len(B) or len(A[0]) != len(B[0]):
    print("\n Hai ma trận không cùng kích thước, không thể cộng!")
else:
    C = cong_matrix(A, B)
    xuat_matrix(A, "A")
    xuat_matrix(B, "B")
    xuat_matrix(C, "A + B")

# Hoán vị A và B
A_T = hoan_vi(A)
B_T = hoan_vi(B)
xuat_matrix(A_T, "A hoán vị")
xuat_matrix(B_T, "B hoán vị")