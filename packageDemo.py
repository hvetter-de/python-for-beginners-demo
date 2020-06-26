# Demo how to use a package

import simplePackage.simpleMath
import simplePackage.dog
import math

# simpleMath
staticSum = simplePackage.simpleMath.simpleMath.staticSumNumbers(5,6)
print(f'StaticSum: {staticSum}')


# dog
dogInstance = simplePackage.dog.dog('Doggo')
dogInstance.add_trick('sit')
dogInstance.add_trick('come')

print('dog tricks:')
for trick in dogInstance.tricks:
    print(trick)