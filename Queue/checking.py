# 입력으로 들어온 문자열이 다음 집합의 원소인지 체크하는 코드를 큐를 이용해서 작성하시오.  
# { w$w | w: 문자열}

from src.ListQueue import *

def checking(s:str):
    st = ListQueue()
    i = 0
    for i in range(len(s)):
        if s[i] == '$': break
        st.enqueue(s[i])
        
    for j in range(i+1, len(s)):
        if st.isEmpty(): return False
        if st.dequeue() != s[j]: return False
    if st.isEmpty(): return True
    else: return False

print(checking('abccc$dfdf'))
print(checking('ab$ab'))

