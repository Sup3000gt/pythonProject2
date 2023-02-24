import math

d, x, y, h = map(int, input().split())

bigTheta = math.atan((y+(h/2))/x)
Theta1 = bigTheta - math.atan(y/x)
Theta2 = bigTheta - math.atan((y-(h/2))/x)-Theta1
LowDistance = math.tan(Theta1)*d
HighDistance = math.tan(Theta2)*d

ans = LowDistance + HighDistance

print(ans)