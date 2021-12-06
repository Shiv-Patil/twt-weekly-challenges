def solution(n):
    s,r=[],'';p,a=s.pop,s.append
    try:
        for i in n:a(int(i+'1')*p()+p())if i in('-','+')else a(int(chr(i+87)))if-40<(i:=ord(i)-87)<-29else a(p()*p())if i==-45else a(i)if 9<i<16else 0;r+=str(p())if i==23else''
    except:r="something smells fishy..."
    return r

import time
from tqdm import tqdm
import json

with open("tests1.json") as f:
  data = json.load(f)

failed_cases=[]
start=time.time()
last=start
for i in tqdm(data['cases'],desc=f"Testing: ", ncols=70):
    try:
        ans=solution(i[0])
        if ans!=i[1]:
            failed_cases.append(i+[ans])
    except BaseException as e:
        if "name 'solution' not defined" in str(e):
            print("\nPlease copy solution in designated area in source code")
            quit()
        else:
            failed_cases.append(i+["Error: "+str(e)])


end=time.time()

print(f"""\nPassed: {len(data['cases'])-len(failed_cases)}/{len(data['cases'])}
Time: {end-start}
{"Failed_cases:"if failed_cases else ""}""")

for t in failed_cases[:min(3,len(failed_cases))]:
    print(f"""Input: {t[0]}
your answer: {t[2]}
Actual answer: {t[1]}""")
