import pandas as pd
import matplotlib.pyplot as plt
import os

# 确保输出目录存在
os.makedirs("results", exist_ok=True)

# 读取数据
df = pd.read_csv("data/ev_data_sample.csv")

# 计算温度 vs 续航损失
df["loss_percent"] = (df["baseline_range_km"] - df["measured_range_km"]) / df["baseline_range_km"] * 100

# 打印平均损失
print("平均续航损失: %.1f%%" % df["loss_percent"].mean())

# 绘制图表
plt.figure(figsize=(8,5))
plt.scatter(df["ambient_temp_C"], df["loss_percent"], c=df["cabin_heating_on"], cmap="coolwarm", label="Heating")
plt.xlabel("Ambient Temperature (°C)")
plt.ylabel("Range Loss (%)")
plt.title("EV Range Loss vs Temperature")
plt.colorbar(label="Cabin Heating On (0=No, 1=Yes)")
plt.savefig("results/range_loss.png")
print("图表已保存到 results/range_loss.png")
