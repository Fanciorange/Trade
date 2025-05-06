import torch.nn as nn
# 定义MLP模型
class MLP(nn.Module):
    def __init__(self, input_dim,hidden_dim):
        super().__init__()
        # 第一层: 输入维度 -> 128
        self.layer1 = nn.Linear(input_dim,hidden_dim)
        # 第二层: 128 -> 64
        self.layer2 = nn.Linear(hidden_dim,input_dim)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.5)  # 在此处应用dropout，p为丢弃概率
        self.fc = nn.Linear(input_dim,input_dim)
    def forward(self, x):
        x1 = self.relu(self.layer1(x))
        x2= self.relu(self.layer2(x1))

        return self.fc(self.dropout(x2))


class Model(nn.Module):
    def __init__(self, input_dim,hidden_dim,layer_num=5):
        super().__init__()
        self.mlp = nn.ModuleList(
                    [MLP(input_dim,hidden_dim) for _ in range(layer_num)]
                )
        self.relu = nn.ReLU()
        self.fc = nn.Linear(input_dim,1)
        self.sigmoid = nn.Sigmoid()
    def forward(self,x):
        for mlp_layer in self.mlp:
            x = mlp_layer(x)
        return self.sigmoid(self.relu(self.fc(x)))
        