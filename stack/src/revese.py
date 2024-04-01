from Liststack import liststack

def reverse(str):
    st = liststack()
    for i in range(len(str)):
        st.push(str[i])
    out = ""
    while not st.isEmpty():
        out += st.pop()
    return out


print(reverse("Test1234"))