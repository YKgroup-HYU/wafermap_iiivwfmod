import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from wafer_map import wm_app

# csv를 panda로 가져오는데, 슬라이싱을 공백 단위로 해버려서
# 데이터 값이 온전히 살지 않았습니다. 그래서 VpiL@-0V [V.cm]를 VpiL0V로 바꿨습니다..

ld = pd.read_csv('./data/Info_LMZ_AL810962.csv')
data_length = len(ld)
# ld = load_data, csv 파일 로드
# 결과 담을 리스트의 크기를 위해 data_length 를 뽑았습니다.

ld[ld['Lot']=='AL810962']
ld[ld['Wafer']=='D08']
ld[ld['TestSite']=='IIIV_LMZC_IIIV230_JT100']
fd =ld[['Row','Column','VpiL0V']]
# pandas 형식상 and가 먹히지 않아서 순차적으로 filter했습니다.
# fd = filtered_data로 필터링 후 데이터를 담았습니다.

data = []
# data = wm_app을 위한 리스트

for i in range(0,data_length):
    in_data = []
    Row = fd.loc[i].Row
    Column = fd.loc[i].Column
    OP = fd.loc[i].VpiL0V
    in_data.append(Row)
    in_data.append(Column)
    in_data.append(OP)
    data.append(in_data)
# wm_app의 data 형식을 맞추기 위해 이중 list 구조로 담았습니다.
# fd의 list 변환도 안먹히고, len이나 range가 먹히지 않아 csv 파일의 길이로 선언했습니다.

wm_app.WaferMapApp(data,(25870,13820),(0,0),600000)
# dia = 300000으로 하니 사이즈를 벗어나서 반지름인듯 해 x2로 넣었습니다