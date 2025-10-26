def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Nhập mảng
print("Nhập các phần tử của mảng (cách nhau bởi dấu cách):")
M = list(map(int, input().split()))

# Tách số lẻ và chẵn
le = [x for x in M if x % 2 != 0]
chan = [x for x in M if x % 2 == 0]

# Tách số nguyên tố và không nguyên tố
nt = [x for x in M if CheckPrime(x)]
khong_nt = [x for x in M if not CheckPrime(x)]

# In kết quả
print("Dòng 1 - Số lẻ:", le, "→ Có", len(le), "số lẻ.")
print("Dòng 2 - Số chẵn:", chan, "→ Có", len(chan), "số chẵn.")
print("Dòng 3 - Số nguyên tố:", nt)
print("Dòng 4 - Không phải số nguyên tố:", khong_nt)