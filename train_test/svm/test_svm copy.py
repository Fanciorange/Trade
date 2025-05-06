import joblib

import sys,time,os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)
from dataloader import DataProcessor
from sklearn.metrics import accuracy_score, classification_report

modelpath ="/data/users/zzp/trade_data/train_test/svm/models/top_model_1_acc0.8576.pkl"
datafile_path = ["train_factor_1.json","train_factor_2.json"]
def split_true_false_data(modelpath):
    
    # 假设 model_path 是你保存模型的路径
    loaded_objects = joblib.load(modelpath)

    # 提取保存的对象
    model = loaded_objects['model']
    features = loaded_objects['features']
    scaler = loaded_objects['scaler']

    test_data_processor = DataProcessor(datafile_path,isTrain=0)
    X_test,y_test = test_data_processor.get_X_y(features)

    X_test = scaler.transform(X_test)

    y_pred = model.predict(X_test)
    y_test == y_pred
    
    accuracy = accuracy_score(y_test, y_pred)
    print(f"模型准确率: {accuracy:.6f}")
    print("分类报告:")
    print(classification_report(y_test, y_pred, digits=6))


