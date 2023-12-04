"""
import matplotlib.pyplot as plt

# 기본사용 y축
value = [1, 2, 3, 4]
#value = [2, 4, 5, 7, 10]
res = plt.plot(value)
plt.show()

# x, y축 두 축 지정 구성

# x_value = [2, 3, 6, 7, 10 ]
# y_value = [1, 4, 5, 8, 9]

# plt.plot(x_value, y_value)
# res = plt.plot([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
# plt.show()
"""

# 딕셔너리 설정 
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.show()
"""

# 레이블 설정
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

plt.xlabel("x_data")
# plt.xlabel("y_data")
plt.ylabel("y_data")
plt.show()
"""

#레이블 여백/위치 조절
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

# plt.xlabel("x_data", labelpad=15)
# plt.ylabel("y_data", labelpad=50)

# plt.xlabel("x_data", loc="right")
# plt.ylabel("y_data", loc="top")
# plt.show() 

plt.xlabel("x_data", labelpad=15, loc="left")
plt.ylabel("y_data", labelpad=50, loc="bottom")
plt.show()
"""

# 다중데이터 출력
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)
# plt.plot([1, 4, 5, 9], [2, 3, 8, 10])

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


# 위치조절
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x_data")
plt.ylabel("y_data")

# plt.legend()
# plt.legend(loc=(1, 1))
# plt.legend(loc="best")

# plt.legend(loc=(0.5, 0.5))
# plt.legend(loc=(0.3, 0.3))

# plt.legend(loc="lower right")
# plt.legend(loc="center right")
# plt.legend(loc="upper right")
# plt.legend(loc="upper left")
# plt.legend(loc="upper center")
plt.show()
"""

# 라벨 설정 
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.plot("x1_data", "y1_data", data=dic1_val, label="Value(m)")

plt.xlabel("x_data")
plt.ylabel("y_data")
"""

# col 조절 
# plt.legend(ncol=1)
# plt.legend(ncol=2)

# 폰트조절
# plt.legend(ncol=2, fontsize=10)
# plt.legend(ncol=2, fontsize=20)

# 테두리 설정
# plt.legend(ncol=2, fontsize=20, frameon=True)
# plt.legend(ncol=2, fontsize=20)
# plt.legend(ncol=2, fontsize=20, frameon=False)

# 테두리 음영 설정
# plt.legend(ncol=2, fontsize=20, frameon=True,  shadow=True)
# plt.legend(ncol=2, fontsize=20, shadow=True)

# plt.show()


# 축 범위 지정
"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data")
plt.ylabel("y_data")

# plt.xlim()
# plt.ylim()


# 현재 축 범위 출력
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
print(x_min, x_max)
print(y_min, y_max)
"""


# 축 계산
# plt.xlim(x_min - 0.6, x_max)
# plt.ylim(y_min - 0.6, y_max)


# 축 범위 지정
# plt.xlim([0, 10])
# plt.ylim([0, 10])

# plt.xlim([0, 50])
# plt.ylim([0, 50])

# plt.xlim([-5, 50])
# plt.ylim([5, 50])

# plt.xlim([0, 10])
# plt.ylim([0, 10])
# plt.axis([0, 10, 0, 10])

# plt.xlim([-5, 10])
# plt.ylim([-5, 10])
# plt.axis([-5, 10, -5, 10])

# plt.xlim([0, 50])
# plt.ylim([0, 50])
# plt.axis([0, 50, 0, 50])

# plt.xlim([0, 20])
# plt.ylim([0, 50])
# plt.axis([0, 20, 0, 50])

# x_min, x_max, ymin, ymax = plt.axis()
# print(x_min, x_max, ymin, ymax)

# plt.axis("square")
# plt.axis("scaled")
# plt.axis("tight")
# plt.axis("on")
# plt.axis("off")
# plt.axis("equal")
# plt.axis("auto")

# plt.show()


# 선 스타일 설정

# plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")

# plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "--", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ":", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "-.", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ".", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ".-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ".--", label="PData(km)")

# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", label="PData(km)")

# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 0)), label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (4, 0)), label="PData(km)")


# dash
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (5, 1)), label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (5, 5)), label="PData(km)")

# dot
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 1)), label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 2)), label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 5)), label="PData(km)")

# dashdot
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (5, 1, 1, 3)), label="PData(km)")


# 색
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="b", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="g", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="lime", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#35FA8D", label="Value(m)")


