def solution(x, y):
    for i in f'{y:08b}':x=(x>>1)if i=='1'else(x<<1)
    return x

import tqdm
import time
import json

with open("tests_c2.json", "r") as f:
    cases = json.load(f)

failed = []
t = time.time()

for i, j, k in tqdm.tqdm(cases):
    soln = solution(i, j)
    if soln != k:
        failed.append([(i, j), k, soln])

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

print(solution(2, 5))
print(solution(5, 100))
print(solution(69420, 255))
print(solution(255, 255))
print(f'{5:08b}')
print(f'{100:08b}')
print(f'{255:08b}')
