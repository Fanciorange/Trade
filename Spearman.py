import os
import matplotlib.pyplot as plt
import scipy.stats as stats
from dataloader import DataProcessor  # 确保 dataloader.py 与本文件在同一目录

# ==== 加载数据 ====
dataprocessor = DataProcessor(["train_factor_r1.json"])
factorls = dataprocessor.get_random_factornames(k=-1)  # 使用全部特征
#X, y = dataprocessor.get_X_y(factorls)
X = dataprocessor.get_X(factorls)
y = dataprocessor.get_X("rise_ratio")

# 显示数据形状
print(f"数据特征矩阵形状: {X.shape}")
print(f"标签向量形状: {y.shape}")

# 创建保存图片的目录
os.makedirs("images", exist_ok=True)

# ==== 计算所有特征的相关系数 ====
correlations = []
for i, feature_name in enumerate(factorls):
    feature_values = X[:, i]
    corr, p_value = stats.pearsonr(feature_values, y)
    correlations.append((feature_name, corr, p_value))

# ==== 选出相关系数绝对值最高的前10个特征 ====
top_corrs = sorted(correlations, key=lambda x: abs(x[1]), reverse=True)[:10]

print("\n相关系数排名前 10 的特征：")
for i, (fname, corr, pval) in enumerate(top_corrs, 1):
    print(f"{i}. {fname:30s}  相关系数: {corr:.4f}  P值: {pval:.2e}")

# ==== 绘图并保存 ====
for fname, corr, _ in top_corrs:
    idx = factorls.index(fname)
    feature_values = X[:, idx]

    plt.figure(figsize=(8, 5))
    plt.scatter(feature_values, y, alpha=0.7)
    plt.title(f"{fname} vs Label\nPearson Corr = {corr:.4f}")
    plt.xlabel(fname)
    plt.ylabel("Label")
    plt.grid(True)
    plt.tight_layout()

    filename = f"images/{fname}.png"
    plt.savefig(filename)
    plt.close()
    print(f"已保存图像: {filename}")
