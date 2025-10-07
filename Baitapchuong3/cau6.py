print("Nhập vào một số n có tối đa hai chữ số")
n = int(input("Nhập số n (0-99): "))
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

if n < 10:
    print(chu_so[n])
else:
    chuc = n // 10
    donvi = n % 10

    if chuc == 1:
        doc = "mười"
    else:
        doc = chu_so[chuc] + " mươi"

    if donvi == 0:
        pass
    elif donvi == 1:
        if chuc == 1:
            doc += " một"
        else:
            doc += " mốt"
    elif donvi == 5:
        doc += " lăm"
    else:
        doc += " " + chu_so[donvi]

    print(doc)