
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV 파일 불러오기
df = pd.read_csv("C:\\Users\\user\\Documents\\카카오톡 받은 파일\\유기동물보호+현황_20231205172845.csv")  

# 데이터프레임 내용 출력
print(df)


# 년도별 유기동물 보호 현황 시각화 [막대 그래프]
x = np.arange(3)
years = ['2018', '2019', '2020', '2021', '2022']
values = [275, 225, 138, 132, 62]

plt.bar(x, values)
plt.xticks(x, years)

plt.show()


"""
# '입양분양'가 가장 많은 보호소 상위 5개 출력
top_adoption_shelters = df.nlargest(5, '입양분양')
print("입양분양가 가장 많은 보호소 상위 5개:\n", top_adoption_shelters)

# '폐사안락사'가 가장 적은 보호소 상위 3개 출력
top_low_death_shelters = df.nsmallest(3, '폐사안락사')
print("\n폐사안락사가 가장 적은 보호소 상위 3개:\n", top_low_death_shelters)

# '입양비율' 계산하여 새로운 열 추가
df['입양비율'] = (df['입양수'] / df['유기동물수']) * 100

# '입양비율'이 가장 높은 보호소 상위 5개 출력
top_adoption_rate_shelters = df.nlargest(5, '입양비율')
print("\n입양비율이 가장 높은 보호소 상위 5개:\n", top_adoption_rate_shelters)
"""

"""
# 데이터 시각화
plt.figure(figsize=(10, 6))

plt.plot(df['Year'], df['Rescued'], marker='o', label='Rescued')
plt.plot(df['Year'], df['Adopted'], marker='o', label='Adopted')
plt.plot(df['Year'], df['Euthanized'], marker='o', label='Euthanized')

plt.title('유기동물 보호 현황')
plt.xlabel('Year')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.show()
"""















