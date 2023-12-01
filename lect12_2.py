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



# 연령대별 생존자
res = pd.crosstab(tr["Age"], tr["Survived"])
print(res)
print("\n----------------------\n")

# 승차등급별 생존자
res = pd.crosstab(tr["Pclass"], tr["Survived"])
print(res)
print("\n----------------------\n")

# 성별별 생존자
res = pd.crosstab(tr["Sex"], tr["Survived"])
print(res)
print("\n----------------------\n")

# 호칭별 구분
tr["Title"] = tr.Name.str.extract(" ([A-Za-z]+)\.")
res = tr["Title"].value_counts()
print(res)
print("\n----------------------\n")

# 호칭 수정
tr["Title"] = tr["Title"].replace(["Capt", "Col", "Countess", "Don","Dona", "Dr", "Jonkheer", "Lady","Major", "Rev", "Sir"], "Other")
tr["Title"] = tr["Title"].replace("Mlle", "Miss")
tr["Title"] = tr["Title"].replace("Mme", "Mrs")
res = tr["Title"] = tr["Title"].replace("Ms", "Miss")
print(res)
print("\n----------------------\n")

# age 별 Null 확인
res = tr["Age"].isnull()
print(res)
print("\n----------------------\n")

# 그룹별 평균 나이
meanAge = tr[["Title", "Age"]].groupby(["Title"]).mean()
print(meanAge)
print("\n----------------------\n")

# 빈 나이 평균값 채워넣기
for index, row in meanAge.iterrows():
    nullIndex = tr[(tr.Title == index) & (tr.Age.isnull())].index
    # print(nullIndex, index, row[0])
    tr.loc[nullIndex, "Age"] = row[0]
print("\n----------------------\n")

# 나이 구간 나누기
print(tr["Age"].head(20))
print("\n----------------------\n")
print(tr["Age"].isnull().sum())
print("\n----------------------\n")
tr["AgeCate"] = pd.qcut(tr.Age, 8, labels=range(1, 9))
print(tr.head())
print("\n----------------------\n")
print(tr.dtypes)
print("\n----------------------\n")
tr.AgeCate = tr.AgeCate.astype(int)
print(tr.head())

# 방 번호별 탑승자
tr["CabinCate"] = tr["Cabin"].str.slice(start=0, stop=1)
print(tr["CabinCate"].value_counts())
print("\n----------------------\n")

# 방 번호 매핑
tr["CabinCate"] = tr["CabinCate"].map({ "N": 0, "C": 1, "B": 2, "D": 3, "E": 4, "A": 5, "F": 6, "G": 7, "T": 8 })
print(tr["CabinCate"].value_counts())
print(tr)
print("\n----------------------\n")

# 방 번호별 생존자
res = pd.crosstab(tr["CabinCate"], tr["Survived"])
print(res)
print("\n----------------------\n")

# 요금컬럼 별 구간 구분
tr["FareCate"] = pd.qcut(tr.Fare, 8, labels=range(1, 9))
tr.FareCate = tr.FareCate.astype(int)
print(tr["FareCate"].value_counts())
print("\n----------------------\n")

# 요금 구간별 생존자
res = pd.crosstab(tr["FareCate"], tr["Survived"])
print(res)
print("\n----------------------\n")
"""

# 아이리스 정보처리

# 파일열기
"""
import pandas as pd

df = pd.read_csv("C:\\Users\\Catholic\\python\\happy\\data\\Iris.csv", index_col=0, encoding='cp949')

# 컬럼 매칭
ir = df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"},
)
print(ir.head())
print("\n----------------------\n")

# 컬럼 선택
res = ir.iloc[:, [0, 1, 4]]
print(res)
print("\n----------------------\n")

# 공통 string 제거
ir = ir["품종"].str[5:]
print(ir)
print("\n----------------------\n")

# 그룹핑
res = ir.groupby("품종").mean()
print(res)
print("\n----------------------\n")
res = ir["품종"].value_counts()
print(res)
"""

# 데이터 시각화
"""
import matplotlib.pyplot as plt

