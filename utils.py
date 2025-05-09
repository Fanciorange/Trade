import joblib
import sys,time,os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)
from dataloader import DataProcessor
from sklearn.metrics import accuracy_score, classification_report
from analyse import Analysis


modelpath ="/data/users/zzp/trade_data/train_test/svm/models/top_model_1_acc0.8576.pkl"
# 假设 model_path 是你保存模型的路径
loaded_objects = joblib.load(modelpath)

# 提取保存的对象
model = loaded_objects['model']
features = loaded_objects['features']
scaler = loaded_objects['scaler']


def execute_all_methods(cls,instance=None):
    # 如果没有传入实例，则创建一个实例
    if instance is None:
        instance = cls()

    # 获取类中所有方法（排除私有方法和特殊方法）
    methods = [
        method_name for method_name, method_obj in inspect.getmembers(cls, predicate=inspect.isfunction)
        if not method_name.startswith("_")  # 排除私有方法和特殊方法
    ]
     
    ignore_name =['Aroon_2', 'BBANDS_3', 'HT_PHASOR', 'HT_SINE', 'MACDFIX_3', 
                  'MACD_3', 'MININDEX', 'STOCH', 'STOCHF', 'STOCHRSI', 'STOCH_2']
    res ={}
    for method_name in methods:
        if method_name in ignore_name:
            continue
        method = getattr(instance, method_name)
        vals = method().item()
        res[method_name] = vals
        
    return res

def reorganize_stock_data(df,tp="s"):
    if tp == "s":
        k = 15
    elif tp =='d':
        k=3600*24
    elif tp == 'm':
        k = 60
    elif tp =='h':
        k = 3600
    # 确保数据按时间顺序排列（假设索引是时间顺序）
    df = df.sort_index()  # 如果索引不是时间戳，可能需要按时间列排序
    # 创建分组键（每15秒为一组）
    df['group'] = df.index // k  # 基于索引分组（假设索引从0开始连续）
    
    # 定义聚合规则（假设价格列名为'price'，成交量为'volume'）
    agg_dict = {
        'open':   'first',  # 每组第一个价格作为开盘价
        'high':  'max',    # 每组最高价
        'low':   'min',    # 每组最低价
        'close':  'last',   # 每组最后一个价格作为收盘价
        'volume': 'sum'    # 每组成交量总和
    }
    # 执行聚合操作
    ohlcv_df = df.groupby('group').agg(agg_dict)
    # 重置索引并清理列名（可选）
    ohlcv_df = ohlcv_df.reset_index(drop=True)
    
    return ohlcv_df


def process_data(data):
    day = reorganize_stock_data(data,"d")
    minute = reorganize_stock_data(data[-9000:],"m")[-120:]
    hour = reorganize_stock_data(data[-86400:],"h")[-120:]
    second = reorganize_stock_data(data[-2400:],"s")[-120:]

    day_last_10= day['close'].values[-10:].tolist()
    hour_last_10=  hour['close'].values[-10:].tolist()
    minute_last_10= minute['close'].values[-10:].tolist()
    second_last_10= second['close'].values[-10:].tolist()
    day_last_10 = {k:v for k,v in enumerate(day_last_10)}
    hour_last_10 = {k:v for k,v in enumerate(hour_last_10)}
    minute_last_10 = {k:v for k,v in enumerate(minute_last_10)}
    second_last_10 = {k:v for k,v in enumerate(second_last_10)}
    day = Analysis(day) 
    hour = Analysis(hour)
    minute = Analysis(minute)
    second = Analysis(second)

    day_index = execute_all_methods(Analysis,day)
    hour_index = execute_all_methods(Analysis,hour)
    minute_index = execute_all_methods(Analysis,minute)
    second_index = execute_all_methods(Analysis,second)
    del day,hour,minute,second
    return {
        "day_factor":day_index ,
        "hour_factor":hour_index,
        "minute_factor":minute_index,
        "second_factor":second_index,
        "daylast_10": day_last_10,
        "hourlast_10": hour_last_10,
        "minutelast_10": minute_last_10,
        "secondlast_10": second_last_10,
        }


def get_trend(df):
    datas = process_data(df)
    test_data_processor = DataProcessor(datas=datas,isTrain=0)
    X_test = test_data_processor.get_X(features)
        
    X_test = scaler.transform(X_test)
    y_pred = model.predict(X_test)
    return y_pred