# 스타일

# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, color="C6", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=5,  color="C6", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="butt", color="C6", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", color="C6", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, solid_capstyle="round", color="C6", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, dash_capstyle="round", color="C6", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dotted", linewidth=10, dash_capstyle="round", color="C6", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dotted", linewidth=10, solid_capstyle="round", color="C6", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashdot", linewidth=10, dash_capstyle="round", color="C6", label="Value(m)")


# 마커 지정 

# plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo", label="PData(km)")

# plt.plot([2,3,6,7,10], [1,4,5,8,9], "b0-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo--", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-.", label="PData(km)")

# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker = "H", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker = "D", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker = "X", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker = 11, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker = "s", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker = "$test$", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker = "$y$", label="PData(km)")


# 그래프 영역 채우기
""" 
xdata = [2, 3, 6, 7, 10]
ydata = [1, 4, 5, 8, 9]
y1data = [2, 4, 6, 8, 10]

plt.plot(xdata, ydata)
plt.xlabel("x_data")
plt.ylabel("y_data")
"""

# 세로축 세우기
# plt.fill_between(xdata[1:4], ydata[2:4], alpha=0.5)
# plt.fill_between(xdata[1:4], ydata[2:4], alpha=1)
# plt.fill_between(xdata[2:4], ydata[2:4], alpha=0.5)
# plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
# plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.3)

# 가로축 세우기 
# plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
# plt.fill_betweenx(ydata[2:4], xdata[2:4], alpha=0.3)

# plt.plot([1,3,5,7,9], [2,4,6,8,10])
# plt.plot(xdata, y1data)

# 두 선간 채우기 
# plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
# plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], alpha=0.5)
# plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], color="C1" alpha=0.5)


# 영역 채우기 
# plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.5, 6.0], alpha=0.5)
# plt.fill([1.9, 1.9, 3.1, 3.1], [0.5, 2.5, 5.5, 3.1], alpha=1)

# plt.show()


"""
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val, label = "PData(km)")
plt.plot("x1_data", "y1_data", data=dic1_val, label = "Value(m)")
#plt.plot([1, 4, 5, 9], [2, 3, 8, 10])

plt.xlabel("x-data")
plt.ylabel("y-data")
"""

# 배경 그리드 설정 

# plt.grid()

# plt.grid(axis="x")

# plt.grid(axis="y")
# plt.grid(color="g", alpha=0.5, linestyle="-")
# plt.grid(color="g", alpha=0.5, linestyle="")

# plt.grid(axis="y", color="g", alpha=0.5, linestyle="-")
# plt.grid(axis="x", color="r", alpha=0.3, linestyle="-.")


# 눈금표시 

# plt.xticks()
# plt.yticks()

# plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
# plt.yticks([0,1,2,3,4,5,6,7,8,9,10])

# plt.xticks([1, 3, 5, 7, 9, 11])
# plt.yticks([2, 4, 6, 8, 10, 12])

# plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
# plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
# plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# plt.tick_params(axis="x", direction="in")
# plt.tick_params(axis="x", direction="out")
# plt.tick_params(axis="y", direction="in")

# plt.show()


# 막대그래프 
"""
x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "g", "b"]

# plt.bar(x_years, y_data)


# 색지정
# plt.bar(x_years, y_data, color="g")
# plt.bar(x_years, y_data, color="C7")
# plt.bar(x_years, y_data, color="#57ADCC")

# 개별 색 지정 
# plt.bar(x_years, y_data, color=clr)

# 너비 설정 
# plt.bar(x_years, y_data, color=clr, width=2)
# plt.bar(x_years, y_data, color=clr, width=0.5)
# plt.bar(x_years, y_data, color=clr, width=0.1)

# 막대 위치 선정
# plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
# plt.bar(x_years, y_data, color=clr, align="center", width=0.5)

# 막대 테두리 설정 
# plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)
# plt.bar(x_years, y_data, color=clr, align="center", edgecolor="C3", linewidth=3, width=0.5)
# plt.bar(x_years, y_data, color=clr, align="center", edgecolor="blue", linewidth=3, width=0.5)

# 축 지표 설정 

# plt.yticks(100, 200, 300, 400, 500, 600, 900)


# 수평그래프 
# plt.barh(x_years, y_data)

plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)





plt.show()
"""