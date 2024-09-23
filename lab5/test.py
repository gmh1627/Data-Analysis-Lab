import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 假设你有一个包含特征和分类标签的数据框
# 例如：df = pd.read_csv('your_data.csv')

# 随机生成样例数据
data = {
    'radius_mean': [10, 12, 13, 8, 9, 11, 14, 15, 7, 13],
    'texture_mean': [22, 21, 23, 20, 19, 25, 24, 22, 21, 23],
    'perimeter_mean': [88, 89, 85, 90, 87, 84, 91, 92, 80, 86],
    'area_mean': [100, 110, 120, 115, 125, 130, 105, 95, 140, 150],
    'smoothness_mean': [0.1, 0.15, 0.14, 0.12, 0.13, 0.16, 0.14, 0.11, 0.18, 0.13],
    'diagnosis': [0, 1, 0, 1, 1, 0, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

# 提取特征列
features = df.columns[:-1]  # 最后一列是分类标签

# 对数据进行标准化
scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

# 将数据转换为长格式，以便于使用seaborn绘图
df_long = df.melt(id_vars='diagnosis', var_name='features', value_name='value')

# 生成分类散点图
plt.figure(figsize=(10, 6))
sns.stripplot(x='features', y='value', hue='diagnosis', data=df_long, jitter=True, palette='coolwarm', dodge=True)
plt.xticks(rotation=45)
plt.show()
