# 定義一個函數來計算BMI
def calculate_bmi(height, weight):
    height_m = height / 100  # 將身高轉換為米
    bmi = weight / (height_m ** 2)  # 計算BMI
    return bmi

# 使用者輸入身高和體重
height = float(input("請輸入您的身高（cm）："))
weight = float(input("請輸入您的體重（kg）："))

# 計算BMI並輸出結果
bmi = calculate_bmi(height, weight)
print("您的BMI是：", bmi)