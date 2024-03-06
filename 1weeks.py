# 하노이 타워 

def move(n, src, dest, tmp):
    if n > 0:
        move(n-1, src, tmp, dest)
        print("move %d from %c to %c" % (n, src, dest))
        move(n-1, tmp, dest, src)
print(move(3, 'a', 'c', 'b'))

# 2^n을 계산해주는 pow2(n)을 재귀적으로 구현

def pow2(n):
    if n == 1:
        return 2
    else:
        return 2 * pow2(n-1)
    
print(pow2(100))

# 리스트에서 최대값을 찾는 프로그램을 재귀적으로 만들기

def max(num, n):
    if n == 0:
        return num[0]
    else:
        max_of_rest = max(num, n - 1)
        if num[n] > max_of_rest:
            return num[n]
        else:
            return max_of_rest

num = [2, 4, 1, 18, 9, 3]

print(max(num, len(num)-1))