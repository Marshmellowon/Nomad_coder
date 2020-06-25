def plus(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def pow(a, b):
    return a ** b


def remain(a, b):
    return a % b


def calculate(a, b, c):
    aint = int(a)
    cint = int(c)
    if b == "+":
        return plus(aint, cint)
    elif b == "-":
        return sub(aint, cint)
    elif b == "*":
        return mul(aint, cint)
    elif b == "/":
        divRes = div(aint, cint)
        return divRes
    elif b == "**":
        return pow(aint, cint)
    elif b == "%":
        return remain(aint, cint)


if __name__ == '__main__':
    a = input("숫자를 입력하세요: ")
    b = input("연산자를 입력하세요: ")
    c = input("숫자를 입력하세요: ")

    print("연산 결과는 : ", calculate(a, b, c), "입니다.")
