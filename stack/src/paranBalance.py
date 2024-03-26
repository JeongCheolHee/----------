from .Liststack import liststack

def paranBalance(s):
    st = liststack()
    for char in s:
        if char == '(':
            st.push(char)
        elif char == ')':
            if st.isEmpty():
                # 닫는 괄호가 더 많은 경우
                return False
            st.pop()
    # 스택이 비어있지 않으면 열린 괄호가 더 많은 경우
    return st.isEmpty()