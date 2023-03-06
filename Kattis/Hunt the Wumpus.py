S = int(input())
def newS(S):
    return S + (S // 13) + 15

lst =[]
while len(lst) < 4:
    SS = str(newS(S))
    wumpus = SS[-2:]
    if wumpus not in lst:
        lst.append(wumpus)
    S = int(SS)

moves = 0
while len(lst) > 0:
    guess = input()
    if guess in lst:
        print("You hit a wumpus!")
        lst.remove(guess)
    distance = []
    for w in lst:
        Manhattan = abs(int(guess[0]) - int(w[0])) + abs(int(guess[1]) - int(w[1]))
        distance.append(Manhattan)
    if len(lst) > 0:
        print(min(distance))
    moves += 1
# print("Your score is "+moves+" moves.")
print("Your score is "+ str(moves) +" moves.")
