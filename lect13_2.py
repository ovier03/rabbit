"""
import matplotlib.pyplot as plt
x_years = ["2020", "2021", "2022"]
y_data = ["200", "400", "600", "800"]
clr = ["r", "g", "b]
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="//")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="///")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="////")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\\")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="+")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="+++")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="+")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="*")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="o")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="oo")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="x")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="xx")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch=".")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="..")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="...")
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="....")
plt.show()
"""

# 산점도 그래프 그리기
"""
x = 1
y = 1
plt.scatter(x, y)
plt.scatter(x+1, y+1)
plt.scatter(x+2, y+1)
plt.scatter(x+3, y+1)
plt.scatter(x+3, y+2)
plt.scatter(x+3, y+3)
plt.scatter(x+3, y+4)
plt.scatter(x+4, y+1)
plt.scatter(x+4, y+2)
plt.scatter(x+4, y+3)
plt.scatter(x+4, y+4)
"""

# {x}{y}{포인트크기}{색상설정}{투명}
"""
plt.scatter(x+1.5, y+1.5, 100, 2)
plt.scatter(x+1.5, y+1.5, 150, 3)
plt.scatter(x+1.5, y+1.5, 200, 4)

plt.scatter(x+1.5, y+1.5, 200, 2, alpah=0.5)

plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="cividis")
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="spectral")
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="viridis")
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="plasma")
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="inferno")
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="magma")

plt.colorbar()
plt.show()
"""


# 히스토그램 그리기
"""
import numpy as np
rn = np.random.randint(1, 30, size=20)
print(rn)
plt.hist(rn, bins=10, label="def")
plt.legend()
plt.show()


plt.hist(rn, bins=20)

# 라벨 설정
plt.hist(rn,  bins=10, label="def") 

# 투명도 설정
plt.hist(rn,  bins=10, label="def", alpha=0.5)

# 그래프 스타일 설정
plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="step")
plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="stepfilled")
plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="barstacked")
"""


# 파이차트 그리기
"""
rate = [30, 40, 20, 10]
labels = ["Alpha", "Beta", "Gamma", "Delta"]
plat.pie(rate)

plt.show()

#
# 라벨 표시
plt.pie(rate, labels=labels)

# 퍼센트 표시
plt.pie(rate, labels=labels, autopct='%.1d%%')
plt.pie(rate, labels=labels, autopct='%.1f%%')
plt.pie(rate, labels=labels, autopct='%.2f%%')

# 시작각도 설정 abcd
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=270)

# 시계방향으로 시작
plt.pie(rate, labels=labels, autopct='%.1f%%', counterclock=False)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=False)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=180, counterclock=False)
plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=270, counterclock=False)

# 공백 설정
plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0, 0, 0])
plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[1, 1, 1, 1])
plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0.1, 0.1, 0.1, 0.1])
plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.1, 0, 0.1])
plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.5, 0, 0.5])
plt. show()

# 패널 스타일 설정
# 사용가능한 스타일 키
print(plt.style.available)

plt.style.use("bmh")
plt.style.use("ggplot")
plt.style.use("classic")
plt.style.use("Solraize_Light2")
plt.style.use("dark_background")
plt.style.use("fast")
plt.style.use("grayscale")
plt.plot([2,3,6,7,10], [1,4,5,8,9])

plt.show()

# 포맷 설정
plt.plot([2,3,6,7,10], [1,4,5,8,9])
plt.rcParams['figure.figsize'] = (1, 2)
plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['font.size'] = 20
plt.rcParams['lines.linewidth'] = 50
plt.rcParams['lines.linestyle'] = '--'
plt.rcParams['lines.linestyle'] = '-'
# 위 눈금 설정
plt.rcParams['xtick.top'] = True

# 오른 눈금 설정
plt.rcParams['ytick.right'] = True

# 안쪽으로 눈금 설정
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

# 눈금 길이
plt.rcParams['ytick.major.size'] = 12

# 세부 눈금
plt.rcParams['xtick.minor.visible'] = True

# 객체 활용
fig, ax = plt.subplots()

ax = fig.add_axes([0, 0, 0, 0])
ax = fig.add_axes([1, 1, 0, 0])
ax = fig.add_axes([1, 1, 1, 1])
plt.show()

# 다중행열구성
fig, ax = plt.subplots(1, 1)
fig, ax = plt.subplots(1, 2)
fig, ax = plt.subplots(2, 1)
fig, ax = plt.subplots(2, 2)
fig, ax = plt.subplots(3, 2)
fig, ax = plt.subplots(3, 3)
plt.show()

# 다중객체 그래프 구성
x = [1,4,5,8,9]
y1 = [2,3,6,7,10]

fig, ax = plt.subplots(2, 2)
fig, ax = plt.subplots(2, 2, sharex=True)
fig, ax = plt.subplots(2, 2, sharey=True)

# y축 동시 출력
x = [1,4,5,8,9]

y1 = [2,3,6,7,10]
y2 = [10,8,6,4,2]

fig, ax1 = plt.subplots()
ax1.set_xlabel("X-Data")
ax1.set_ylabel("Y1")
ax1.plot(x, y1)

ax2 = ax1.twinx()
ax2.set_ylabel("Y2")
ax2.plot(x, y2)

# 개별색상 설정

ax1.plot(x, y1, color="C1")
ax2.plot(x, y2, color="C2")

# 개별라벨 출력
ax1.plot(x, y1, color="C1", label="y1 Data")
ax1.legend(loc="upper right")

ax2.plot(x, y2, color="C2", label="y2 Data")
ax2.legend(loc="lower right")

# 이종그래프 출력
x = [1,4,5,8,9]
y1 = [2,3,6,7,10]
y2 = [2,3,6,7,10]

fig, ax1 = plt.subplots()

ax1.plot(x, y1, "-o", color="C1")
ax1.set_xlabel("X")
ax1.set_ylabel("Ydata")
ax1.legent()

ax2 = ax1.twinx()
ax2.bar(x, y2, color="C2")
ax2.set_ylabel("Y2data")

plt.show()
"""