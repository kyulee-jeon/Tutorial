# 모듈 설치
import os
import pandas as pd
import numpy as np

# 파일 경로 확인
os.getcwd()

# 불러오기
df = pd.read_excel('filename')
df = pd.read_csv('filename')

# 저장하기
df.to_csv('savename', index=False)


* CHECK *
# Column, null count, dtype 확인 (object 주의)
df.info() 

# 결측값 제거
df_nonnull = df.dropna(axis=0) 

# 고유값 개수 세기
df['colname'].nunique()


* Column *
# 특정 열 추출
df = df[['col name']]

# 특정 열 삭제
df = df.drop(['colname'], axis=1)
df.pop('colname')

# 데이터 타입 변경
df.astype('str')
df['colname'] = df['colname'].astype('int') 
import datetime as datetime
df['colname'] = pd.to_datetime(df['col name']) 


* Row *
# 조건에 맞는 행 추출
condition = df['colname'] == 'value'
1) df[condition] 
2) df.loc[condition]

# list에 있는 행만 추출
df.loc[list]


* function *
# groupby (함수, 저장방법)
df_grouped = df.groupby('criteria column').min().reset_index()

# merge
df_merged = pd.merge(df1, df2, how='left', on='common column')


* Transform *
# column (series) to numpy array
np.array(df['colname'])

# numpy array to list
.tolist()

# dataframe to numpy
.to_numpy()
