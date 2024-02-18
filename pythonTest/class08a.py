'''
import math
num = int(input('Type a number: '))
root = math.sqrt(num)
print('The square root of {} is equal to {}'.format(num, math.floor(root)))

from math import sqrt
num = int(input('Type a number: '))
root = sqrt(num)
print('The square root of {} is equal to {:.2f}'.format(num, root))

import random
num = random.random()
print(num)
'''

import emoji
from emoji import emojize

msg = ":smile:"

print(emojize(":smiling_face_with_sunglasses:"))

