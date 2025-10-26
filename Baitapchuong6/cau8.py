# Nhập số phần tử
n = int(input("Nhập số phần tử n: "))

# Nhập dãy n số thực
M = []
for i in range(n):
    x = float(input(f"Nhập M[{i}]: "))
    M.append(x)

print("Dãy số ban đầu là:")
print(M)

# Sắp xếp giảm dần
M.sort(reverse=True)

print("Dãy số sau khi sắp xếp giảm dần:")
print(M)