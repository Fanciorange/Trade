
import sys,time,os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)
import random,json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from dataloader import DataProcessor
train_data_processor = DataProcessor(["test_factor_5m.json"])
test_data_processor = DataProcessor(["train_factor_5m.json"])

top_models = []

for i in range(1):
    start = time.time()
    if i==0:
        with open("/data/users/zzp/trade_data/features.json",'r')as f:
            s = f.read()
        columes = json.loads(s)
    else:
        columes = train_data_processor.get_random_factornames(-1)


    # 获取训练集和测试集
    X_train, y_train = train_data_processor.get_X_y(columes)
    X_test, y_test =  test_data_processor.get_X_y(columes)

    # 标准化数据
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test =  scaler.transform(X_test)

    # 训练 SVM 模型
    svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')
    svm_model.fit(X_train, y_train)

    # 评估模型
    ytrain_pred = svm_model.predict(X_train)
    ytest_pred =  svm_model.predict(X_test)

    accuracy1 = accuracy_score(y_test, ytest_pred)
    accuracy2 = accuracy_score(y_train, ytrain_pred)
    print(f"第{i+1}轮模型准确率: train:{accuracy1:.6f}  test:{accuracy2:.6f}")
    print("分类报告:")
    print(classification_report(y_train, ytrain_pred, digits=6))
    print(classification_report(y_test, ytest_pred, digits=6))
    print(f"耗时: {time.time()-start:.2f} 秒")



# current_file_directory = os.path.dirname(os.path.abspath(__file__))
# savedir = f"{current_file_directory}/models"
# os.makedirs(savedir,exist_ok=True)

# # 保存 top 5 模型到 models 文件夹
# for idx, (acc, model, features) in enumerate(top_models):
#     model_path = f"{savedir}/top_model_{idx+1}_acc{acc:.4f}.pkl"
#     colume_path =  f"{savedir}/top_model_{idx+1}_acc{acc:.4f}.colname"
#     joblib.dump({
#         'model': model,
#         'features': features,
#         'scaler': StandardScaler().fit(train_data_processor.get_X_y(features)[0])  # 可以额外保存 scaler
#     }, model_path)
#     print(f"已保存模型到 {model_path}")
