# import sys
#
# N, M, P = map(int, input().split())
# attack = input().split()
# int_attack =[int(num) for num in attack]
# Total = 0
# for i in range (M):
#     Total += int(attack[i])
#     if int_attack[i] >= N or N + P*20 <= Total:
#         print("next time")
#         sys.exit()
# for i in range (M):
#     if i != M:
#         if N-int_attack[i] < int_attack[i+1] and P >= 1:
#             P -= 1
# print("champion")


N, M, P = map(int, input().split())
attack_damages = list(map(int, input().split()))

current_health = N
for damage in attack_damages:
    while damage > current_health and P > 0:
        P -= 1
        current_health += 20
    current_health -= damage
    if current_health <= 0:
        print("next time")
        break
else:
    print("champion")