

from model import Model
import torch,json
import sys,time,os
import numpy as np
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)
from dataloader import DataProcessor


# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)

# 获取当前文件的目录
current_dir = os.path.dirname(current_file_path)

input_dim = 50 
device = "cuda"
# 假设Model类定义和input_dim变量已经在前面定义好了
# 创建模型实例
model = Model(input_dim, 1024).to(device)

# 加载模型参数
model_path = f'{current_dir}/mlp_model_state_dict.pth'  # 这是保存模型参数的文件路径
model.load_state_dict(torch.load(model_path))

with open(f"{current_dir}/factors.json",'w')as f:
    s = f.read()
factornames = json.loads(s)
# 确保在评估模式下运行，如果有BatchNorm层或Dropout层
model.eval()


test_data_processor = DataProcessor(["test_factor.json"])
test_X,test_y = test_data_processor.get_X_y(factornames)



# 如果你想在测试集上进行预测，可以这样做：
with torch.no_grad():  # 禁用梯度计算，减少内存占用并加速计算
    test_features = torch.from_numpy(test_X.astype(np.float32)).to(device)
    predictions = model(test_features)
    # 处理predictions，例如转换为numpy数组或者进行其他后处理