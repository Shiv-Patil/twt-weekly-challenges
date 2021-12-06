def solution(s):
 s=s.split();k,l=s[:],len(s)
 for n in range(l):s[n],s[n-1]=((k[n-1][0]+s[n][1:],s[n-1][:-1]+k[n][-1]),(s[n][:-1]+k[n-1][-1],k[n][0]+s[n-1][1:]))[l&1]
 return' '.join(s)

import tqdm
import time
import json

with open("tests_c1.json", "r") as f:
    cases = json.load(f)

failed = []
t = time.time()

for i in tqdm.tqdm(cases):
    soln = solution(i)
    if soln != cases[i]:
        failed.append([i, cases[i], soln])

print(f"\nFinished in {time.time() - t} seconds")
print(f"Failed {len(failed)} cases.\n--------------------------------------")

if not failed:
    quit()

for e, i in enumerate(failed[:5]):

    print(f"Failed Case {e + 1}:")
    print(f"Case: {i[0]}")
    print(f"Correct Answer (According to my solution): {i[1]}")
    print(f"Your Answer: {i[2]}")

    print("--------------------------------------")

print(solution("Hello World"))
