import joblib

import sys,time,os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)
from dataloader import DataProcessor
from sklearn.metrics import accuracy_score, classification_report

modelpath ="/data/users/zzp/trade_data/train_test/svm/models/top_model_1_acc0.5326.pkl"
# 假设 model_path 是你保存模型的路径
loaded_objects = joblib.load(modelpath)

# 提取保存的对象
model = loaded_objects['model']
features = loaded_objects['features']
scaler = loaded_objects['scaler']

print(features)

test_data_processor = DataProcessor(["test_factor.json"],isTrain=0)
X_test,y_test = test_data_processor.get_X_y(features)

X_test = scaler.transform(X_test)


# 评估模型
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy:.6f}")
print("分类报告:")
print(classification_report(y_test, y_pred, digits=6))


