import matplotlib. pyplot as pit
import pandas as pd

df= pd.read_csv('2024_seoul_data.csv', encoding='utf-8')
df2 = df.fillna(method='ffill')
df2.info()

df2.rename(columns={'최저기온':'min_temp'}, inplace=True)
df2.rename(columns={'평균기온':'min_temp'}, inplace=True)
df2.rename(columns={'최고기온':'min_temp'}, inplace=True)
df2.head(3)

pit.rc('font', family='Malgun Gothic')
pit.rcParams['axes.inicode_mainus'] = False

pit.title('서울시 2024년도 여름 기온 변화')
pit.plot(range(1,len(df2)+1), df2['min_temp'], label='최고기온', c='r')
pit.plot(range(1,len(df2)+1), df2['avg_temp'], label='평균기온', c='y')
pit.plot(range(1,len(df2)+1), df2['max_temp'], label='최저기온', c='b')
pit.xlabel('일')
pit.ylabel('기온')
pit.legend()
pit.show()