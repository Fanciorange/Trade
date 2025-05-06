from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import sys
import time
import os
from sklearn.ensemble import RandomForestClassifier

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

import random
import joblib,json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from dataloader import DataProcessor

train_data_processor = DataProcessor(["train_factor_1.json", "train_factor_2.json"])
test_data_processor = DataProcessor(["test_factor.json"])

# 假设X是你包含200个特征的数据，y是目标变量
# X, y = make_classification(n_samples=1000, n_features=200, n_informative=100, n_classes=2, random_state=1)

# 创建随机森林分类器实例
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

factors = train_data_processor.get_random_factornames(-1)
X_train, y_train = train_data_processor.get_X_y(factors)
# 训练模型
rf_model.fit(X_train, y_train)

# 获取特征重要性
importances = rf_model.feature_importances_

# 将特征重要性与特征名称对应起来（如果有的话），然后按重要性排序
feature_names = [f'feature_{i}' for i in range(len(factors))]  # 如果有实际特征名，替换这里的逻辑
sorted_indices = importances.argsort()[::-1]

# 打印或保存最重要的100个特征
important_features = [(feature_names[index], importances[index]) for index in sorted_indices[:100]]

features = [factors[index] for index in sorted_indices]
print(important_features)
with open("features.json",'w')as f:
    f.write(json.dumps(features))