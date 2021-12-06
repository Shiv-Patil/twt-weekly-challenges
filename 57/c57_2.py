f=input;u=int
for _ in' '*u(f()):
 *j,=map(lambda x:x.split(),map(f,['']*(n:=u(f()))));j.sort(key=lambda y:u(y[2]));z=[0]*n
 for m in reversed(j):
  for s in range(min(n,u(m[1]))-1,-1,-1):
   if not(z[s]):z[s]=m[0];break
 print(' '.join(filter(None,z)))
