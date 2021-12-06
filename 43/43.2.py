def __solution(n):
    r=' ';g={r*2:r}
    for i in range(1,26):g[f"{int(i/5.1)+1}{round(i%5.1)}"]=chr(i+97)if i>9else chr(i+96)
    if n[0]in'12345':n=n.replace(r,r*2);[r:=r+g[i+k]for i,k in zip(n[0::2],n[1::2])];n=''
    for i in n:r+={v:k for k,v in g.items()}.get(i,'24')
    return r[1:]

def _solution(n):
    r,i,n,g='',0,n.split(' '),{}
    for _ in range(1,26):g[f"{int(_/5.1)+1}{round(_%5.1)}"]=chr(_+97)if _>9else chr(_+96)
    for s in n:
        while i<len(s):
            if s[i]in'12345':r+=g[s[i]+s[i+1]];i+=2
            else:r+={v:k for k,v in g.items()}.get(s[i],'24');i+=1
        n[n.index(s)],i,r=r,0,''
    return' '.join(n)

def solution(d,r=''):
    s=[*d]
    while s:a=s.pop();r=(chr((n:=int(s.pop())*5+~-int(a))+(n>13)+92)if'/'<a<':'else[' ',f'{(a:=ord(a)-92-(a>"i"))//5}{a%5+1}'][a>0])+r
    return r

import time
import tqdm
from tests2 import tests

passed = 0
failed = {}
start = time.time()

for i in tqdm.tqdm(tests):
    ans = solution(i)
    if tests[i] == ans:
        passed += 1
    else:
        failed[i] = {}
        failed[i]['correct'] = tests[i]
        failed[i]['your_answer'] = ans

print(f"Time Taken: {round(time.time()-start, 2)} seconds")
print(f"Passed {passed}/{len(tests)}\n\n")

if failed:
    keys = list(failed.keys())[:3]
    for i in keys:
        print(f"Input: {i}\nCorrect Answer: {failed[i]['correct']}\nYour Answer: {failed[i]['your_answer']}\n")
print(solution("3534315412244543     434145114215"))