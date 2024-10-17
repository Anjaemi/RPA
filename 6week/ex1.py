import pandas as pd
import matplotlib.pyplot as pit
import matplotlib.font_manager as font_manager
import seaborn as sns

hat=pd.read_csv('ch4-1.csv') # hat 변수에 데이터셋 입력

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
pit.rc('font', family=font_name)

#히스토그램 그리기
pit.figure(figsize=(10, 17)) #그래프 크기 지정
pit.hist(hat.weight, bins = 7)
pit.title('B 부화장 병아리 무게 분포 현황', fontsize = 17)
pit.xlabel('병아리 무게(g)')
pit.ylabel('마릿수')

#sns.distplot(hat.weight)

pit.show()