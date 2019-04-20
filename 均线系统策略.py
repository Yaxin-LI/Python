# -*- coding: utf-8 -*-
"""
@author: Yaxin LI
"""

##############################################
#均线系统交易策略
##############################################

#设置路径
import os
os.chdir(r'C:\Users\lenovo\Desktop\Python\attachments')

#加载工具包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

#加载数据
data=pd.read_csv('ChinaBank.csv')
data.index=data.iloc[:,1]
data.index=pd.to_datetime(data.index,format='%Y-%m-%d')
data=data.iloc[:,2:]
data.head()


#1. 简单移动平均线：价格线上穿十日均线：买入；下穿卖出
data['sma10']=data['Close'].rolling(10).mean()
data['lag1_sma10']=data['sma10'].shift(1)
data['lag1_Close']=data['Close'].shift(1)

cond1=(data['lag1_Close']<data['lag1_sma10'])&(data['Close']>data['sma10'])
cond2=(data['lag1_Close']>data['lag1_sma10'])&(data['Close']<data['sma10'])
Signal=pd.DataFrame((1*cond1-1*cond2),index=data.index,columns=['sma10'])

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(data['Close'],label="Close",color='k')
plt.plot(data['sma10'],label='sma10',color='b',linestyle=':')
plt.title("收盘价与10日均线图")
plt.legend()

#2. 双均线交叉:短均线上穿长均线：买入；下穿卖出
data['sma5']=data['Close'].rolling(5).mean()
data['lag1_sma5']=data['sma5'].shift(1)
data['sma30']=data['Close'].rolling(30).mean()
data['lag1_sma30']=data['sma30'].shift(1)

cond3=(data['lag1_sma5']<data['lag1_sma30'])&(data['sma5']>data['sma30'])
cond4=(data['lag1_sma5']>data['lag1_sma30'])&(data['sma5']<data['sma30'])
Signal['sma5_sma30']=1*cond3-1*cond4

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(data['sma5'],label='sma5',color='r',linestyle='dashed')
plt.plot(data['sma30'],label='sma30',color='G',linestyle='-.')
plt.title("5日及10日移动均线图")
plt.legend()
plt.show()


#3. 异同移动平均线:DIF上穿DEA：买入；下穿卖出
data['DIF']=data['Close'].ewm(span=12).mean()-data['Close'].ewm(span=26).mean()
data['DEA']=data['DIF'].ewm(span=9).mean()
data['MACD']=data['DIF']-data['DEA']

data['lag1_DIF']=data['DIF'].shift(1)
data['lag1_DEA']=data['DEA'].shift(1)

cond5=(data['lag1_DIF']<data['lag1_DEA'])&(data['DIF']>data['DEA'])&(data['DEA']>0.0)
cond6=(data['lag1_DIF']>data['lag1_DEA'])&(data['DIF']<data['DEA'])&(data['DEA']<0.0)

Signal['MACD']=1*cond5-1*cond6

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(data['DIF'],label="DIF",color='k')
plt.plot(data['DEA'],label='DEA',color='r',linestyle='dashed')
plt.title("DIF与DEA线")
plt.legend()


#4. 整合所有信号
Signal['all_sig']=Signal['sma10']+Signal['sma5_sma30']+Signal['MACD']
Signal['all_sig']=np.where(Signal['all_sig']>1,1,np.where(Signal['all_sig']<-1,-1,0))

Signal['trade_sig']=Signal['all_sig'].shift(1)
Signal.head()


#5. 模拟账户交易
data['ass_ret']=data['Close']/data['Close'].shift(1)-1
Account=pd.DataFrame(data['ass_ret'][2:],index=data.index[2:],columns=['ass_ret'])
Account['Close']=data['Close'][2:]
Account['trade_sig']=Signal['trade_sig'][2:]
Account['Cash']=0
Account['Share']=0

#初始化账户状态
Account.ix[0,'Cash']=20000
Account.ix[1,'Share']=1000
Account.ix[1,'Cash']=Account.ix[0,'Cash']-Account.ix[1,'Share']*Account.ix[1,'Close']
Account.head()

#模拟交易
i=2
while i <len(Account['ass_ret']):
    Account.ix[i,'Cash']=Account.ix[i-1,'Cash']
    Account.ix[i,'Share']=Account.ix[i-1,'Share']
    
    if Account.ix[i,'trade_sig']==1:
        Account.ix[i,'Share']=Account.ix[i,'Share']+3000
        Account.ix[i,'Cash']=Account.ix[i,'Cash']-1000*Account.ix[i,'Close']
        
    if (Account.ix[i,'trade_sig']==-1)&(Account.ix[i,'Share']>0):
        Account.ix[i,'Share']=Account.ix[i,'Share']-1000
        Account.ix[i,'Cash']=Account.ix[i,'Cash']+1000*Account.ix[i,'Close']
    i+=1
    
Account['Asset']=Account['Cash']+Account['Share']*Account['Close']
     
    
plt.subplot(411)
plt.title("中国银行均线系统策略交易账户")
plt.plot(Account['Close'], color='b')
plt.ylabel("Price")

plt.subplot(412)
plt.plot(Account['Share'], color='b')
plt.ylabel("Share")
plt.ylim(0,max(Account['Share'])+1000)

plt.subplot(413)
plt.plot(Account['Asset'],label="asset",color='r')
plt.ylabel("Asset")
plt.ylim(min(Account['Asset'])-5000,max(Account['Asset'])+5000)

plt.subplot(414)
plt.plot(Account['Cash'], label="cash",color='g')
plt.ylabel("Cash")
plt.ylim(0,max(Account['Cash'])+5000)   

Trade_ret=math.sqrt(Account['Asset'][-1]/20000)-1 
    
print('年化资产收益率为:',Trade_ret)   

    
    
