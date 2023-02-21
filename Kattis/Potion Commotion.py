import sys

MaxHealth, M, Potion = map(int, input().split())
attack = input().split()
int_attack =[int(num) for num in attack]

currentHealth = MaxHealth

for i in range(M):
    if int_attack[i] >= MaxHealth:      # if any attack is greater than our maxHP, then we lost
        print("next time")
        sys.exit()
    currentHealth -= int_attack[i]      # take HP off everytime
    while i+1 <M and currentHealth <= int_attack[i+1]:  # if our HP is not enough to support us to take next attack
        if Potion > 0:                                  # we start to use potion
            currentHealth += 20
            Potion -= 1
            if currentHealth > MaxHealth:               # if potion is bigger than maxHP, then we set our currentHP
                currentHealth = MaxHealth               # to MaxHP
        else:                                           # otherwise means we don't have enough potion, we lost
            print("next time")
            sys.exit()
print("champion")                                       # if we complete the whole loop, without lost, we win






