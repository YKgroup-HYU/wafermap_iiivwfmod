import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from wafer_map import wm_app

df = pd.read_csv(r'../data/Info_LMZ_AL810962.csv')

data_length = len(df)

# Data filter
df[df['Lot']=='AL810962']
df[df['Wafer']=='D05']
df[df['TestSite']=='IIIV_LMZC_IIIV230_JT100']
df[df['Date Flag']==0]
df[df['ErrorFlag']==0]

z = 'VpiL@0V [V.cm]' # z for plot
df_ft =df[['Row','Column', z]] # df_ft = filtered_data로 필터링 후 데이터를 담았습니다.
data = [] # data = wm_app을 위한 리스트

for i in range(0, data_length):
    in_data = []
    # Row = df_ft.loc[i].Row
    # Column = df_ft.loc[i].Column
    # OP = df_ft.loc[i].VpiL0V
    Row = df_ft['Row'].loc[i]
    Column = df_ft['Column'].loc[i]
    OP = df_ft[z].loc[i] # 이 문법을 사용하면 공백있어도 가능함.
    in_data.append(Column)
    in_data.append(Row)
    in_data.append(OP)
    data.append(in_data)
# wm_app의 data 형식을 맞추기 위해 이중 list 구조로 담았습니다.
# df_ft의 list 변환도 안먹히고, len이나 range가 먹히지 않아 csv 파일의 길이로 선언했습니다. <- 이게 무슨말이지?

wm_app.WaferMapApp(data,(25870,13820),(0,0),300000)
