def solution(e):a,o,b=e.split();a,m,b=map(int,(a,o+'1',b));r=lambda x:f"{x%256:b}";return(z:=a+b*m,r(a)+f" {o} {r(b)} = "+r(z))*(-129<z<128)or"Invalid"

print(solution("2 + 5"))
print(solution("0 + -1"))
print(solution("100 + 100"))
