# 과제 1 사칙연산 계산기 프로그램을 만들어주세요.

# 사용자로부터 "숫자 연산자 숫자" 를 입력받아 결과값을 출력해주세요.
# 사용자가 c를 입력하면 다시 입력받아야하고 e를 입력하면 계산기가 종료되어야합니다.
# e를 입력하기 전까지는 계산기가 끝나면 안됩니다.
# 숫자나 연산자를 잘못 입력하면 다시 입력받도록 해주세요.
a = "a"
b = "b"
d = "d"
while True:
    print('사칙연산 계산기 입니다. 숫자나 연산자를 잘못 입력하면 처음으로 돌아갑니다.')
    a = (input("첫 번째 수를 입력하세요:"))
    if a == "c":
        continue
    elif a == "e":
        break
    elif a.isdigit() == False:
        print("숫자를 입력해주세요")
        continue
    a = int(a)

    d = input("연산자를 입력하세요:")
    if d == "c":
        continue
    elif d == "e":
        break
    elif d == "+" or "-" or "*" or "/":
        pass



    b = (input("두 번째 수를 입력하세요:"))
    if b == "c":
        continue
    elif b == "e":
        break
    elif b.isdigit() == False:
        print("숫자를 입력해주세요")
        continue
    b = int(b)

    if d == "+":
        print("%d+%d=%d" % (a, b, a + b))
    elif d == "-":
        print("%d-%d=%d" % (a, b, a - b))
    elif d == "*":
        print("%d*%d=%d" % (a, b, a * b))
    elif d == "/":
        print("%d/%d=%d" % (a, b, a / b))

print("계산기 종료")