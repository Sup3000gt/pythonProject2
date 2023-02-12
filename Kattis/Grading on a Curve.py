a, b = input().split()      # get student score,
student = int(a)            # change to int
score = int(b)
score_list = []
for i in range(student):    # put in a list
    score_list.append(int(input()))
score_list.sort()           # sort the list, "this is important"
A = int(3 / 4 * student)    # since we want 1/4 of people get A, which means we want the 3/4index of the list
B = int(1 / 2 * student)    # same for B and C
C = int(1 / 4 * student)
curveA = score_list[A] // 0.9   # use floor division to get whole number instead of float
curveB = score_list[B] // 0.8
curveC = score_list[C] // 0.7
if curveA ==0 or curveB == 0 or curveC == 0:    # we want to see which curve point is the smallest to meet our requirement
    print(-1)               # if we got a curve == 0  means at least 1/4 of student are getting 0 return -1
else:
    print(int(min(curveA, curveB, curveC)))     # else we return min
