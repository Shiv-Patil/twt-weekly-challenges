U,I=int,input
for _ in' '*U(I()):
 i=[0]
 for e in (l:=list(map(U,I().split()))):
  if(k:=(i[0]+l[i[0]])%len(l))not in i:i=[k]+i;continue
  if len(i)==len(l)and k==0 and l[0]!=0:continue
  print(False);break
 else:print(True)
