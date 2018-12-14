## 후위표기법을 이용하여 사칙연산하기

infix = ['(', '2', '+', '3', ')', '*', '4']
postfix = []
stack = []
result = []
operator = ['*', '/', '+', '-']
bracket = ['(', ')']

def is_number(x):
    if x not in operator and x not in bracket:
        return True
    else:
        return False


def pref(x):
    if x is '*' or '/':
        return 1
    elif x is '+' or '-':
        return 0


def calc_two_oprd(oprd1, oprd2, oprt):
    if oprt == '+':
        return oprd1 + oprd2
    elif oprt == '-':
        return oprd1 - oprd2
    elif oprt == '*':
        return oprd1 * oprd2
    elif oprt == '/':
        return oprd1 // oprd2


def calc(post):
    for p in post:
        if is_number(p):
            result.append(int(p))
        else:
            oprd2 = result.pop()  # 먼저 뽑은걸 2로.
            oprd1 = result.pop()
            result.append(calc_two_oprd(oprd2, oprd1, p))
    return result.pop()


def main():
    for c in infix:
        if is_number(c):
            postfix.append(c)
        elif c in operator:
            p = pref(c)
            while len(stack) > 0:
                top = stack[-1]
                if p >= pref(top):
                    break
                postfix.append(stack.pop())
            stack.append(c)

        elif c == '(':
            stack.append(c)
        elif c == ')':
            while True:
                x = stack.pop()
                if x == '(':
                    break
                postfix.append(x)

    while len(stack) > 0:
        postfix.append(stack.pop())

    print("{} 의 결과는 {}".format(postfix, calc(postfix)))


if __name__ == "__main__":
    main()