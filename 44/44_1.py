solution=lambda n:[sum(n)%2^n.pop(0)for _ in n[:]]

from tqdm import tqdm
import time,json

with open('test_c1.json','r') as f:
    cases=json.load(f)['cases']

passed=0
start=time.time()
failed_cases=[]
for test in tqdm(cases,desc="Testing"):
    inp,ans=test
    try:
        user_ans=solution(inp)
        if ans==user_ans:
            passed+=1
        else:
            failed_cases.append(test+["Your Answer: "+str(user_ans)])
    except BaseException as e:
        if "name 'solution' is not defined" in str(e):
            print("\nPlease copy paste/import your solution into this file in the designated area.")
            quit()
        failed_cases.append(test+["Error: "+str(e)])

end=time.time()

print(f"""Passed: {passed}/{len(cases)}
time: {end-start}""")

if failed_cases:
    print("Some failed cases: ")
    for test in failed_cases[:5]:
        print(f"""Candles = {test[0]}
Correct answer: {test[1]}
{test[2]}""")

print(solution([1, 1, 1, 1, 1]))