# 기본사용 y축
value = [1, 2, 3, 4]
# value = [2, 4, 5, 7, 10]
res = plt.plot(value)
plt.show()
"""

# 두 축 설정하기
"""
x_value = [2, 3, 6, 7, 10 ]
y_value = [1, 4, 5, 8, 9]

plt.plot(x_value, y_value)
res = plt.plot([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
plt.show()
"""

# 딕셔너리 사용, 두 축 지정 구성
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.show()
"""

#레이블 설정
#레이블 이름 설정
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.show()
"""

#레이블 여백 조절/ 위치 조절
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

plt.xlabel("x_data", labelpad=15)
plt.ylabel("y_data", labelpad=50)

# plt.xlaber("x_data", labelpad=15, loc="right")
# plt.xlaber("x_data", labelpad=50, loc="top")

# plt.xlaber("x_data", labelpad=15, loc="left")
# plt.xlaber("x_data", labelpad=50, loc="bottom")

plt.show()
"""

# 다중데이터 출력 
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.show()
"""

# 라벨 출력
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x_data")
plt.ylabel("y_data")
plt.legend()

plt.show()
"""

# 라벨 위치 조절
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x_data")
plt.ylabel("y_data")
plt.legend()

# plt.legend(loc=(1, 1))
# plt.legend(loc="best")
# plt.legend(loc=(0.5, 0.5))
# plt.legend(loc=(0.3, 0.3))
# plt.legend(loc="lower right")
# plt.legend(loc="upper right")
# plt.legend(loc="upper left")
# plt.legend(loc="upper center")
plt.show()
"""

# 라벨 설정
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.legend(ncol=1)
plt.legend(ncol=2)
plt.show()

# 폰트 조절
plt.legend(ncol=2, fontsize=10)

# 테두리 설정 

plt.legend(ncol=2, fontsize=10, frameon=True)
plt.legend(ncol=2, fontsize=10, frameon=False)

# 테두리 음영 설정

plt.legend(ncol=2, fontsize=20,frameon=True, shadow=True)
"""

# 축 범위 지정
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data")
plt.ylabel("y_data")
"""

"""
plt.xlim()
plt.ylim()

plt.show()
"""

# 현재 축 범위 출력
"""
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
print(x_min, x_max)
print(y_min, y_max)
"""

# 축 계산
"""
plt.xlim(x_min - 0.6, x_max)
plt.ylim(y_min - 0.6, y_max)
"""

# 축 범위 지정
"""
plt.xlim([0, 10])
plt.ylim([0, 10])
"""

"""
plt.xlim([0, 50])
plt.ylim([0, 50])

plt.show()

# 두축 값 동시 확인

x_min, x_max, ymin, ymax = plt.axis()

# 두 축을 동시 지정

#        x.min, x.max, y.min, y.max
plt.axis([0, 10, 0, 10])
plt.axis([0, 20, 0, 50])

# 축 출력 옵션 지정

plt.axis("square")
# plt.axis("scaled")
# plt.axis("equal")
# plt.axis("tight")
# plt.axis("auto")
# plt.axis("on")
# plt.axis("off")
"""

# 선 스타일 설정
"""
plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "--", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ":", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ".", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9],"-.", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ".-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ".--", label="PData(km)")
"""

# 선 스타일 지정
"""
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")

# 선 스타일 수동 설정
# linestyle(0, (픽셀크기, 여백간격))
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 0)), label="PData(km)")

# 문자열 색 지정
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")

# 키워드 색 지정
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")

# hex = rgb값 적용 색 지정
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#75FA8D", label="Value(m)")

# 지정 키 색 지정
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C0", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C2", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C3", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C4", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C5", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C7", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C8", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C9", label="Value(m)")

# 모양 설정
plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")

# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, solid_capstyle="round", label="Value(m)"

plt.show()
"""