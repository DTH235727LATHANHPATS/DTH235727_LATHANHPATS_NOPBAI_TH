import random

N = int(input("Nhập số phần tử N: "))
lst = []

while len(lst) < N:
    x = random.randrange(-100, 100)
    if x not in lst:       # đảm bảo không trùng
        lst.append(x)

print("List ngẫu nhiên không trùng là:")
print(lst)
