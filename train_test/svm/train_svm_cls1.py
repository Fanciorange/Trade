
import sys,time,os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)
import random
import numpy as 
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from dataloader import DataProcessor
train_data_processor = DataProcessor(["train_factor_1.json","train_factor_2.json"])


modelpath ="/data/users/zzp/trade_data/train_test/svm/models/top_model_1_acc0.5326.pkl"
# 假设 model_path 是你保存模型的路径
loaded_objects = joblib.load(modelpath)

# 提取保存的对象
model = loaded_objects['model']
features = loaded_objects['features']
scaler = loaded_objects['scaler']

X_train,y_train = train_data_processor.get_X_y(features)

X_train = scaler.transform(X_train)


# 评估模型
y_pred = model.predict(X_train)

accuracy = accuracy_score(y_train, y_pred)
print(f"模型准确率: {accuracy:.6f}")
print("分类报告:")
print(classification_report(y_train, y_pred, digits=6))



y = y_train==y_pred
coordinates = np.argwhere(y)