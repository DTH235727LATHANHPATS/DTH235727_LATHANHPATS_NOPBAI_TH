import time
import os

# 4 hình bạn muốn hiển thị (có thể thay bằng hình thật trong đề)
hinh1 = """
   *
  * *
 * * *
* * * *
"""
hinh2 = """
  *  
 * * 
*   *
 * * 
  *  
"""
hinh3 = """
*****
*   *
*   *
*****
"""
hinh4 = """
*   *
 * * 
  *  
 * * 
*   *
"""

# Danh sách các hình
cac_hinh = [hinh1, hinh2, hinh3, hinh4]

# Lặp qua từng hình
for h in cac_hinh:
    os.system('cls' if os.name == 'nt' else 'clear')  # Xoá màn hình (tùy hệ điều hành)
    print(h)
    time.sleep(5)  # Dừng 5 giây