import pandas as pd

data = {
    '과목번호' : ['C1','C2','C3','C4','C5','C6'],
    '과목명' : ['인공지능개론','웃음치료','경영학','3D디자인','스포츠경영','예술의 세계'],
    '시간수' : [3,2,3,4,2,1]
}
df= pd.DataFrame(data)
print(df,end='\n\n')

print("1****************************")
print(df.iloc[2],end='\n\n')
print("2****************************")
print(df.iloc[0:5],end='\n\n')
print("3****************************")
print(df.iloc[[0,3,5]],end='\n\n')
print("4****************************")
print(df.iloc[:,3],end='\n\n')
print("5****************************")
print(df.iloc[:, 0:3],end='\n\n')
print("6****************************")
print(df.iloc[:,[1,3]],end='\n\n')
print("7****************************")
print(df.iloc[0:3, 1:3],end='\n\n')
print("8****************************")
print(df.iloc[[1,2,5],[1,3]],end='\n\n')