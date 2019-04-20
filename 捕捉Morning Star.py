# -*- coding: utf-8 -*-
"""
@author: Yaxin LI
"""

##############################################
#捕捉morning star
##############################################


#设置路径
import os
os.chdir(r'C:\Users\lenovo\Desktop\Python\attachments')

#加载工具包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter,DayLocator, date2num
import datetime
from mpl_finance import candlestick_ohlc

#加载数据
data2012=pd.read_csv('ssec2012.csv')
data2012.index=data2012.iloc[:,1]
data2012.index=pd.to_datetime(data2012.index,format='%Y-%m-%d')
data2012=data2012.iloc[:,2:]
data2012.head()


#1. 寻找满足要求的三个连续烛图的位置
Close=data2012.Close
Open=data2012.Open

Diff=Close-Open
lag1_Diff=Diff.shift(1)
lag2_Diff=Diff.shift(2)

DIFF=pd.DataFrame({'Diff':Diff,'lag1_Diff':lag1_Diff,'lag2_Diff':lag2_Diff})
DIFF.head()
DIFF["signal1"]=np.where((DIFF['lag2_Diff']<-11)&(abs(DIFF['lag1_Diff'])<2)&\
    (DIFF['Diff']>6)&(abs(DIFF['Diff'])>abs(DIFF['lag2_Diff']*0.5)),1,0)
#第一天下跌大于11，第二天变动小于2，今天涨的大于6，而且第三天的蜡烛长于第一天的一半
DIFF[DIFF["signal1"]==1]


#2. 寻找十字星的位置
lag1_Open=Open.shift(1)
lag1_Close=Close.shift(1)
lag2_Close=Close.shift(2)
Doji=pd.DataFrame({'Open':Open,'lag1_Open':lag1_Open,'lag1_Close':lag1_Close,'lag2_Close':lag2_Close})
Doji.head()
Doji["signal1"]=np.where((Doji['lag1_Open']<Doji['Open'])&\
    (Doji['lag1_Open']<Doji['lag2_Close'])&\
    (Doji['lag1_Close']<Doji['Open'])&\
    (Doji['lag1_Close']<Doji['lag2_Close']),1,0)
#第二天开盘小于第一天开盘，第二天开盘小于第三天开盘，第二天收盘小于第三天开盘，第二天
#收盘小于第一天收盘（完全在下方）
Doji[Doji["signal1"]==1]


#3. 捕捉下跌趋势：连续两天下跌
ret=Close/Close.shift(1)-1
lag1_ret=ret.shift(1)
lag2_ret=ret.shift(2)
Trend=pd.DataFrame({'ret':ret,'lag1_ret':lag1_ret,'lag2_ret':lag2_ret})
Trend.head()
Trend["signal1"]=np.where((Trend['lag1_ret']<0)&(Trend['lag2_ret']<0),1,0)
#第二天开盘小于第一天开盘，第二天开盘小于第三天开盘，第二天收盘小于第三天开盘，第二天
#收盘小于第一天收盘（完全在下方）
Trend[Trend["signal1"]==1]


#4. 找到morning star对应的日期
Mor_Star=data2012[(DIFF["signal1"]==1)&(Doji["signal1"]==1)&(Trend["signal1"]==1)]


#5. 展示morning star的K线图
def candlestick(data,Start_Date,End_Date):
    Morning_Star=[]
    Morning_Star=data[Start_Date:End_Date]

    Date=[date2num(date) for date in Morning_Star.index]
    Morning_Star.loc[:,'Date']=Date
    M_new=Morning_Star.reindex(columns=['Date','Open','High','Low','Close','Volume'])

    graphlist=list()
    for i in range(len(M_new)):
        graphlist.append(M_new.iloc[i,:])

    ax= plt.subplot()
    weekFormatter = DateFormatter('%y %b %d')#日期格式
    ax.xaxis.set_major_locator(DayLocator())#主要刻度：每周一的日期
    ax.xaxis.set_major_formatter(weekFormatter)#设置日期格式
    plt.rcParams['font.sans-serif'] = ['SimHei']#字体
    plt.rcParams['axes.unicode_minus'] = False
    ax.set_title("Morning Star 日 K 线图")
    candlestick_ohlc(ax,graphlist, width=0.7,colorup='r', colordown='g')
    plt.setp(plt.gca().get_xticklabels(),rotation=50, horizontalalignment='center')
#setp对一个列表或者单个对象进行设置，这里设置x轴的标签
    return(plt.show())

Start_Date1=(Mor_Star.index[0]+datetime.timedelta(days=-2)).strftime("%Y-%m-%d %H:%M:%S")
End_Date1=Mor_Star.index[0]
candlestick(data2012,Start_Date1,End_Date1)

Start_Date2=(Mor_Star.index[0]+datetime.timedelta(days=-9)).strftime("%Y-%m-%d %H:%M:%S")
End_Date2=(Mor_Star.index[0]+datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
candlestick(data2012,Start_Date2,End_Date2)


