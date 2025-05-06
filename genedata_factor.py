import pandas as pd
import json
import time
from multiprocessing import Pool, cpu_count
from analyse import *
with open("datas/train_index",'r',encoding='utf-8')as f:
    indexs = json.loads(f.read())

import inspect
# 获取类的所有方法名并执行
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
    special_name =['Aroon_2', 'BBANDS_3', 'MACDFIX_3', 
                  'MACD_3', 'STOCH', 'STOCHF', 'STOCHRSI', 'STOCH_2']
    res ={}
    for method_name in methods:
        method = getattr(instance, method_name)
        vals = method()
        if method_name in ignore_name:
            continue
        if method_name in special_name:
            if isinstance(vals,dict):
                for k,val in vals.item():
                    subname = k
                    res[subname] = val.item()
            else:
                 for i,val in enumerate(vals):
                    subname = method_name+f"_{i+1}"
                    res[subname] = val.item()
        else:
            res[method_name] = vals.item()
        
    return res






file_path = 'datas/BTC_USDT-1s.feather'

data = pd.read_feather(file_path)






# 一次性提取所有数据
all_data = [data.iloc[index[0]:index[2]] for index in indexs]




def reorganize_stock_data(df,tp="s",is_smooth=False):
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
    if is_smooth:
        window = 5  # 5日平滑
        cols_to_smooth = ['open', 'high', 'low', 'close']
        ohlcv_df[cols_to_smooth] = ohlcv_df[cols_to_smooth].rolling(window=window).mean()
    return ohlcv_df



start = time.time()
res=[]

def process_id(id,is_smooth=False):
    # with label
    data =all_data[id][:-300]

    day = reorganize_stock_data(data,"d",is_smooth)
    minute = reorganize_stock_data(data[-9000:],"m",is_smooth)[-120:]
    hour = reorganize_stock_data(data[-86400:],"h",is_smooth)[-120:]
    second = reorganize_stock_data(data[-7200:],"s",is_smooth)[-120:]

    last300s = all_data[id]['close'][-300:].values
    cur_v = all_data[id]['close'].values[-300]
    last300_rates = (last300s-cur_v)/cur_v
    upper,down = (last300_rates>0.0002).sum(),(last300_rates<-0.0002).sum()
    steady = len(last300s)-upper-down
    
    label = 1 if last300_rates [-1]>0 else -1

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
        "label": label,
        "up_num": upper.item(),
        "down_num": down.item(),
        "steady_num": steady.item()
        }
num_processes = cpu_count()-8  # 获取 CPU 核心数

with Pool(processes=num_processes) as pool:
    results = pool.map(process_id, range(len(all_data)//2,len(all_data)))
# results =[]
# for i in range(len(all_data)//2):
#     results.append(process_id(i))
cnt= 0
for item in results:
    if item['label']==1:
        cnt+=1
print(cnt,len(results))
print("start")
s = time.time()
with open('train_factor_r1.json','w')as f:
    f.write(json.dumps(results))
print("done")


print(time.time()-start)




  


