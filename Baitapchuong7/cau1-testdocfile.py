def LuuFile(path, data):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data + "\n")
    file.close()

def DocFile(path):
    arrProduct = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()
        arr = data.split(';')
        arrProduct.append(arr)
    file.close()   # ← phải nằm ngoài for
    return arrProduct
