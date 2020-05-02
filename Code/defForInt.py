#return값은 true or false
#token의 자료형은 string
#token이 int에 만족하는지 아닌지 판단하는 함수
#return은 bool값
#클래스에 합쳐줄수 있니?
#동작은 잘 하는거 같다
def isINTEGER(token):
    #string인 token에서 한글자씩 input
    state = ["T0","T1","T2","T3","T4","T5"]
    recentState = state[0]
    for input in token:
        if recentState == state[0]:
            if input == "-":
                recentState = state[1]
            elif input in ZERO:
                recentState = state[2]
            elif input in NON_ZERO:
                recentState = state[3]
            else:
                return False
        elif recentState == state[1]:
            if input in NON_ZERO:
                recentState = state[3]
            else:
                return False
        elif recentState == state[2]:
            return False
        elif recentState == state[3]:
            if input in ZERO:
                recentState = state[4]
            elif input in NON_ZERO:
                recentState = state[5]
            else:
                return False
        elif recentState == state[4]:
            if input in ZERO:
                recentState = state[4]
            elif input in NON_ZERO:
                recentState = state[5]
            else:
                return False
        elif recentState == state[5]:
            if input in ZERO:
                recentState = state[4]
            elif input in NON_ZERO:
                recentState = state[5]
            else:
                return False
    if recentState == state[2] or recentState == state[3] or recentState == state[4] or recentState == state[5]:
        return True
    else:
        return False