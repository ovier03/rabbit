# datetime 모듈의 datetime 함수를 dt라는 별명으로 사용
#from datetime import datetime as dt

# 현재 시간 출력 
#print (dt.now()) 

#datatime 이용 함수
"""
from datetime import datetime as dt
"""

# 특정 시간대의 현재 시간 출력
"""
from pytz import timezone
#tx = timezone('Asia/Seoul')
tz = timezone('UTC')
print("timezone :", dt.now(tz))
"""

# 문자열을 날짜로 변환 (지정해서 출력)
"""
date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object) 
"""

#날짜를 문자열로 변환
"""
date_object = dt.now()
date_string = date_object.strftime('%Y-%n-%d')
print(date_string)
"""

# 수정
"""
import mod.utils as mu
#import datetime as dt

#print (dt.now)
dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

res = mu.cvt_str2time
print(res)
"""

# os: 운영체제와 상호작용하기 위한 함수 제공

"""
import os

# 현재 작업한 디렉토리 출력
print(os.getcwd())

# 디렉토리 변경
os.chdir('../')

# 변경된 디렉토리 출력
print(os.getcwd)

# 파일 목록 출력
print(os.listdir())
 
# 디렉토리 삭제
os.rmdir('new_directory')
print(os.listdir())

# 디렉토리 생성
os.mkdir('new_directory')
print(os.listdir())
"""

# os 모듈
"""
import mod.utils as mu
import os

print(mu.get_curdir())

pname = "python"
mu.os_mkdir("python")
print(os.listdir(pname))

os.rmdir(pname)
print(os.listdir())
"""


# sys: python 인터프리터와 상호작용하기 위한 함수를 제공
"""
import sys

print(sys.version)
print(sys.argv)
"""

# stack

st = []

# 스택에 값 넣기
"""
st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)

print(st)

# 스택의 상태 확인하기
print(st) #[1, 2, 3]

#스택에서 값 빼기
top = st.pop()
print(top) 
print(st) 
print(len(st))
"""

# 큐

#빈 큐 생성
"""
queue = []

# 큐에 값 넣기
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)

#큐의 상태 확인하기
print(queue) #[1,2,3]

#큐에서 값 뺴기
front = queue.pop(0)
print(front) #1
print(queue) # [2,3]
print(len(queue))
"""