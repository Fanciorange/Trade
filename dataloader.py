
import pandas as pd
import json,random


class DataProcessor():
    def __init__(self,filepaths=None,datas=None,isTrain=True):
        assert filepaths!=None or datas !=None
        self.filepaths = filepaths
        self.isTrain = isTrain
        self.init__(filepaths,datas)
        
    def init__(self,filepaths,datas):
        if datas is None:
            datas = []
            for filepath in filepaths:
                # 读取训练集
                with open(filepath, 'r') as f:
                    s = f.read()
                datas.extend(json.loads(s))
        datas = self.flatten_and_prefix_factors(datas)
        df = pd.DataFrame(datas)
        self.data = self.processNaN(df)
    def flatten_and_prefix_factors(self,datas):
        def rename_factor(data):
            res = {}
            for name in ['day_factor', 'hour_factor', 'minute_factor']:
                for key in data[name].keys():
                    new_key = name[:name.index("_")+1]+key
                    res[new_key] = data[name][key]
            if 'label' in data:
                res['label'] = data['label']
            return res
        finaldata = []
        for data in datas:
            finaldata.append(rename_factor(data))
        return finaldata
    def processNaN(self,df):
        df_filled = df.fillna(0)
        return df_filled
    def get_random_factornames(self,k=50,seed=None):
        valid_columes = self.data.loc[:, self.data.nunique() != 1].columns.to_list()
        valid_columes.remove("label")
        valid_columes.remove("rise_ratio")
        if seed:
            random.seed(seed)
        if k==-1:
            return valid_columes
        return random.sample(valid_columes,k)
    def get_X_y(self,factornames):
        X = self.data[factornames].values
        y = self.data['label'].values
        return X,y
    def get_X(self,factornames):
        X = self.data[factornames].values
        return X

dataprocessor = DataProcessor(["train_factor_r1.json"])
factorls = dataprocessor.get_random_factornames()
X,y = dataprocessor.get_X_y(factorls)


