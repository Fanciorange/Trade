import sys, time, os
import random, json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from dataloader import DataProcessor

# 加载数据
train_data_processor = DataProcessor(["train_factor_1_steady.json"])
test_data_processor = DataProcessor(["test_factor_1_steady.json"])

columes = train_data_processor.get_random_factornames(-1)

# 构建训练集和测试集
X_train = train_data_processor.get_X(columes)
y_train = train_data_processor.get_X("up_num") / 300
X_test = test_data_processor.get_X(columes)
y_test = test_data_processor.get_X("up_num") / 300

# 标准化数据
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 定义多个回归模型
models = {
    "SVR": SVR(kernel='rbf', C=1.0, gamma='scale'),
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
    "GradientBoosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42),
    "LinearRegression": LinearRegression(),
    "MLPRegressor": MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
}

# 遍历并训练每个模型
for name, model in models.items():
    print(f"\n训练模型: {name}")
    start = time.time()

    model.fit(X_train, y_train)

    ytrain_pred = model.predict(X_train)
    ytest_pred = model.predict(X_test)

    mse_train = mean_squared_error(y_train, ytrain_pred)
    mae_train = mean_absolute_error(y_train, ytrain_pred)
    r2_train = r2_score(y_train, ytrain_pred)

    mse_test = mean_squared_error(y_test, ytest_pred)
    mae_test = mean_absolute_error(y_test, ytest_pred)
    r2_test = r2_score(y_test, ytest_pred)

    print(f"Train -> MSE: {mse_train:.6f}, MAE: {mae_train:.6f}, R²: {r2_train:.6f}")
    print(f"Test  -> MSE: {mse_test:.6f}, MAE: {mae_test:.6f}, R²: {r2_test:.6f}")
    print(f"总耗时: {time.time()-start:.2f} 秒\n")

