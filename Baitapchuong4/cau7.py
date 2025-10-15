import math

def distance(xa, ya, xb, yb):
    # sử dụng math.hypot để tránh làm thủ công căn bậc hai
    return math.hypot(xb - xa, yb - ya)

def main():
    # cách nhập 1: nhập 2 số trên 1 dòng (xa ya), 1 dòng tiếp (xb yb)
    xa, ya = map(float, input("Nhập xA yA (cách nhau bằng khoảng trắng): ").split())
    xb, yb = map(float, input("Nhập xB yB (cách nhau bằng khoảng trắng): ").split())

    d = distance(xa, ya, xb, yb)
    print(f"Độ dài đoạn AB = {d:.4f}")   # in đến 4 chữ số thập phân

if __name__ == "__main__":
    main()