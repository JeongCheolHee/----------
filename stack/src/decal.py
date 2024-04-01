from Liststack import liststack

def decal(s):
    st = liststack()
    mid_found = False
    
    for char in s:
        if char == '$':
            mid_found = True
            continue
        
        if not mid_found:
            st.push(char)
        else:
            if st.isEmpty() or st.pop() != char:
                return False
    
    return st.isEmpty() and mid_found

print(decal("ab$ba"))  # True
print(decal("abc$abc"))  # False