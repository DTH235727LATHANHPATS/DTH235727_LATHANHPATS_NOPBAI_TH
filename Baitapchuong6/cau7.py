def is_increasing(lst):
    """Hàm kiểm tra list có tăng dần không"""
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True

while True:
    print("Nhập dãy số (cách nhau bằng dấu cách):")
    lst = list(map(int, input().split()))
    
    if is_increasing(lst):
        break
    else:
        print(" Dãy không tăng dần! Vui lòng nhập lại.\n")

print(" Dãy số tăng dần hợp lệ là:")
print(lst)