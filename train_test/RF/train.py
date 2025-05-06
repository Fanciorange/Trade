import sys
import time
import os
from sklearn.ensemble import RandomForestClassifier

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

import random,json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from dataloader import DataProcessor

train_data_processor = DataProcessor(["train_factor_1.json", "train_factor_2.json"])
test_data_processor = DataProcessor(["test_factor.json"])

top_models = []
with open("/data/users/zzp/trade_data/features.json",'r')as f:
    s = f.read()
columns = json.loads(s)
for i in range(20):
    start = time.time()
    if i==0:
        with open("/data/users/zzp/trade_data/features.json",'r')as f:
            s = f.read()
            columns = json.loads(s)
    else:
        columns = train_data_processor.get_random_factornames(100)

    # 获取训练集和测试集
    X_train, y_train = train_data_processor.get_X_y(columns)
    X_test, y_test = test_data_processor.get_X_y(columns)

    # 标准化数据（虽然随机森林不需要标准化，但为了统一可以保留）
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 训练随机森林模型
    rf_model = RandomForestClassifier(
        n_estimators=100,   # 决策树数量
        max_depth=None,     # 树深度不限
        random_state=42     # 固定随机种子便于复现
    )
    rf_model.fit(X_train, y_train)

    # 评估模型
    y_pred = rf_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"第{i+1}轮模型准确率: {accuracy:.6f}")
    print("分类报告:")
    print(classification_report(y_test, y_pred, digits=6))
    print(f"耗时: {time.time()-start:.2f} 秒")

    # 添加当前模型到 top_models 列表中
    top_models.append((accuracy, rf_model, columns))

    # 只保留前 5 个准确率最高的模型
    top_models.sort(reverse=True, key=lambda x: x[0])
    if len(top_models) > 5:
        top_models.pop()


current_file_directory = os.path.dirname(os.path.abspath(__file__))
savedir = f"{current_file_directory}/models"
os.makedirs(savedir, exist_ok=True)

# 保存 top 5 模型到 models 文件夹
for idx, (acc, model, features) in enumerate(top_models):
    model_path = f"{savedir}/top_model_{idx+1}_acc{acc:.4f}.pkl"
    joblib.dump({
        'model': model,
        'features': features,
        'scaler': StandardScaler().fit(train_data_processor.get_X_y(features)[0])  # 可以额外保存 scaler
    }, model_path)
    print(f"已保存模型到 {model_path}")