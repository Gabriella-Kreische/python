import math

angle = float(input('Enter a angle: '))
sino = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print('The angle of {} has sino of {:.2f}!'.format(angle, sino))
print('The angle of {} has cosine of {:.2f}!'.format(angle, cosine))
print('The angle of {} has a tangent of {:.2f}.'.format(angle, tangent))
