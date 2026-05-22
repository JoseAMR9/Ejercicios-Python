import module

module.sumValue(1,2,3)
module.printValue("Hola")

from module import sumValue, printValue

sumValue(1,2,3)
printValue("Hola")

import math

print(math.pi)
print(math.pow(2,8))

from math import pi as PI_VALUE # as = alias

print(PI_VALUE)