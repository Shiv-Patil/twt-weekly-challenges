def a(x,u):
 s=r=u//x;n=3;l=-1
 while 1:
  r=r//(x*x);t=r//n
  if not t:break
  s+=l*t;l=-l;n+=2
 return s
def r(p):
 u=10**(p+10);i=4*(4*a(5,u)-a(239,u));return i//10**10
solution=lambda n:int(str(r(n+1))[n])

print(solution(0))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
