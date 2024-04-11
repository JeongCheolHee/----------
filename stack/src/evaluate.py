from Liststack import liststack

def evaluate(p):
    s= liststack()
    digitPreviously = False
    for i in range(len(p)):
        ch = p[i]
        if ch.isdigit():
            if digitPreviously:
                tmp = s.pop()
                tmp = 10 * tmp + (ord(ch)-ord('0'))
                s.push(tmp)
            else:
                s.push(ord(ch)-ord('0'))
                digitPreviously = True
        elif isOperator(ch):
            result = operation(s.pop(), s.pop(), ch)
            s.push(result)
            digitPreviously = False
        else: # 공백일 때
            digitPreviously = False
    return s.pop()


def isOperator(ch) -> bool: # 연산자 이면 True, 아니면 False
    return (ch == "+" or ch == "-" or ch == '*' or ch == '/')

def operation(opr2 : int, opr1 : int, ch) -> int: # 스택 맨 위에 있던 것이 opr2 
    return {'+': opr1 + opr2, '-' : opr1 - opr2, '*' : opr1 * opr2, '/': opr1 // opr2}[ch]



def main():
    posfix = "700 3 47 + 6 * - 4 /"
    print("input: ", posfix)
    answer = evaluate(posfix)
    print("Anser :", answer)
if __name__ == "__main__":
    main()
