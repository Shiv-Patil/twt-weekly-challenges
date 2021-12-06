def solution(string,times):
    answer,_,char,string,count=[string],'',0,str(string),1
    for kek in range(times-1):
        while char <= len(string)-1:
            if char<len(string)-1:
                while string[char]==string[char+1]:
                    count+=1;char+=1
                    if len(string)==char+1:break
            _+=f"{count}{string[char]}";count=1;char+=1
        answer.append(int(_));string,_,char=_,'',0
    return answer if times else[]

import time
import tqdm
from test_c2 import tests

passed = 0
failed = {}
start = time.time()

for i in tqdm.tqdm(tests):
        r, n = i[0], i[1]
        ans = solution(r, n)
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