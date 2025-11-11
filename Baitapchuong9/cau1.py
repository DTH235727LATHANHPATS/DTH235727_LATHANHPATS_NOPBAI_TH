import numpy as np
from sklearn.linear_model import LinearRegression

# Dữ liệu chiều cao (X) và cân nặng (y) từ bảng cho sẵn
heights = np.array([147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]).reshape(-1, 1)
weights = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

# Tạo mô hình hồi quy tuyến tính
model = LinearRegression()

# Huấn luyện mô hình
model.fit(heights, weights)

def predict_weight(height_cm):
    # Dự báo cân nặng từ chiều cao
    height_arr = np.array([[height_cm]])
    weight_pred = model.predict(height_arr)
    return weight_pred[0]

if __name__ == "__main__":
    while True:
        try:
            input_height = input("Nhập chiều cao (cm), hoặc gõ 'exit' để thoát: ")
            if input_height.lower() == 'exit':
                break
            height_val = float(input_height)
            weight_val = predict_weight(height_val)
            print(f"Dự báo cân nặng với chiều cao {height_val} cm là: {weight_val:.2f} kg\n")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
