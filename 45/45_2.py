_solution=lambda n,s,g:sum(min(_:=abs(a-b),10-_)for a,b in zip(s,g))
solution=lambda n,s,g:sum(min(_:=abs(a-b),10-_)for a,b in zip(s,g))

from test_c2 import tests

for i in tests:
    try:
        a=solution(*i[0])
        if a != i[1]:
            print("Failed.")
            print("test case: ")
            print("solution(" + str(i[0]) + ")")
            print("Your solution: " + str(a))
            print("The actual solution: " + str(i[1]))
            break
    except Exception as e:
        print("Your error: " + str(e))
        break
else:
    print("100% passed!")

print(solution(5, [1,9,3,5,2], [4,4,9,1,0]))
