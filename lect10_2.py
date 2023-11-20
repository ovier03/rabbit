# Dataframe (개발환경대로 설치하기)
"""
import pandas as pd

df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])

print(df)
print("\n-------------------\n")
print(df[1])
print("\n-------------------\n")
print(df[1],[1])
print("\n-------------------\n")
print(df[2],[1])
"""

# Dataframe dic
"""
import pandas as pd

data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)

print(fr)
print("\n-------------------\n")

print(fr["x"])
print("\n-------------------\n")

print(fr.x)
print("\n-------------------\n")

print(fr.iloc[2])
print("\n-------------------\n")

print(fr.loc["y축"])
print("\n-------------------\n")

# 컬럼(열)추가

frs = pd.DataFrame(fr,columns=["x", "y", "z", "t"])
print(frs)
frs["t"] = [60, 120, 180]
print(frs)

# 행 추가

print("\n-------------------\n")
frs.loc["t축"] = [100, 200, 300, 400]
print(frs)
 

# 행 수정

print("\n-------------------\n")
frs.loc["t축"] = [500, 600, 700, 800]
print(frs)

# 행/열 삭제

print("\n-------------------\n")

#행 삭제
frs.drop("x", axis=1, inplace=True)
print(frs)

# 열 삭제
frs.drop("x축", inplace=True)
print(frs)
"""

# 컬럼추가
"""
import pandas as pd

dt = [[1,10,100],[2,20,200],[3,30,300]]
# col = ["x","y","z"]
# idx = ["x축","y축","z축"]

col = ["col1", "col2", "col3"]
idx = ["삼성", "현대", "LG"]


df = pd.DataFrame(data=dt,index=idx,columns=col)

print(df)
print("\n-------------------\n")

# 컬럼 / 행 출력

# print(df["x"])
print(df["col1"])
print("\n-------------------\n")

# 인덱스 / 로우 출력

# print(df.loc['x축'])
print(df.loc["삼성"])
print("\n-------------------\n")

# 연산

print(df + 1)
print("\n-------------------\n")
print(df.div(100))
print("\n-------------------\n")
print(df / 100)
print("\n-------------------\n")
print(df.mul(100))
print("\n-------------------\n")

# 두 데이터프레임간 연산

# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["삼성","현대","LG"],columns=["col2"])
print(df2)
print("\n-------------------\n")
print(df.div(df2))
print("\n-------------------\n")
print(df.mul(df2))
print("\n-------------------\n")

# 빈값을 채워 연산
 
print(df.div(df2, fill_value=1))
"""

# 멀티인덱스
""" 
import pandas as pd

idx = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
dt = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

ind = pd.MultiIndex.from_tuples(idx)
df = pd.DataFrame(dt, columns=['col1', 'col2', 'col3'], index = ind)

print(df)
print("\n-------------------\n")
print(df.loc["row1"])
print("\n-------------------\n")
print(df.loc[("row2", "val3")])
print("\n-------------------\n")

print(df.loc[("row3", "val3")])
print("\n-------------------\n")
print(df.loc[("row3", "val3"), "col1"])
print("\n-------------------\n")
"""

# 랜덤 데이터 생성
"""
import numpy as np
import pandas as pd

dt = np.random.randint(10, size=(5, 5))
df = pd.DataFrame(dt)

print(df)
print("\n-------------------\n")

print(df[2])
print("\n-------------------\n")

print(df.loc[2])
print("\n-------------------\n")

print(df.loc[3][1])
print("\n-------------------\n")

print(df.head(2))
print("\n-------------------\n")

print(df.tail(3))
print("\n-------------------\n")

print(df.sample[3])
print("\n-------------------\n")
"""

# 출력
"""
from faker import Faker as fk
import os
import pandas as pd

temp = fk("ko-KR")
print(temp.name())
folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
        f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")
"""

# 파일열기
"""
import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"
 

df = pd.read_csv(target)

# print(df)
print(df.values[0])

# 부분읽기

print("\n-------------------\n")
print(df.head())

print("\n-------------------\n")
print(df.head(3))

print("\n-------------------\n")
print(df.tail())

print("\n-------------------\n")
print(df.tail(3))

print("\n-------------------\n")
print(df.sample())
print(df.sample(4))

# 인텍스 설정 확인

print("\n-------------------\n")
print(df.index)

# 컬럼별 타입확인

print("\n-------------------\n")
print(df.dtypes)
print(type(df))

# 출력

print(df.values)
print(df.values[3])

# 엘레멘트 출력

for el in df.values[0] :
    print(el)

# 데이터프레임 정보확인

print(df.info())

# null 값 확인

print(df.isnull())
print(df.isnull().sum())

# 컬럼 / 행 데이터 확인

print(df.name)
print(df.address)
print(df.postcode)
print(df.company)
print(df.job)
print(df.phone)
print(df.email) 
print(df.id)
print(df.color)

print(df["name"])
print(df["address"])
print(df["postcode"])
print(df["company"])
print(df["job"])
 

# 여러 칼럼 확인

print(df[["name", "id"]])
print(df[["name", "address", "postcode"]])

# 칼럼 데이터 상세

print(df.postcode.describe())
print(df.color.describe())

# 칼럼 데이터 연산

print(df.color.count())

# 각 데이터별 카운팅

print(df.color.value_counts())

# 데이터간 연산

temp = df.postcode.sum() /석석df.name.count()
print(temp)

# 비교 연산

print(df.name == "이민석")
temp = df[df.color == "Maroon"].head(1)
temp = df[df.color == "Mardon"].head(2)
print(temp)
"""


