import torch
import json
import numpy as np
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from model import Model  # 假设你有一个自定义模型类
import sys
import time
import os

# 获取项目根目录路径并添加到系统路径中
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from dataloader import DataProcessor  # 假设这是你的数据处理器

# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)

# 获取当前文件的目录
current_dir = os.path.dirname(current_file_path)

# 数据加载与预处理
train_data_processor = DataProcessor(["train_factor_1.json", "train_factor_2.json"])
test_data_processor = DataProcessor(["test_factor.json"])

device = "cuda" if torch.cuda.is_available() else "cpu"  # 确保兼容性

input_dim = 100  # 假设输入特征的数量是100
factornames = train_data_processor.get_random_factornames(input_dim)

train_X, train_y = train_data_processor.get_X_y(factornames)
test_X, test_y = test_data_processor.get_X_y(factornames)

# 数据标准化
mean = train_X.mean(axis=0)
std = train_X.std(axis=0)
std[std == 0] = 1e-8  # 防止除以零
train_X = (train_X - mean) / std
test_X = (test_X - mean) / std

# 创建模型实例
model = Model(input_dim, 1024).to(device)

# 使用BCEWithLogitsLoss，假设输出需要经过sigmoid激活函数
criterion = nn.BCEWithLogitsLoss()

# 使用AdamW优化器
optimizer = torch.optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)  # 示例学习率和权重衰减

# 准备数据集
features = torch.from_numpy(train_X.astype(np.float32))  # 将训练特征转换为 PyTorch 张量，并确保是 float32 类型
labels = torch.from_numpy(train_y).float()
labels = labels.view(-1, 1)
dataset = TensorDataset(features, labels)
dataloader = DataLoader(dataset, batch_size=200, shuffle=True)

# 训练模型
epochs = 200
print("Start training")
for epoch in range(epochs):
    for i, (inputs, targets) in enumerate(dataloader):
        inputs, targets = inputs.to(device), targets.to(device)
        
        optimizer.zero_grad()  # 清除过往梯度
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()  # 反向传播
        optimizer.step()  # 更新权重

    print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item()}')

print("Training complete")

# 保存模型参数到文件
save_path = os.path.join(current_dir, 'mlp_model_state_dict.pth')
torch.save(model.state_dict(), save_path)
with open(os.path.join(current_dir, 'factors.json'), 'w') as f:
    json.dump(factornames, f, indent=4)
print("Model parameters have been saved")