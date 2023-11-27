# 변환
"""
import pandas as pd

target = './data/apt.csv'
df = pd.read_csv(target, encoding = "CP949")

df.to_csv("./data/conv_apt.csv", encoding="utf8")

print(df.head())

df = pd.read_csv("./data/conv_apt.csv", index_col=0)
print(df.head())

df = pd.read_csv("./data/conv_apt.csv", index_col=0)
print(df.head()) 
"""

"""
# 컬럼명 바꾸기
df = pd.read_csv("./data/conv_apt.csv", index_col=0)
df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df)
# print(df.dtypes)

df["분양가"] = df["분양가"].convert_dtypes()
# print(df.dtypes)
 
arr = df.to_numpy()
# print(arr)
# print(len(arr))

# print(df.describe())

print(df.transpose())
print(df.T.head())
"""

# 정렬
"""
import pandas as pd

df = pd.read_csv("C:\\Users\\Catholic\\python\\happy\\data\\apt.csv", index_col=0, encoding='cp949')
df = df.rename(columns={"분양가격(제곱미터)": "분양가"})
res = df.sort_values("지역명", ascending=False)
df.reset_index(inplace=True)
print(res.head())
res = df.sort_values(by="연도")[10:20]
print(res)
res = df[["지역명", "연도", "분양가"]][:7]
print(res)
print("\n----------------------\n")
res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
print(res)
print("\n----------------------\n")
res = df.loc[df["지역명"]=="강원"]
res = df.loc[df["연도"] > 2020]
print(res)
print("\n----------------------\n")
df0 = df.copy()
print(df0)
print("\n----------------------\n")

# 인덱스 지정 선택
res = df.iloc[2][1]
print(res)
print("\n----------------------\n")

# 인덱스 필터

res = df[df.index > 3560]
print(res)
print("\n----------------------\n")

# 필터

res = df[df.연도 == 2023]
print(res)
print("\n----------------------\n")

# 비트연산 필터

res = df[(df.연도 == 2023) & (df.지역명 =="서울") & (df.월 == 6)]
print(res)
print("\n----------------------\n")

# 컬럼 추가

res = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
print(res)
print("\n----------------------\n")

# NaN 행 제거

# df1 = df.reindex(index=df.index[:7], columns=0)
df1 = df.reindex(columns=list(df.columns) + ["extra"])
print(df1)

df1.loc[:4, "extra"] = False
print(df1)
df1.loc[:4, "extra"] = "0"
print("\n----------------------\n")
df2 = df1.copy()

res = df2.dropna(how="any")
res = df2.dropna(how="any", inplace=True)
print(df2)
print("\n----------------------\n")

res = df1.fillna(value="1234")
print(res)
print("\n----------------------\n")
res = df.dropna(how="any", inplace=True)
print(res)
print("\n----------------------\n")
print(df2)

res = pd.isna(df1)
print(res)

res = df["연도"].value_counts()
print(res)
print("\n----------------------\n")

res = df.groupby(["지역명", "연도", "월"]).sum()
print(res)
print("\n----------------------\n")
res = df.groupby(["지역명", "연도", "월"])["분양가"].agg("sum")
print(res)
print("\n----------------------\n")
"""

# 타이타닉
"""
import pandas as pd

tr = pd.read_csv("C:\\Users\\Catholic\\python\\happy\\data\\train.csv", index_col=0, encoding='cp949')
res = tr.isnull().sum()
print(res)
print("\n----------------------\n")
res = pd.crosstab(tr["Embarked"], tr["Survived"])
print(res)
print("\n----------------------\n")

# 컬럼 매핑
res = res.columns.map({0:"Dead", 1:"Alive"})
print(res)
print("\n----------------------\n")
"""






































