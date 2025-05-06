import joblib
import sys
import time
import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from dataloader import DataProcessor
from sklearn.metrics import accuracy_score, classification_report

# 指定模型路径（随机森林模型）
modelpath = ""

# 加载模型及相关对象
loaded_objects = joblib.load(modelpath)

# 提取模型、特征列表和标准化器
model = loaded_objects['model']
features = loaded_objects['features']
scaler = loaded_objects['scaler']

print("使用的特征列表：", features)

# 加载测试数据
test_data_processor = DataProcessor(["test_factor.json"], isTrain=False)
X_test, y_test = test_data_processor.get_X_y(features)

# 特征标准化（即使随机森林不需要，也可保留保持一致性）
X_test = scaler.transform(X_test)

# 评估模型
start_time = time.time()
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy:.6f}")
print("分类报告:")
print(classification_report(y_test, y_pred, digits=6))
print(f"预测耗时: {time.time() - start_time:.2f} 秒")