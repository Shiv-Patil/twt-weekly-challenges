_=lambda x:x if x<10 else _(sum(list(map(int,list(str(x))))));solution=_
print(solution(942))