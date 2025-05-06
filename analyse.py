


import talib as ta
import pandas as pd
import numpy as np

class Analysis:
    def __init__(self,df):
        self.high = df['high'].values
        self.low = df['low'].values
        self.close = df['close'].values
        self.volume =  df['volume'].values
        self.open = df['open'].values

    def ATR(self ,timeperiod=14):
        high, low, close = self.high,self.low,self.close
        return ta.ATR(high, low, close, timeperiod=14)[-1]
    def RSI(self ): 
        # 秒级rsi  日级rsi  分级别rsi 
        # 使用 ta 库计算 RSI
        # 参数 window 是 RSI 的周期，默认为 14
        rsi = ta.RSI(self.close, timeperiod=2)
        rsimean = rsi[-6:].mean()
        if rsimean <30:
            return 0
        elif rsimean>70:
            return 1
        else:
            return 2
    def STOCH_2(self ):
        high, low, close = self.high,self.low,self.close
        
        slowk, slowd = ta.STOCH(high, low, close, 
                                fastk_period=5, 
                                slowk_period=3, 
                                slowk_matype=0, 
                                slowd_period=3, 
                                slowd_matype=0)
                                
        return slowk[-1],slowd[-1]
    def MACD_3(self ):
        close = self.close
        macd, macdsignal, macdhist = ta.MACD(close, 
                                            fastperiod=12, 
                                            slowperiod=26, 
                                            signalperiod=9)
        return {"macd":macd[-1],"macdsignal":macdsignal[-1],
                "macdhist":macdhist[-1]}
    def BBANDS_3(self ):
            # 提取收盘价序列
        close = self.close

        # 使用TA-Lib计算布林带
        upper_band, middle_band, lower_band = ta.BBANDS(close,
                                                            timeperiod=5,  # 计算周期
                                                            nbdevup=2,     # 上轨标准差倍数
                                                            nbdevdn=2,     # 下轨标准差倍数
                                                            matype=0) 
        return {"upper_band":upper_band[-1],
                "middle_band:":middle_band[-1],"lower_band":lower_band[-1]}
    def EMA(self ):
        # 提取收盘价序列
        close = self.close

        # 使用TA-Lib计算EMA
        ema = ta.EMA(close, timeperiod=5)
        return ema[-1]
    def ADXR(self ):
        high = self.high
        low = self.low
        close = self.close
        real = ta.ADXR(high, low,close, timeperiod=14)
        return real[-1]
    def AD(self ):
        high = self.high
        low = self.low
        close = self.close
        volume =  self.volume
        ad_line = ta.AD(high, low, close, volume)
        return ad_line[-1]
    def APO(self ):
        close = self.close
        real = ta.APO(close, fastperiod=12, slowperiod=26, matype=0)
        return real[-1]
    def Aroon_2(self ):
        high = self.high
        low = self.low
        aroondown, aroonup = ta.AROON(high, low, timeperiod=14)
        return {"aroondown":aroondown[-1],"aroonup":aroonup[-1]}
    def AROONOSC(self ):
        high = self.high
        low = self.low
        return ta.AROONOSC(high, low, timeperiod=14)[-1]
    def AVGPRICE(self ):
        open = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.AVGPRICE(open, high, low, close)[-1]
    def BOP(self ):
        open = self.open
        high = self.high
        low = self.low
        close = self.close
        real = ta.BOP(open, high, low, close)
        return real[-1]
    def CCI(self ):
        high = self.high
        low = self.low
        close = self.close
        return ta.CCI(high, low, close, timeperiod=14)[-1]
    def CMO(self ):
        close = self.close
        return ta.CMO(close)[-1]

    def DEMA(self ):
        close = self.close
        return ta.DEMA(close, timeperiod=10)[-1]
    def DX(self ):
        high = self.high
        low = self.low
        close = self.close
        real = ta.DX(high, low, close, timeperiod=14)
        return real[-1]
    def HT_DCPERIOD(self ):
        close = self.close
        return ta.HT_DCPERIOD(close)[-1]
    def HT_DCPHASE(self ):
        close = self.close
        return ta.HT_DCPHASE(close)[-1]
    def HT_PHASOR(self ):
        close = self.close
        return ta.HT_PHASOR(close)[-1]
    def HT_SINE(self ):
        close = self.close
        return ta.HT_SINE(close)[-1]
    def HT_TRENDLINE(self ):
        close = self.close
        return ta.HT_TRENDLINE(close)[-1]
    def HT_TRENDMODE(self ):
        close = self.close
        return ta.HT_TRENDMODE(close)[-1]
    def KAMA(self ):
        close = self.close
        return ta.KAMA(close)[-1]
    def LINEARREG(self ):
        close = self.close
        real = ta.LINEARREG(close, timeperiod=14)
        return real[-1]
    def LINEARREG_SLOPE(self ):
        close = self.close
        return ta.LINEARREG_SLOPE(close)[-1]
    def LINEARREG_INTERCEPT(self ):
        close = self.close
        return ta.LINEARREG_INTERCEPT(close)[-1]

    def MACDFIX_3(self ):
        close = self.close
        macd, macdsignal, macdhist =ta.MACDFIX(close, signalperiod=9)
        return (macd[-1],macdsignal[-1],macdhist[-1])

    def TRIX(self ):
        close = self.close
        return ta.TRIX(close)[-1]
    def TSF(self ):
        close = self.close
        return ta.TSF(close)[-1]
    def TYPPRICE(self ):
        high = self.high
        low = self.low
        close = self.close
        real = ta.TYPPRICE(high, low, close)
        return real[-1]
    def ULTOSC(self ):
        high = self.high
        low = self.low
        close = self.close
        return ta.ULTOSC(high, low, close, timeperiod1=7, 
                         timeperiod2=14, timeperiod3=28)[-1]
    
    def VAR(self ):
        close = self.close
        return ta.VAR(close,)[-1]
    def WCLPRICE(self ):
        high = self.high
        low = self.low
        close = self.close
        return ta.WCLPRICE(high, low, close)[-1]   
    def MAX(self ):
        close = self.close
        return ta.MAX(close)[-1] 
    def MIN(self ):
        close = self.close
        return ta.MIN(close)[-1] 
    def MAXINDEX(self ):
        close = self.close
        return ta.MAXINDEX(close)[-1] 
    def MEDPRICE(self ):
        close = self.close
        return ta.MAXINDEX(close)[-1]
    def MFI(self ):
        high = self.high
        low = self.low
        close = self.close
        volume =  self.volume
        return ta.MFI(high, low, close, volume, timeperiod=14)[-1]
    def MIDPOINT(self ):
        close = self.close
        return ta.MIDPOINT(close)[-1]
    def MIDPRICE(self ):
        high = self.high
        low = self.low
        return ta.MIDPRICE(high, low,)[-1]
    def MININDEX(self ):
        low = self.low
        return ta.MININDEX(low)
    def MINUS_DI(self ):
        high = self.high
        low = self.low
        close = self.close
        return ta.MINUS_DI(high, low, close, timeperiod=14)[-1]
    def MINUS_DM(self ):
        high = self.high
        low = self.low
        return ta.MINUS_DM(high, low)[-1]
    def MOM(self ):
        close = self.close
        return ta.MOM(close)[-1]
    def OBV(self ):
        """累积能量指标 (On-Balance Volume)"""
        close = self.close
        volume =  self.volume
        return ta.OBV(close, volume)[-1]

    def PLUS_DI(self , timeperiod=14):
        """正向方向指标 (Plus Directional Indicator)"""
        high = self.high
        low = self.low
        close = self.close
        return ta.PLUS_DI(high, low, close, timeperiod)[-1]

    def PLUS_DM(self , timeperiod=14):
        """正向方向运动 (Plus Directional Movement)"""
        high = self.high
        low = self.low
        return ta.PLUS_DM(high, low, timeperiod)[-1]

    def PPO(self , fastperiod=12, slowperiod=26, matype=0):
        """价格百分比振荡器 (Percentage Price Oscillator)"""
        close = self.close
        return ta.PPO(close, fastperiod, slowperiod, matype)[-1]

    def ROC(self , timeperiod=10):
        """变化率 (Rate of Change)"""
        close = self.close
        return ta.ROC(close, timeperiod)[-1]

    def ROCP(self , timeperiod=10):
        """变化率百分比 (Rate of Change Percentage)"""
        close = self.close
        return ta.ROCP(close, timeperiod)[-1]

    def ROCR(self , timeperiod=10):
        """变化率比率 (Rate of Change Ratio)"""
        close = self.close
        return ta.ROCR(close, timeperiod)[-1]

    def ROCR100(self , timeperiod=10):
        """变化率比率（100倍）(Rate of Change Ratio 100 Scale)"""
        close = self.close
        return ta.ROCR100(close, timeperiod)[-1]

    def RSI(self , timeperiod=14):
        """相对强弱指数 (Relative Strength Index)"""
        close = self.close
        return ta.RSI(close, timeperiod)[-1]

    def SAR(self , acceleration=0.02, maximum=0.2):
        """抛物线转向指标 (Parabolic SAR)"""
        high = self.high
        low = self.low
        return ta.SAR(high, low, acceleration, maximum)[-1]

    def SAREXT(self , startvalue=0, offsetonreverse=0, accelerationinitlong=0.02,
               accelerationlong=0.02, accelerationmaxlong=0.2, accelerationinitshort=0.02,
               accelerationshort=0.02, accelerationmaxshort=0.2):
        """扩展抛物线转向指标 (Parabolic SAR - Extended)"""
        high = self.high
        low = self.low
        return ta.SAREXT(high, low, startvalue, offsetonreverse,
                         accelerationinitlong, accelerationlong, accelerationmaxlong,
                         accelerationinitshort, accelerationshort, accelerationmaxshort)[-1]
    def STDDEV(self , timeperiod=5, nbdev=1):
        """标准差 (Standard Deviation)"""
        close = self.close
        return ta.STDDEV(close, timeperiod, nbdev)[-1]

    def STOCH(self ):
        """随机指标 (Stochastic)"""
        high = self.high
        low = self.low
        close = self.close
        slowk, slowd = ta.STOCH(high, low, close)
        return {'slowk': slowk[-1], 'slowd': slowd[-1]}

    def STOCHF(self , ):
        """快速随机指标 (Stochastic Fast)"""
        high = self.high
        low = self.low
        close = self.close
        fastk, fastd = ta.STOCHF(high, low, close)
        return {'fastk': fastk[-1], 'fastd': fastd[-1]}

    def STOCHRSI(self ):
        """随机相对强弱指数 (Stochastic Relative Strength Index)"""
        close = self.close
        fastk, fastd = ta.STOCHRSI(close)
        return {'fastk': fastk[-1], 'fastd': fastd[-1]}

    def SUM(self , timeperiod=30):
        """求和 (Summation)"""
        close = self.close
        return ta.SUM(close, timeperiod)[-1]

    def T3(self , timeperiod=5, vfactor=0.7):
        """三重指数移动平均 (Triple Exponential Moving Average (T3))"""
        close = self.close
        return ta.T3(close)[-1]

    def TEMA(self , timeperiod=30):
        """三重指数移动平均 (Triple Exponential Moving Average)"""
        close = self.close
        return ta.TEMA(close, timeperiod)[-1]

    def TRANGE(self ):
        """真实范围 (True Range)"""
        high = self.high
        low = self.low
        close = self.close
        return ta.TRANGE(high, low, close)[-1]

    def TRIMA(self , timeperiod=30):
        """三角形移动平均 (Triangular Moving Average)"""
        close = self.close
        return ta.TRIMA(close, timeperiod)[-1]

    def TRIX(self , timeperiod=30):
        """TRIX（1日ROC的三次平滑EMA）(1-day Rate-Of-Change (ROC) of a Triple Smooth EMA)"""
        close = self.close
        return ta.TRIX(close, timeperiod)[-1]

    def TSF(self , timeperiod=14):
        """时间序列预测 (Time Series Forecast)"""
        close = self.close
        return ta.TSF(close, timeperiod)[-1]

    def TYPPRICE(self ):
        """典型价格 (Typical Price)"""
        high = self.high
        low = self.low
        close = self.close
        return ta.TYPPRICE(high, low, close)[-1]

    def ULTOSC(self , timeperiod1=7, timeperiod2=14, timeperiod3=28):
        """终极振荡器 (Ultimate Oscillator)"""
        high = self.high
        low = self.low
        close = self.close
        return ta.ULTOSC(high, low, close, timeperiod1, timeperiod2, timeperiod3)[-1]

    def VAR(self , timeperiod=5, nbdev=1):
        """方差 (Variance)"""
        close = self.close
        return ta.VAR(close, timeperiod, nbdev)[-1]

    def WCLPRICE(self ):
        """加权收盘价 (Weighted Close Price)"""
        high = self.high
        low = self.low
        close = self.close
        return ta.WCLPRICE(high, low, close)[-1]

    def WILLR(self , timeperiod=14):
        """威廉%R (Williams' %R)"""
        high = self.high
        low = self.low
        close = self.close
        return ta.WILLR(high, low, close, timeperiod)[-1]

    def WMA(self , timeperiod=30):
        """加权移动平均 (Weighted Moving Average)"""
        close = self.close
        return ta.WMA(close, timeperiod)[-1]
    def CDL2CROWS(self ):
        """两只乌鸦 (Two Crows)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDL2CROWS(open_price, high, low, close)[-1]

    def CDL3BLACKCROWS(self ):
        """三只黑乌鸦 (Three Black Crows)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDL3BLACKCROWS(open_price, high, low, close)[-1]

    def CDL3INSIDE(self ):
        """三内部上涨/下跌 (Three Inside Up/Down)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDL3INSIDE(open_price, high, low, close)[-1]

    def CDL3LINESTRIKE(self ):
        """三线 Strike (Three Line Strike)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDL3LINESTRIKE(open_price, high, low, close)[-1]

    def CDL3STARSINSOUTH(self ):
        """南方三星 (Three Stars In The South)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDL3STARSINSOUTH(open_price, high, low, close)[-1]

    def CDL3WHITESOLDIERS(self ):
        """三个白士兵 (Three Advancing White Soldiers)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDL3WHITESOLDIERS(open_price, high, low, close)[-1]
    def CDLABANDONEDBABY(self , penetration=0.3):
        """被弃婴形态 (Abandoned Baby)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLABANDONEDBABY(open_price, high, low, close, penetration)[-1]

    def CDLADVANCEBLOCK(self ):
        """大敌当前形态 (Advance Block)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLADVANCEBLOCK(open_price, high, low, close)[-1]

    def CDLBELTHOLD(self ):
        """捉腰带线 (Belt-hold)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLBELTHOLD(open_price, high, low, close)[-1]

    def CDLBREAKAWAY(self ):
        """脱离形态 (Breakaway)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLBREAKAWAY(open_price, high, low, close)[-1]

    def CDLCLOSINGMARUBOZU(self ):
        """收盘光头光脚 (Closing Marubozu)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLCLOSINGMARUBOZU(open_price, high, low, close)[-1]

    def CDLCONCEALBABYSWALL(self ):
        """藏婴吞没形态 (Concealing Baby Swallow)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLCONCEALBABYSWALL(open_price, high, low, close)[-1]

    def CDLCOUNTERATTACK(self ):
        """反击线形态 (Counterattack)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLCOUNTERATTACK(open_price, high, low, close)[-1]

    def CDLDARKCLOUDCOVER(self , penetration=0.5):
        """乌云盖顶形态 (Dark Cloud Cover)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLDARKCLOUDCOVER(open_price, high, low, close, penetration)[-1]
    def CDLDOJI(self ):
        """十字星 (Doji)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLDOJI(open_price, high, low, close)[-1]

    def CDLDOJISTAR(self ):
        """十字星 (Doji Star)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLDOJISTAR(open_price, high, low, close)[-1]

    def CDLDRAGONFLYDOJI(self ):
        """蜻蜓十字星 (Dragonfly Doji)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLDRAGONFLYDOJI(open_price, high, low, close)[-1]

    def CDLENGULFING(self ):
        """吞没形态 (Engulfing Pattern)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLENGULFING(open_price, high, low, close)[-1]

    def CDLEVENINGDOJISTAR(self , penetration=0.3):
        """黄昏十字星 (Evening Doji Star)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLEVENINGDOJISTAR(open_price, high, low, close, penetration)[-1]

    def CDLEVENINGSTAR(self , penetration=0.3):
        """黄昏之星 (Evening Star)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLEVENINGSTAR(open_price, high, low, close, penetration)[-1]

    def CDLGAPSIDESIDEWHITE(self ):
        """上下跳空并列阳线 (Up/Down-gap side-by-side white lines)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLGAPSIDESIDEWHITE(open_price, high, low, close)[-1]

    def CDLGRAVESTONEDOJI(self ):
        """墓碑十字星 (Gravestone Doji)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLGRAVESTONEDOJI(open_price, high, low, close)[-1]

    def CDLHAMMER(self ):
        """锤子线 (Hammer)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLHAMMER(open_price, high, low, close)[-1]

    def CDLHANGINGMAN(self ):
        """吊颈线 (Hanging Man)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLHANGINGMAN(open_price, high, low, close)[-1]

    def CDLHARAMI(self ):
        """孕线形态 (Harami Pattern)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLHARAMI(open_price, high, low, close)[-1]

    def CDLHARAMICROSS(self ):
        """十字孕线形态 (Harami Cross Pattern)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLHARAMICROSS(open_price, high, low, close)[-1]

    def CDLHIGHWAVE(self ):
        """高浪线 (High-Wave Candle)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLHIGHWAVE(open_price, high, low, close)[-1]

    def CDLHIKKAKE(self ):
        """陷阱形态 (Hikkake Pattern)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLHIKKAKE(open_price, high, low, close)[-1]

    def CDLHIKKAKEMOD(self ):
        """改良陷阱形态 (Modified Hikkake Pattern)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLHIKKAKEMOD(open_price, high, low, close)[-1]

    def CDLHOMINGPIGEON(self ):
        """归巢线 (Homing Pigeon)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLHOMINGPIGEON(open_price, high, low, close)[-1]

    def CDLIDENTICAL3CROWS(self ):
        """三胞胎乌鸦 (Identical Three Crows)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLIDENTICAL3CROWS(open_price, high, low, close)[-1]

    def CDLINNECK(self ):
        """颈内线 (In-Neck Pattern)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLINNECK(open_price, high, low, close)[-1]

    def CDLINVERTEDHAMMER(self ):
        """倒锤子线 (Inverted Hammer)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLINVERTEDHAMMER(open_price, high, low, close)[-1]

    def CDLKICKING(self ):
        """反冲形态 (Kicking)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLKICKING(open_price, high, low, close)[-1]

    def CDLKICKINGBYLENGTH(self ):
        """按长度判断的反冲形态 (Kicking - bull/bear determined by the longer marubozu)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLKICKINGBYLENGTH(open_price, high, low, close)[-1]
    def CDLLADDERBOTTOM(self ):
        """梯底 (Ladder Bottom)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLLADDERBOTTOM(open_price, high, low, close)[-1]

    def CDLLONGLEGGEDDOJI(self ):
        """长脚十字 (Long Legged Doji)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLLONGLEGGEDDOJI(open_price, high, low, close)[-1]

    def CDLLONGLINE(self ):
        """长线 (Long Line Candle)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLLONGLINE(open_price, high, low, close)[-1]

    def CDLMARUBOZU(self ):
        """光头光脚/秃蜡烛 (Marubozu)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLMARUBOZU(open_price, high, low, close)[-1]

    def CDLMATCHINGLOW(self ):
        """匹配低点 (Matching Low)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLMATCHINGLOW(open_price, high, low, close)[-1]

    def CDLMATHOLD(self , penetration=0.5):
        """铺垫 (Mat Hold)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLMATHOLD(open_price, high, low, close, penetration)[-1]

    def CDLMORNINGDOJISTAR(self , penetration=0.3):
        """早晨十字星 (Morning Doji Star)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLMORNINGDOJISTAR(open_price, high, low, close, penetration)[-1]

    def CDLMORNINGSTAR(self , penetration=0.3):
        """早晨之星 (Morning Star)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLMORNINGSTAR(open_price, high, low, close, penetration)[-1]

    def CDLONNECK(self ):
        """颈上线 (On-Neck Pattern)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLONNECK(open_price, high, low, close)[-1]

    def CDLPIERCING(self ):
        """刺透形态 (Piercing Pattern)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLPIERCING(open_price, high, low, close)[-1]

    def CDLRICKSHAWMAN(self ):
        """黄包车夫 (Rickshaw Man)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLRICKSHAWMAN(open_price, high, low, close)[-1]

    def CDLRISEFALL3METHODS(self ):
        """上升/下降三法 (Rising/Falling Three Methods)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLRISEFALL3METHODS(open_price, high, low, close)[-1]

    def CDLSEPARATINGLINES(self ):
        """分离线 (Separating Lines)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLSEPARATINGLINES(open_price, high, low, close)[-1]

    def CDLSHOOTINGSTAR(self ):
        """射击之星 (Shooting Star)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLSHOOTINGSTAR(open_price, high, low, close)[-1]

    def CDLSHORTLINE(self ):
        """短线 (Short Line Candle)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLSHORTLINE(open_price, high, low, close)[-1]

    def CDLSPINNINGTOP(self ):
        """纺锤 (Spinning Top)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLSPINNINGTOP(open_price, high, low, close)[-1]

    def CDLSTALLEDPATTERN(self ):
        """停顿形态 (Stalled Pattern)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLSTALLEDPATTERN(open_price, high, low, close)[-1]

    def CDLSTICKSANDWICH(self ):
        """棍棒三明治 (Stick Sandwich)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLSTICKSANDWICH(open_price, high, low, close)[-1]

    def CDLTAKURI(self ):
        """探水竿 (Takuri, Dragonfly Doji with very long lower shadow)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLTAKURI(open_price, high, low, close)[-1]

    def CDLTASUKIGAP(self ):
        """ Tasuki Gap """
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLTASUKIGAP(open_price, high, low, close)[-1]

    def CDLTHRUSTING(self ):
        """插入形态 (Thrusting Pattern)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLTHRUSTING(open_price, high, low, close)[-1]

    def CDLTRISTAR(self ):
        """三星形态 (Tristar Pattern)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLTRISTAR(open_price, high, low, close)[-1]

    def CDLUNIQUE3RIVER(self ):
        """奇特三河床 (Unique 3 River)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLUNIQUE3RIVER(open_price, high, low, close)[-1]

    def CDLUPSIDEGAP2CROWS(self ):
        """向上跳空两只乌鸦 (Upside Gap Two Crows)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLUPSIDEGAP2CROWS(open_price, high, low, close)[-1]

    def CDLXSIDEGAP3METHODS(self ):
        """上升/下降跳空三法 (Upside/Downside Gap Three Methods)"""
        open_price = self.open
        high = self.high
        low = self.low
        close = self.close
        return ta.CDLXSIDEGAP3METHODS(open_price, high, low, close)[-1]


import matplotlib.pyplot as plt
def plot(data):
    # 创建 x 轴数据（索引）
    x = np.arange(len(data))
    plt.plot(x, data, marker='o', linestyle='-', color='b')
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.legend()
    # 显示图形
    plt.show()