import math

angle = float(input('Type the angle: '))
sine = math.sin(angle)
cosine = math.cos(angle)
tangent = math.tan(angle)
print('The sine of {} angle is {:.2f}'.format(angle, sine))
print('The cosine of {} angle id {:.2f}'.format(angle, cosine))
print('The tangent of a {} angle is {:.2f}'.format(angle, tangent))
